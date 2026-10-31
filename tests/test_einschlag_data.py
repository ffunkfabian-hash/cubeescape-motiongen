"""data/einschlag.json (REF 0.36 "Impact") keeps the shape BALLON reads: unique row ids, every row names a known video, Destiny rows
have their `z-im-` anchor in docs/destiny2.md and comparison rows theirs in docs/einschlag.md, the transfer table uses BALLON class keys
and never invents metre values, and every video is listed in data/clips.json."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/einschlag.json").read_text(encoding="utf-8"))
D2 = (ROOT / "docs/destiny2.md").read_text(encoding="utf-8")
DOC = (ROOT / "docs/einschlag.md").read_text(encoding="utf-8")
ARTS = {"spur", "flug", "strahl", "schrot", "einschlag", "loch", "explosion", "laufrauch", "treffer"}
CLASSES = {"auto_rifle", "submachine_gun", "scout_rifle", "pulse_rifle", "sidearm", "machine_gun", "hand_cannon", "sniper_rifle",
           "shotgun", "grenade_launcher", "rocket_launcher", "trace_rifle", "fusion_rifle", "linear_fusion_rifle", "combat_bow"}
REQUIRED = ("id", "spiel", "waffe", "klasse", "art", "video", "zeit_s", "wert", "belegstaerke")


class ShapeTests(unittest.TestCase):
    def test_header(self):
        self.assertEqual(DATA["version"], "0.36.0")
        self.assertTrue(DATA["rows"])
        self.assertTrue(DATA["ballon_uebernahme"])

    def test_rows_have_unique_ids_and_known_videos(self):
        ids = [row["id"] for row in DATA["rows"]]
        self.assertEqual(len(ids), len(set(ids)))
        for row in DATA["rows"]:
            for field in REQUIRED:
                self.assertIn(field, row, f"{row.get('id')}: {field} fehlt")
            self.assertIn(row["art"], ARTS, row["id"])
            self.assertIn(row["video"], DATA["videos"], row["id"])
            self.assertIn(row["belegstaerke"], ("M", "O"), row["id"])
            if row["klasse"] is not None:
                self.assertIn(row["klasse"], CLASSES, row["id"])
            duration = DATA["videos"][row["video"]]["dauer_s"]
            self.assertLessEqual(row["zeit_s"], duration, f"{row['id']}: Zeit hinter dem Videoende")

    def test_anchors_exist(self):
        for row in DATA["rows"]:
            anchor = f'<a id="{row["id"]}"></a>'
            if row["spiel"] == "Destiny 2":
                self.assertTrue(row["id"].startswith("z-im-"), row["id"])
                self.assertIn(anchor, D2, row["id"])
            else:
                self.assertTrue(row["id"].startswith("i-"), row["id"])
                self.assertIn(anchor, DOC, row["id"])

    def test_transfer_table_uses_ballon_keys_and_no_metres(self):
        row_ids = {row["id"] for row in DATA["rows"]}
        for key, entry in DATA["ballon_uebernahme"].items():
            self.assertIn(key, CLASSES, key)
            for metre in ("speed_mps", "radius_m", "width_m", "length_m", "size_m"):
                self.assertIsNone(entry.get(metre), f"{key}.{metre}: aus Bildern nicht ableitbar")
            for ref in entry["belege"]:
                self.assertIn(ref, row_ids, f"{key}: {ref}")

    def test_frame_markers_are_non_negative_integers(self):
        def walk(value, where):
            if isinstance(value, list):
                for item in value:
                    walk(item, where)
            elif not isinstance(value, bool) and isinstance(value, (int, float)):
                self.assertEqual(value, int(value), where)
                self.assertGreaterEqual(value, 0, where)
        for row in DATA["rows"]:
            for name, value in (row.get("bilder") or {}).items():
                walk(value, f"{row['id']}.{name}")

    def test_time_matches_first_frame(self):
        for row in DATA["rows"]:
            fmt = DATA["videos"][row["video"]]["format"]
            fps = 29.97 if "29,97" in fmt else 59.94 if "59,94" in fmt else 60.0
            values = list((row.get("bilder") or {}).values())
            if not values:
                continue
            first = values[0][0] if isinstance(values[0], list) else values[0]
            self.assertAlmostEqual(row["zeit_s"], first / fps, delta=0.05, msg=row["id"])

    def test_videos_are_youtube_ids_listed_in_clips_json(self):
        clips = json.loads((ROOT / "data/clips.json").read_text(encoding="utf-8"))
        urls = {entry["clip"] for entry in clips}
        for vid in DATA["videos"]:
            self.assertRegex(vid, r"^[A-Za-z0-9_-]{11}$")
            self.assertIn(f"https://www.youtube.com/watch?v={vid}", urls, vid)

    def test_doc_links_to_rows(self):
        for anchor in re.findall(r"\(destiny2\.md#(z-im-[a-z0-9-]+)\)", DOC):
            self.assertIn(f'<a id="{anchor}"></a>', D2, anchor)


if __name__ == "__main__":
    unittest.main()
