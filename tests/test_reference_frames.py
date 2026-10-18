"""reference_frames: the sheets cover a window without gaps, the native rate puts one picture per tile, the cross is optional."""
import importlib.util
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()
