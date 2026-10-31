"""data/verdict.json (REF 0.37 "Verdict") keeps the shape BALLON reads: one entry per BALLON class (16), every verdict comparison
names a known video and a valid result, contradictions carry a cause and a re-measurement row, the counts match the doc, unique
`z-v37-` row ids whose anchors exist in docs/destiny2.md, unknown values stay null, and every measured video is in data/clips.json."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/verdict.json").read_text(encoding="utf-8"))
DOC = (ROOT / "docs/destiny2.md").read_text(encoding="utf-8")
BALLON_CLASSES = {
    "auto_rifle", "submachine_gun", "scout_rifle", "pulse_rifle", "hand_cannon", "sidearm", "sniper_rifle", "trace_rifle",
    "machine_gun", "shotgun", "fusion_rifle", "linear_fusion_rifle", "combat_bow", "grenade_launcher", "rocket_launcher",
    "portal_cannon",
}
RESULTS = {"bestaetigt", "widerspricht", "neu", "nicht_belegt", "trifft_nicht_zu"}


class ShapeTests(unittest.TestCase):
    def test_header(self):
        self.assertEqual(DATA["version"], "0.37.0")
        self.assertEqual(DATA["name"], "Verdict")
        self.assertTrue(DATA["ballon_uebernahme"])

    def test_every_ballon_class_has_one_entry(self):
        names = [entry["ballon"] for entry in DATA["klassen"]]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(set(names), BALLON_CLASSES)

    def test_comparisons_name_known_videos_and_valid_results(self):
        for entry in DATA["klassen"]:
            self.assertTrue(entry["abgleich"], entry["ballon"])
            for vid in entry["videos"]:
                self.assertIn(vid, DATA["videos"], entry["ballon"])
            for item in entry["abgleich"]:
                self.assertIn(item["ergebnis"], RESULTS, entry["ballon"])
                if item["ergebnis"] in ("nicht_belegt", "trifft_nicht_zu"):
                    self.assertIsNone(item["urteil"], entry["ballon"])
                    self.assertTrue(item["ursache"], entry["ballon"])
                    continue
                self.assertIn(item["video"], entry["videos"], entry["ballon"])
                self.assertRegex(item["zeit"], r"^\d{2}:\d{2}$", entry["ballon"])

    def test_contradictions_have_cause_and_remeasurement(self):
        contradictions = [item for entry in DATA["klassen"] for item in entry["abgleich"] if item["ergebnis"] == "widerspricht"]
        self.assertTrue(contradictions)
        ids = {row["id"] for row in DATA["rows"]}
        for item in contradictions:
            self.assertTrue(item["ursache"], item["urteil"])
            self.assertIn(item["nachmessung"], ids, item["urteil"])

    def test_counts_match_comparisons_and_doc(self):
        counted = {key: 0 for key in DATA["zaehlung"]}
        for entry in DATA["klassen"]:
            for item in entry["abgleich"]:
                if item["ergebnis"] in counted:
                    counted[item["ergebnis"]] += 1
        self.assertEqual(counted, DATA["zaehlung"])
        z = DATA["zaehlung"]
        self.assertIn(f"{z['bestaetigt']} bestätigt / {z['widerspricht']} widerspricht / {z['neu']} neu", DOC)

    def test_rows_have_unique_ids_known_videos_and_doc_anchors(self):
        ids = [row["id"] for row in DATA["rows"]]
        self.assertEqual(len(ids), len(set(ids)))
        for row in DATA["rows"]:
            self.assertTrue(row["id"].startswith("z-v37-"), row["id"])
            self.assertIn(row["belegstaerke"], ("M", "O"), row["id"])
            self.assertIn(f'<a id="{row["id"]}"></a>', DOC, row["id"])
            for vid in row["videos"]:
                self.assertIn(vid, DATA["videos"], row["id"])

    def test_unknowns_are_null_not_zero(self):
        rows = {row["id"]: row["werte"] for row in DATA["rows"]}
        self.assertIsNone(rows["z-v37-tadel-flug"]["flugzeit_s"])
        self.assertIsNone(rows["z-v37-sprint"]["frequenz_hz"])
        self.assertIsNone(rows["z-v37-rl-gjallarhorn"]["zielen_aus_bis_huefte"])
        self.assertIsNone(rows["z-v37-rl-todbringer"]["ads"])
        self.assertIsNone(rows["z-v37-bewegung-o"]["takt_s"])
        self.assertEqual(DATA["einheiten"]["unbekannt"], "null")

    def test_walking_is_slower_than_the_sprint_stock(self):
        sprint_step = 0.317  # destiny2.md z-st-automatik-lastwish
        walking = next(row for row in DATA["rows"] if row["id"] == "z-v37-laufen")["werte"]
        for weapon, (low, high) in walking["periode_vertikal_s"].items():
            self.assertLessEqual(low, high, weapon)
            self.assertGreater(low, sprint_step, weapon)

    def test_sprint_boxes_are_inside_the_frame(self):
        sprint = next(row for row in DATA["rows"] if row["id"] == "z-v37-sprint")["werte"]
        for weapon, (x0, y0, x1, y1) in sprint["huelle"].items():
            self.assertTrue(0 <= x0 < x1 <= 100 and 0 <= y0 < y1 <= 100, weapon)
            self.assertIn(weapon, BALLON_CLASSES)

    def test_measured_videos_are_listed_in_clips_json(self):
        clips = json.loads((ROOT / "data/clips.json").read_text(encoding="utf-8"))
        urls = {entry["clip"] for entry in clips}
        for row in DATA["rows"]:
            for vid in row["videos"]:
                self.assertIn(f"https://www.youtube.com/watch?v={vid}", urls, vid)

    def test_videos_are_youtube_ids_with_dates(self):
        for vid, info in DATA["videos"].items():
            self.assertRegex(vid, r"^[A-Za-z0-9_-]{11}$")
            self.assertRegex(info["datum"], r"^\d{4}-\d{2}-\d{2}$", vid)
            self.assertEqual(info["kanal"], "Nexxoss Gaming", vid)
            self.assertRegex(info["format"], r"^\d+x\d+", vid)

    def test_ballon_list_anchors_exist_in_the_doc(self):
        for item in DATA["ballon_uebernahme"]:
            self.assertIn(f'<a id="{item["anker"]}"></a>', DOC, item["feld"])
            self.assertIn(item["staerke"], ("M", "O"), item["feld"])
            self.assertTrue(re.match(r"^(ACTIONS|CLASSES|reticles)", item["feld"]), item["feld"])


if __name__ == "__main__":
    unittest.main()
