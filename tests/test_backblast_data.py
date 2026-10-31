"""data/backblast.json (REF 0.35 "Backblast") keeps the shape BALLON reads: unique `z-bb-` row ids whose anchors exist in
docs/destiny2.md, every row and class names a known video, the image-share table covers all 15 Destiny classes with valid boxes
and area ranges, unknown values stay null, and every video is listed in data/clips.json."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/backblast.json").read_text(encoding="utf-8"))
DOC = (ROOT / "docs/destiny2.md").read_text(encoding="utf-8")
CLASSES = {
    "Automatikgewehr", "Impulsgewehr", "Scoutgewehr", "Maschinenpistole", "Handfeuerwaffe", "Seitenwaffe", "Scharfschütze",
    "Schrotflinte", "Spurgewehr", "Fusion (kurz)", "Lineares Fusionsgewehr", "Bogen", "Granatwerfer", "Raketenwerfer",
    "Maschinengewehr",
}
REQUIRED = ("id", "thema", "art", "typ", "belegstaerke", "waffe", "videos", "werte")


class ShapeTests(unittest.TestCase):
    def test_header(self):
        self.assertEqual(DATA["version"], "0.35.0")
        self.assertTrue(DATA["rows"])
        self.assertTrue(DATA["ballon_uebernahme"])

    def test_rows_have_unique_ids_known_videos_and_doc_anchors(self):
        ids = [row["id"] for row in DATA["rows"]]
        self.assertEqual(len(ids), len(set(ids)))
        for row in DATA["rows"]:
            for field in REQUIRED:
                self.assertIn(field, row, f"{row.get('id')}: {field} fehlt")
            self.assertTrue(row["id"].startswith("z-bb-"), row["id"])
            self.assertIn(row["belegstaerke"], ("M", "O"), row["id"])
            self.assertIn(f'<a id="{row["id"]}"></a>', DOC, row["id"])
            for vid in row["videos"]:
                self.assertIn(vid, DATA["videos"], f"{row['id']}: {vid}")

    def test_image_share_covers_every_class(self):
        self.assertEqual({entry["klasse"] for entry in DATA["bildanteil"]}, CLASSES)
        for entry in DATA["bildanteil"]:
            self.assertIn(entry["video"], DATA["videos"], entry["klasse"])
            for pose in ("huefte", "zielen"):
                value = entry[pose]
                if value["status"] == "O":
                    self.assertIsNone(value["flaeche_prozent"], entry["klasse"])
                    continue
                low, high = value["flaeche_prozent"]
                self.assertTrue(0 < low <= high, entry["klasse"])
                self.assertLess(high, 100, entry["klasse"])
                x0, y0, x1, y1 = value["box"]
                self.assertTrue(0 <= x0 < x1 <= 100 and 0 <= y0 < y1 <= 100, entry["klasse"])
                box_area = (x1 - x0) * (y1 - y0) / 100
                self.assertLessEqual(low, box_area + 0.5, f"{entry['klasse']} {pose}: Fläche größer als Box")

    def test_unknowns_are_null_not_zero(self):
        rl = next(row for row in DATA["rows"] if row["id"] == "z-bb-rl-huefte")
        for key in ("muendung", "rohrende", "griffhand", "nach_unten_geneigt"):
            self.assertIsNone(rl["werte"][key], key)

    def test_reload_durations_match_their_frame_markers(self):
        rows = [row["werte"] for row in DATA["rows"] if "marker_bild" in row["werte"]]
        self.assertGreaterEqual(len(rows), 2)
        for reload in rows:
            rate = reload["bildrate"]
            for weapon, (start, end) in reload["marker_bild"].items():
                self.assertAlmostEqual(reload["dauer_s"][weapon], (end - start) / rate, delta=1.5 / rate, msg=weapon)

    def test_every_video_is_listed_in_clips_json(self):
        clips = json.loads((ROOT / "data/clips.json").read_text(encoding="utf-8"))
        urls = {entry["clip"] for entry in clips}
        for vid in DATA["videos"]:
            self.assertIn(f"https://www.youtube.com/watch?v={vid}", urls, vid)

    def test_videos_are_youtube_ids_with_format(self):
        for vid, info in DATA["videos"].items():
            self.assertRegex(vid, r"^[A-Za-z0-9_-]{11}$")
            self.assertRegex(info["format"], r"^\d+x\d+ \d", vid)
            self.assertRegex(info["datum"], r"^\d{4}-\d{2}-\d{2}$", vid)

    def test_ballon_list_anchors_exist_in_the_doc(self):
        for item in DATA["ballon_uebernahme"]:
            for anchor in re.findall(r"z-bb-[a-z-]+", item["anker"]):
                self.assertIn(f'<a id="{anchor}"></a>', DOC, anchor)


if __name__ == "__main__":
    unittest.main()
