"""Manifest validation rejects malformed records without crashing."""
import importlib.util
import tempfile
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


class AnchorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)

    def write(self, name, text):
        (self.root / name).write_text(text, encoding="utf-8")

    def test_slug_follows_github_rules(self):
        self.assertEqual(check_links.slug("4. Vergleich mit den Vorbildern – nur Zahlen"), "4-vergleich-mit-den-vorbildern--nur-zahlen")
        self.assertEqual(check_links.slug("Übergänge (CE 0.95)"), "übergänge-ce-095")

    def test_duplicate_headings_get_numbered_slugs(self):
        self.assertEqual(check_links.anchors_of("# A\n## A\n<a id=\"x\"></a>"), {"a", "a-1", "x"})

    def test_named_and_heading_anchors_pass(self):
        self.write("a.md", "# Titel\n| **Zeile** <a id=\"z-eins\"></a> | x |\n")
        self.write("b.md", "[ok](a.md#z-eins) [auch](a.md#titel) [lokal](#kopf)\n## Kopf\n")
        self.assertEqual(check_links.check_anchors(self.root), [])

    def test_missing_anchor_and_line_anchor_are_errors(self):
        self.write("a.md", "# Titel\n")
        self.write("b.md", "[weg](a.md#fehlt) [zeile](a.md#L12) [bereich](a.md#L3-L9)\n")
        errors = check_links.check_anchors(self.root)
        self.assertEqual(len(errors), 3)
        self.assertTrue(any("Anker fehlt: a.md#fehlt" in e for e in errors))
        self.assertEqual(sum("Zeilenanker" in e for e in errors), 2)

    def test_external_links_and_unknown_files_are_ignored(self):
        self.write("a.md", "[x](https://example.org/p.md#L5) [y](nicht-da.md#L5)\n")
        self.assertEqual(check_links.check_anchors(self.root), [])


if __name__ == "__main__":
    unittest.main()
