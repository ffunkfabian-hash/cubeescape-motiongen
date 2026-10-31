"""data/gapfill.json (REF 0.34 "Gapfill") keeps the shape BALLON reads: unique row ids, every row names a known video and a
frame-based marker or a reason, every `z-g34-` anchor used by the BALLON list exists in docs/destiny2.md."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/gapfill.json").read_text(encoding="utf-8"))
DOC = (ROOT / "docs/destiny2.md").read_text(encoding="utf-8")
ARTS = {"adsEin", "adsAus", "ziehen", "weltzoom", "sprint", "gehen", "schuss", "huefte"}
REQUIRED = ("id", "waffe", "typ", "video", "art", "belegstaerke")


class ShapeTests(unittest.TestCase):
    def test_header(self):
        self.assertEqual(DATA["version"], "0.34.0")
        self.assertTrue(DATA["rows"])
        self.assertTrue(DATA["ballon_uebernahme"])

    def test_rows_have_unique_ids_and_known_videos(self):
        ids = [row["id"] for row in DATA["rows"]]
        self.assertEqual(len(ids), len(set(ids)))
        for row in DATA["rows"]:
            for field in REQUIRED:
                self.assertIn(field, row, f"{row.get('id')}: {field} fehlt")
            self.assertTrue(row["id"].startswith("z-g34-"), row["id"])
            self.assertIn(row["art"], ARTS, row["id"])
            self.assertIn(row["video"], DATA["videos"], row["id"])

    def test_videos_are_1080p60_youtube_ids(self):
        for vid, info in DATA["videos"].items():
            self.assertRegex(vid, r"^[A-Za-z0-9_-]{11}$")
            self.assertTrue(info["format"].startswith("1920x1080 60"), vid)

    def test_frame_markers_are_integers(self):
        for row in DATA["rows"]:
            for name, value in (row.get("marker") or {}).items():
                if isinstance(value, bool) or value is None:
                    continue
                if isinstance(value, (int, float)):
                    self.assertEqual(value, int(value), f"{row['id']}.{name}")
                    self.assertGreaterEqual(value, 0, f"{row['id']}.{name}")

    def test_ballon_list_anchors_exist_in_the_doc(self):
        for item in DATA["ballon_uebernahme"]:
            for anchor in re.findall(r"z-g34-[a-z]+", item["anker"]):
                self.assertIn(f'<a id="{anchor}"></a>', DOC, anchor)


if __name__ == "__main__":
    unittest.main()
