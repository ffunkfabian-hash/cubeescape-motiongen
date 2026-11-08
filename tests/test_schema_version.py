"""Every data/*.json (REF 0.39 "Hallmark") is an object whose first key is `schema_version`, a positive integer: the version of the
file's format, raised only together with a migration (global rule 7). It is not the field `version`, which names the REF version of
the content. data/clips.json carries the version the link check reads (tools/check_links.py SCHEMA_VERSION)."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_links", ROOT / "tools/check_links.py")
check_links = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_links)
FILES = sorted((ROOT / "data").glob("*.json"))


class SchemaVersionTests(unittest.TestCase):
    def test_data_files_exist(self):
        self.assertGreaterEqual(len(FILES), 20)

    def test_every_data_file_is_an_object_with_schema_version_first(self):
        for path in FILES:
            with self.subTest(path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertIsInstance(data, dict, "Wurzel muss ein Objekt sein, sonst hat das Feld keinen Platz")
                self.assertEqual(next(iter(data), None), "schema_version", "schema_version steht als erster Schlüssel")
                version = data["schema_version"]
                self.assertIs(type(version), int, "ganze Zahl, kein Text und kein bool")
                self.assertGreaterEqual(version, 1)

    def test_clips_json_carries_the_version_the_link_check_reads(self):
        data = json.loads((ROOT / "data/clips.json").read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], check_links.SCHEMA_VERSION)
        self.assertEqual(check_links.validate_manifest(data)[0], [])


if __name__ == "__main__":
    unittest.main()
