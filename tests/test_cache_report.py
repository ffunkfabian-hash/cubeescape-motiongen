import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import cache_report  # noqa: E402


class CacheReportTests(unittest.TestCase):
    def test_scan_counts_video_and_skips_links(self):
        with tempfile.TemporaryDirectory() as root:
            os.makedirs(os.path.join(root, "thema"))
            for name, size in (("a.mp4", 100), ("b.png", 50), ("c.mp4.part", 10)):
                with open(os.path.join(root, "thema", name), "wb") as fh:
                    fh.write(b"x" * size)
            os.symlink("/nonexistent", os.path.join(root, "thema", "broken.mp4"))
            self.assertEqual(cache_report.scan(root), {"thema": [160, 110]})

    def test_missing_root_is_empty(self):
        self.assertEqual(cache_report.scan("/nonexistent-cache-root"), {})


if __name__ == "__main__":
    unittest.main()
