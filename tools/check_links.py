#!/usr/bin/env python3
"""Checks the local Markdown links of the repository and that every measurement row names a clip listed in data/clips.json."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    errors = []
    for page in ROOT.rglob("*.md"):
        text = page.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (page.parent / target).exists():
                errors.append(f"{page.relative_to(ROOT)}: Verweis fehlt: {target}")
    clips = {entry["clip"] for entry in json.loads((ROOT / "data/clips.json").read_text(encoding="utf-8"))}
    for page in (ROOT / "docs").glob("*.md"):
        for line in page.read_text(encoding="utf-8").splitlines():
            if not line.startswith("| **"):
                continue
            for url in re.findall(r"`?((?:clips\.)?twitch\.tv/[^`\s)]+)`?", line):
                if "https://" + url not in clips:
                    errors.append(f"{page.relative_to(ROOT)}: Clip nicht in data/clips.json: {url}")
    for error in errors:
        print("FEHLER:", error)
    print("ok" if not errors else f"{len(errors)} Fehler")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
