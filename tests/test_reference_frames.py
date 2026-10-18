"""reference_frames: the sheets cover a window without gaps, the native rate puts one picture per tile, the cross is optional."""
import importlib.util
import contextlib
import io
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("reference_frames", ROOT / "tools/reference_frames.py")
reference_frames = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(reference_frames)


class WindowTests(unittest.TestCase):
    def test_a_window_is_split_into_sheets_of_cols_times_rows_pictures(self):
        spans = reference_frames.windows(3.0, 4.0, 60, 30)   # 60 pictures, 30 per sheet
        self.assertEqual(len(spans), 2)
        self.assertAlmostEqual(spans[0][0], 3.0)
        self.assertAlmostEqual(spans[0][1], 3.5)
        self.assertAlmostEqual(spans[1][0], 3.5)
        self.assertAlmostEqual(spans[1][1], 4.0)

    def test_the_last_sheet_ends_at_the_window_and_an_empty_tail_is_dropped(self):
        spans = reference_frames.windows(0.0, 0.75, 10, 5)   # 7.5 pictures: 5 + 2.5
        self.assertEqual(len(spans), 2)
        self.assertAlmostEqual(spans[1][1], 0.75)
        self.assertEqual(reference_frames.windows(0.0, 0.5, 10, 5), [(0.0, 0.5)], "exactly one full sheet")
        self.assertEqual(reference_frames.windows(2.0, 2.0, 10, 5), [], "an empty window has no sheet")
        self.assertEqual(reference_frames.windows(2.0, 1.0, 10, 5), [], "a reversed window has no sheet")

    def test_the_overview_rate_covers_fifteen_seconds_per_sheet(self):
        spans = reference_frames.windows(0.0, 40.0, 2, 30)
        self.assertEqual(len(spans), 3)
        self.assertAlmostEqual(spans[0][1] - spans[0][0], 15.0)


class FilterTests(unittest.TestCase):
    def test_the_filter_samples_labels_and_tiles(self):
        graph = reference_frames.filter_graph(60, 480, 6, 5, cross=False)
        self.assertTrue(graph.startswith("fps=60,"))
        self.assertIn("scale=480:-2", graph)
        self.assertIn("drawtext", graph)
        self.assertIn("pts", graph, "the label is the clip time")
        self.assertTrue(graph.endswith("tile=6x5:padding=2:color=black"))
        self.assertNotIn("drawbox", graph)

    def test_the_cross_marks_the_screen_centre_before_scaling(self):
        graph = reference_frames.filter_graph(10, 400, 6, 5, cross=True)
        self.assertEqual(graph.count("drawbox"), 3, "two lines and the centre square")
        self.assertLess(graph.index("drawbox"), graph.index("scale="), "drawn on the full picture, scaled afterwards")
        self.assertIn("x=iw/2", graph)
        self.assertIn("y=ih/2", graph)


class SheetTests(unittest.TestCase):
    def test_native_sheet_selects_exact_source_frames_for_an_off_grid_interval(self):
        records = [(31, 1.001), (32, 1.034367), (33, 1.067733)]
        with tempfile.TemporaryDirectory() as scratch, \
             patch.object(reference_frames, "info", return_value=(30000 / 1001, 3.0, 640, 480)), \
             patch.object(reference_frames, "frame_records", return_value=records) as probe, \
             patch.object(reference_frames.subprocess, "check_call") as ffmpeg:
            outputs = reference_frames.sheet("clip.mp4", str(Path(scratch) / "native"), 1.0, 1.1, None, 6, 5, 200)

        self.assertEqual(probe.call_args.args, ("clip.mp4", 1.0, 1.1))
        self.assertEqual(len(outputs), 1)
        command = ffmpeg.call_args.args[0]
        self.assertIn("-copyts", command)
        self.assertEqual(command[command.index("-map") + 1], "0:v:0")
        self.assertNotIn("-ss", command)
        graph = command[command.index("-vf") + 1]
        self.assertTrue(graph.startswith("select='eq(n\\,31)+eq(n\\,32)+eq(n\\,33)',"))
        self.assertNotIn("fps=", graph)
        self.assertTrue(outputs[0].endswith("native_00.jpg"))

    def test_numeric_sheet_keeps_fps_sampling_path(self):
        with tempfile.TemporaryDirectory() as scratch, \
             patch.object(reference_frames, "info", return_value=(30000 / 1001, 3.0, 640, 480)), \
             patch.object(reference_frames.subprocess, "check_call") as ffmpeg:
            reference_frames.sheet("clip.mp4", str(Path(scratch) / "search"), 1.0, 1.5, 10, 2, 2, 200)

        command = ffmpeg.call_args.args[0]
        self.assertIn("-ss", command)
        self.assertIn("fps=10,", command[command.index("-vf") + 1])

    @unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg and ffprobe are required")
    def test_native_cli_sheet_pixels_match_source_frames_across_a_timestamp_gap(self):
        colors = [(240, 20, 20), (20, 240, 20), (20, 20, 240), (230, 230, 20), (230, 20, 230), (20, 230, 230)]
        frame = 64 * 64
        raw = b"".join(bytes(color) * frame for color in colors)
        with tempfile.TemporaryDirectory() as scratch:
            clip = Path(scratch) / "colors.mkv"
            prefix = Path(scratch) / "native"
            # A PTS gap would make fps resampling duplicate a color and lose native frame identity.
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pixel_format", "rgb24",
                            "-video_size", "64x64", "-framerate", "30000/1001", "-i", "pipe:0",
                            "-vf", "setpts=if(gte(N\\,3)\\,PTS+2\\,PTS)", "-fps_mode", "vfr",
                            "-c:v", "ffv1", "-pix_fmt", "rgb24", str(clip)], input=raw, check=True)

            records = reference_frames.frame_records(str(clip), .05, .215)
            self.assertEqual([index for index, _ in records], [2, 3, 4])
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(reference_frames.main(["sheet", str(clip), ".05", ".215", "--fps", "native",
                                                        "--out", str(prefix), "--cols", "3", "--rows", "1", "--tile", "64"]), 0)

            contact_sheet = Path(f"{prefix}_00.jpg")
            dimensions = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0",
                                                  "-show_entries", "stream=width,height", "-of", "csv=s=x:p=0",
                                                  str(contact_sheet)], text=True).strip()
            width, height = map(int, dimensions.split("x"))
            pixels = subprocess.check_output(["ffmpeg", "-v", "error", "-i", str(contact_sheet), "-f", "rawvideo",
                                              "-pix_fmt", "rgb24", "pipe:1"])
            self.assertEqual(len(pixels), width * height * 3)
            for tile_index, source_index in enumerate((2, 3, 4)):
                x, y = 34 + tile_index * 66, 48
                offset = (y * width + x) * 3
                actual = tuple(pixels[offset:offset + 3])
                expected = colors[source_index]
                self.assertLess(max(abs(actual[channel] - expected[channel]) for channel in range(3)), 35,
                                f"tile {tile_index} should contain source frame {source_index}: {actual} vs {expected}")


class YtDlpCommandTests(unittest.TestCase):
    def test_list_and_fetch_use_cli_or_module_fallback(self):
        for executable, expected_prefix in (("/usr/bin/yt-dlp", ["/usr/bin/yt-dlp"]),
                                             (None, [reference_frames.sys.executable, "-m", "yt_dlp"])):
            with self.subTest(executable=executable), tempfile.TemporaryDirectory() as scratch:
                with patch.object(reference_frames.shutil, "which", return_value=executable), \
                     patch.object(reference_frames.subprocess, "call", return_value=0) as call:
                    self.assertEqual(reference_frames.list_clips("channel", 12), 0)
                list_command = call.call_args.args[0]
                self.assertEqual(list_command[:len(expected_prefix)], expected_prefix)
                self.assertIn("--flat-playlist", list_command)
                self.assertEqual(list_command[-1], "https://www.twitch.tv/channel/clips?filter=clips&range=all")

                clip_path = Path(scratch) / "download.mp4"
                clip_path.touch()
                with patch.object(reference_frames.shutil, "which", return_value=executable), \
                     patch.object(reference_frames.subprocess, "call", return_value=0) as call, \
                     patch.object(reference_frames, "info", return_value=(60, 4.0, 1280, 720)):
                    self.assertEqual(reference_frames.fetch("clip-slug", scratch), 0)
                fetch_command = call.call_args.args[0]
                self.assertEqual(fetch_command[:len(expected_prefix)], expected_prefix)
                self.assertEqual(fetch_command[len(expected_prefix):len(expected_prefix) + 3], ["-q", "--no-warnings", "-f"])
                self.assertEqual(fetch_command[-1], "https://clips.twitch.tv/clip-slug")


class MeasureTests(unittest.TestCase):
    def test_frame_records_keep_source_indexes_and_half_open_native_pts(self):
        payload = {"frames": [{"best_effort_timestamp_time": t} for t in
                              ("0.967633", "1.001000", None, "1.034367", "1.067733", "1.101100")]}
        with patch.object(reference_frames.subprocess, "check_output", return_value=json.dumps(payload).encode()):
            self.assertEqual(reference_frames.frame_records("clip.mp4", 1.0, 1.067733),
                             [(1, 1.001), (3, 1.034367)])

    def test_sheet_symlink_into_repo_is_rejected_before_ffmpeg(self):
        with tempfile.TemporaryDirectory() as scratch:
            prefix = Path(scratch) / "sheet"
            Path(f"{prefix}_00.jpg").symlink_to(ROOT / "README.md")
            with patch.object(reference_frames, "info", return_value=(60, 3, 640, 480)), \
                 patch.object(reference_frames, "frame_records", return_value=[(1, .1)]), \
                 patch.object(reference_frames.subprocess, "check_call") as ffmpeg:
                with self.assertRaisesRegex(ValueError, "Repository"):
                    reference_frames.measure("clip.mp4", 0, 1, "native", False, str(Path(scratch) / "times.txt"),
                                             "", "", "", str(prefix))
            ffmpeg.assert_not_called()
            self.assertFalse((Path(scratch) / "times.txt").exists())

    def test_native_measure_uses_pts_for_list_text_and_contact_sheet(self):
        # 30000/1001 is not an integer rate, and this interval starts between frames.
        pts = [1.001, 1.034367, 1.067733]
        with tempfile.TemporaryDirectory() as scratch:
            text_path = Path(scratch) / "times.txt"
            prefix = Path(scratch) / "sheet"
            with patch.object(reference_frames, "info", return_value=(30000 / 1001, 3.0, 1920, 1080)), \
                 patch.object(reference_frames, "frame_records", return_value=list(enumerate(pts, start=10))) as probe, \
                 patch.object(reference_frames.subprocess, "check_call") as ffmpeg, \
                 contextlib.redirect_stdout(io.StringIO()) as stdout:
                result = reference_frames.measure("clip.mp4", 1.0, 1.1, "native", True, str(text_path),
                                                  "ADS", "https://clips.twitch.tv/test", "Channel, 2026-01-01",
                                                  str(prefix), 6, 5, 480)
            self.assertEqual(result, 0)
            probe.assert_called_once_with("clip.mp4", 1.0, 1.1)
            self.assertEqual(text_path.read_text().splitlines()[1:],
                             [f"{i}, {t:.6f}" for i, t in enumerate(pts, 1)])
            proposal_text = stdout.getvalue().split("Entwurf für data/clips.json (keine Metadaten ergänzt):\n", 1)[1]
            proposal, _ = json.JSONDecoder().raw_decode(proposal_text)
            self.assertEqual(proposal["measurement"], "ADS")
            self.assertEqual(proposal["clip"], "https://clips.twitch.tv/test")
            self.assertEqual(proposal["source"], "Channel, 2026-01-01")
            self.assertEqual(proposal["timestamps"], "1.001000 s, 1.034367 s, 1.067733 s")
            args = ffmpeg.call_args.args[0]
            self.assertIn("-copyts", args)
            self.assertEqual(args[args.index("-map") + 1], "0:v:0")
            self.assertIn("select='eq(n\\,10)+eq(n\\,11)+eq(n\\,12)'", args[args.index("-vf") + 1])
            self.assertIn("drawbox", args[args.index("-vf") + 1])
            self.assertTrue(args[-1].endswith("sheet_00.jpg"))

    def test_rejects_invalid_intervals_and_repo_outputs(self):
        with self.assertRaisesRegex(ValueError, "Intervall"):
            reference_frames.measure("clip.mp4", 2, 1, "native", False, None, "", "", "")
        with tempfile.TemporaryDirectory() as scratch:
            alias = Path(scratch) / "repo-link"
            alias.symlink_to(ROOT, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "Repository"):
                reference_frames.scratch_path(str(alias / "result.txt"))
            file_alias = Path(scratch) / "repo-file.txt"
            file_alias.symlink_to(ROOT / "README.md")
            with self.assertRaisesRegex(ValueError, "Repository"):
                reference_frames.measure("clip.mp4", 0, 1, "native", False, str(file_alias), "", "", "")

    def test_contact_sheet_pages_select_distinct_lists_of_source_frames(self):
        with tempfile.TemporaryDirectory() as scratch:
            with patch.object(reference_frames, "info", return_value=(30, 3.0, 640, 480)), \
                 patch.object(reference_frames, "frame_records", return_value=[(2, .1), (3, .2), (4, .3)]), \
                 patch.object(reference_frames.subprocess, "check_call") as ffmpeg, \
                 contextlib.redirect_stdout(io.StringIO()):
                reference_frames.measure("clip.mp4", 0, 1, "native", False, str(Path(scratch) / "t.txt"),
                                         "", "", "", str(Path(scratch) / "pages"), 2, 1, 100)
            graphs = [call.args[0][call.args[0].index("-vf") + 1] for call in ffmpeg.call_args_list]
            self.assertIn("eq(n\\,2)+eq(n\\,3)", graphs[0])
            self.assertIn("eq(n\\,4)", graphs[1])
            self.assertNotEqual(graphs[0], graphs[1])


if __name__ == "__main__":
    unittest.main()
