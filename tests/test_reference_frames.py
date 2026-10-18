"""reference_frames: the sheets cover a window without gaps, the native rate puts one picture per tile, the cross is optional."""
import importlib.util
import contextlib
import io
import json
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
