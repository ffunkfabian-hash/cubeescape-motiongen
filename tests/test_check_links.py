"""Manifest validation rejects malformed records without crashing."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_links", ROOT / "tools/check_links.py")
check_links = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_links)


class ManifestTests(unittest.TestCase):
    def test_valid_entry_is_collected(self):
        errors, clips = check_links.validate_manifest([{"measurement": "ADS", "clip": "url", "source": "channel",
                                                        "timestamps": "1s"}])
        self.assertEqual(errors, [])
        self.assertEqual(clips, {"url"})

    def test_non_object_and_missing_empty_whitespace_or_wrong_type_fields_are_errors(self):
        errors, clips = check_links.validate_manifest([
            4, {"measurement": " ", "clip": 3, "source": None, "timestamps": ""},
            {"measurement": "ok", "clip": "url", "source": "x"},
        ])
        self.assertEqual(clips, set())
        self.assertEqual(len(errors), 6)
        self.assertTrue(any("muss ein Objekt" in error for error in errors))
        self.assertTrue(any("timestamps" in error for error in errors))

    def test_root_must_be_a_list(self):
        errors, _ = check_links.validate_manifest({})
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
