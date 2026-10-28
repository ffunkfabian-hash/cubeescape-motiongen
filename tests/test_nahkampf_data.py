"""data/nahkampf.json (REF 0.29 "Bladework") keeps the shape the BALLON prototype reads: every example names game, subject,
status, source and notes; image positions are percentages; proportions of one weapon add up to its own length."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data/nahkampf.json").read_text(encoding="utf-8"))
STATUS = {"M", "O", "C", "S", "B"}
REQUIRED = ("game", "subject", "status", "source_url", "timestamp", "notes")
EXAMPLE_LISTS = ("proportions", "third_person", "ego_references", "glaive_ego")


def examples():
    for name in EXAMPLE_LISTS:
        for index, entry in enumerate(DATA[name]):
            yield f"{name}[{index}]", entry


def points(value):
    """Every [x, y] pair or [x0, x1, y0, y1] box inside a value, flattened to numbers."""
    if isinstance(value, dict):
        for item in value.values():
            yield from points(item)
    elif isinstance(value, list) and value and all(isinstance(v, (int, float)) or v is None for v in value):
        yield from (v for v in value if v is not None)
    elif isinstance(value, list):
        for item in value:
            yield from points(item)


class ShapeTests(unittest.TestCase):
    def test_header_names_version_doc_and_status_legend(self):
        self.assertEqual(DATA["doc"], "docs/nahkampf.md")
        self.assertTrue((ROOT / DATA["doc"]).exists())
        self.assertEqual(set(DATA["status"]), STATUS)

    def test_every_example_has_the_standard_fields(self):
        for where, entry in examples():
            for field in REQUIRED:
                self.assertIn(field, entry, f"{where}: {field} fehlt")
            self.assertIn(entry["status"], STATUS, where)
            self.assertTrue(str(entry["subject"]).strip(), where)
            self.assertTrue(str(entry["source_url"]).startswith("https://"), where)

    def test_positions_are_image_percentages(self):
        for where, entry in examples():
            for key in ("tip_xy", "hilt_xy", "bbox", "points", "figure_bbox", "shield_bbox", "blade_tip_xy"):
                for value in points(entry.get(key)):
                    self.assertTrue(0 <= value <= 100, f"{where}.{key}: {value} außerhalb 0–100 %")

    def test_frame_counts_are_positive_integers(self):
        for where, entry in examples():
            frames = entry.get("frames")
            if frames is not None:
                self.assertIsInstance(frames, int, where)
                self.assertGreater(frames, 0, where)


class ProportionTests(unittest.TestCase):
    def test_at_least_six_measured_swords_and_glaives(self):
        for cls in ("Schwert", "Glefe"):
            measured = [p for p in DATA["proportions"] if p["class"] == cls and p["status"] == "M" and not p["cut_off"]]
            self.assertGreaterEqual(len(measured), 6, cls)

    def test_sword_parts_add_up_to_its_length(self):
        for p in DATA["proportions"]:
            if p["class"] == "Schwert":
                self.assertAlmostEqual(p["grip_len"] + p["guard_len"] + p["blade_len"], 1.0, places=2, msg=p["subject"])
                self.assertLess(p["pommel_len"], p["grip_len"], p["subject"])

    def test_glaive_parts_add_up_to_its_length(self):
        for p in DATA["proportions"]:
            if p["class"] == "Glefe":
                self.assertAlmostEqual(p["shaft_len"] + p["head_len"], 1.0, places=2, msg=p["subject"])
                self.assertAlmostEqual(p["emitter_len"] + p["blade_len"], p["head_len"], places=2, msg=p["subject"])
                self.assertLess(p["front_grip"][0], p["front_grip"][1], p["subject"])

    def test_ratios_are_fractions_of_the_length(self):
        for p in DATA["proportions"]:
            for key, value in p.items():
                if key.endswith(("_len", "_w", "_w_med", "_w_max", "_span", "_pos")) and value is not None:
                    self.assertTrue(0 <= value <= 1, f"{p['subject']}.{key}: {value}")
            self.assertTrue(0 < p["h_to_l"] < 1, p["subject"])


class SummaryTests(unittest.TestCase):
    def test_summary_ranges_match_the_measured_weapons(self):
        def span(cls, key):
            values = [p[key] for p in DATA["proportions"] if p["class"] == cls and not p["cut_off"]]
            return [round(min(values), 2), round(max(values), 2)]

        sword, glaive = DATA["ballon_summary"]["sword"], DATA["ballon_summary"]["glaive"]
        for key in ("blade_len", "grip_len", "pommel_len", "guard_len"):
            self.assertEqual(sword[key], span("Schwert", key), key)
        self.assertEqual([sword["h_to_l_slim"][0], sword["h_to_l_wide"][1]], span("Schwert", "h_to_l"))
        for key in ("shaft_len", "head_len", "emitter_len", "blade_len", "h_to_l"):
            self.assertEqual(glaive[key], span("Glefe", key), key)

    def test_ballon_summary_and_open_points_exist(self):
        self.assertTrue(DATA["ballon_summary"])
        self.assertTrue(DATA["open"])
        self.assertEqual({o["option"] for o in DATA["sword_decision"]["options"]}, {"A", "B", "C"})


if __name__ == "__main__":
    unittest.main()
