"""data/aussenansicht.json (REF 0.32 "Spectator") keeps the shape Critic and BALLON read: every example names game, subject,
status, source and notes; body sizes are body heights (KH), image positions percentages, frame counts whole pictures."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/aussenansicht.json").read_text(encoding="utf-8"))
STATUS = {"M", "O", "C", "S", "B"}
REQUIRED = ("game", "subject", "status", "source_url", "timestamp", "notes")


def examples():
    for name in ("body_motion", "weapon_body"):
        for index, entry in enumerate(DATA[name]):
            yield f"{name}[{index}]", entry


def numbers(value):
    if isinstance(value, (int, float)):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from numbers(item)


class ShapeTests(unittest.TestCase):
    def test_header_names_version_doc_and_status_legend(self):
        self.assertEqual(DATA["doc"], "docs/aussenansicht.md")
        self.assertTrue((ROOT / DATA["doc"]).exists())
        self.assertEqual(set(DATA["status"]), STATUS)

    def test_every_example_has_the_standard_fields(self):
        for where, entry in examples():
            for field in REQUIRED:
                self.assertIn(field, entry, f"{where}: {field} fehlt")
            self.assertTrue(set(entry["status"].split("/")) <= STATUS, where)
            self.assertTrue(str(entry["subject"]).strip(), where)
            self.assertTrue(entry["source_url"].startswith("https://"), where)

    def test_both_goals_cover_at_least_three_games(self):
        for name in ("body_motion", "weapon_body"):
            self.assertGreaterEqual(len({e["game"] for e in DATA[name]}), 3, name)

    def test_sizes_are_body_heights_and_percentages(self):
        for where, entry in examples():
            for key in ("stride_kh", "bob_kh", "sway_kh", "weapon_len_kh", "hand_len_kh", "kh_ratio"):
                self.assertNotIsInstance(entry.get(key), str, f"{where}.{key}: Zahl erwartet")
                for value in numbers(entry.get(key)):
                    self.assertTrue(0 <= value <= 2, f"{where}.{key}: {value} KH")
            for value in numbers(entry.get("figure_h_pct")):
                self.assertTrue(0 < value <= 100, f"{where}.figure_h_pct: {value}")
        for hand in DATA["hand_size"]:
            for value in numbers(hand["hand_kh"]):
                self.assertTrue(0.02 <= value <= 0.25, hand["figure"])

    def test_frame_counts_are_positive_integers(self):
        for where, entry in examples():
            frames = entry.get("frames")
            if frames is not None:
                self.assertIsInstance(frames, int, where)
                self.assertGreater(frames, 0, where)

    def test_evaluation_has_player_sources(self):
        for entry in DATA["evaluation"]:
            sources = entry["player_opinion"]["sources"]
            self.assertTrue(sources, entry["subject"])
            self.assertTrue(all(url.startswith("https://") for url in sources), entry["subject"])

    def test_minimum_voices_and_dev_sources_per_goal(self):
        for goal in (1, 2):
            voices = [v for v in DATA["player_voices"] if goal in (v["goal"] if isinstance(v["goal"], list) else [v["goal"]])]
            devs = [d for d in DATA["dev_sources"] if goal in (d["goal"] if isinstance(d["goal"], list) else [d["goal"]])]
            self.assertGreaterEqual(sum(len(v["sources"]) for v in voices), 5, f"Ziel {goal}: Spielerquellen")
            self.assertGreaterEqual(len(devs), 2, f"Ziel {goal}: Fachquellen")


if __name__ == "__main__":
    unittest.main()
