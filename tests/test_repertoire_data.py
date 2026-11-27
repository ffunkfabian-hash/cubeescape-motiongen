"""data/repertoire.json (REF 0.43 "Repertoire") keeps the shape Critic, BALLON and Cube Escape read: every example names game, subject,
category, status, source and notes; heights are body heights (KH), frame counts whole pictures; player voices carry URL and date."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/repertoire.json").read_text(encoding="utf-8"))
STATUS = {"M", "O", "C", "S", "B"}
REQUIRED = ("game", "subject", "category", "status", "source_url", "timestamp", "notes")
CATEGORIES = {"stance", "locomotion", "crouch", "slide", "jump", "fall_land", "climb", "evade", "cover", "traverse", "ability",
              "emote", "finisher", "reload", "draw", "fire_pose", "hold_pose"}


class ShapeTests(unittest.TestCase):
    def test_header(self):
        self.assertEqual(DATA["doc"], "docs/repertoire.md")
        self.assertTrue((ROOT / DATA["doc"]).exists())
        self.assertEqual(set(DATA["status"]), STATUS)
        self.assertEqual(len(DATA["goals"]), 2)

    def test_every_example_has_the_standard_fields(self):
        for index, entry in enumerate(DATA["examples"]):
            where = f"examples[{index}]"
            for field in REQUIRED:
                self.assertIn(field, entry, f"{where}: {field} fehlt")
            self.assertIn(entry["status"], STATUS, where)
            self.assertIn(entry["category"], CATEGORIES, where)
            self.assertTrue(entry["source_url"].startswith("https://www.youtube.com/watch?v="), where)

    def test_both_goals_and_both_games_are_covered(self):
        games = {e["game"] for e in DATA["examples"]}
        self.assertTrue({"Destiny 2", "The Division 2"} <= games)
        cats = {e["category"] for e in DATA["examples"]}
        self.assertIn("reload", cats)
        self.assertIn("hold_pose", cats)
        self.assertTrue(cats & {"crouch", "slide", "jump", "cover"})

    def test_heights_are_body_heights_and_frames_positive(self):
        for index, entry in enumerate(DATA["examples"]):
            kh = entry.get("kh")
            if isinstance(kh, (int, float)):
                self.assertTrue(0 < kh <= 1.2, f"examples[{index}].kh {kh}")
            frames = entry.get("duration_frames")
            if isinstance(frames, (int, float)):
                self.assertGreater(frames, 0, f"examples[{index}]")

    def test_voices_and_sources_name_url_and_date(self):
        self.assertGreaterEqual(len(DATA["player_voices"]), 20)
        for voice in DATA["player_voices"]:
            self.assertTrue(voice["url"].startswith("https://www.reddit.com/r/"), voice["id"])
            self.assertRegex(voice["date"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertGreaterEqual(len(DATA["dev_sources"]), 2)


if __name__ == "__main__":
    unittest.main()
