#!/usr/bin/env python3
"""Checks the local Markdown links of the repository and that every measurement row names a clip listed in data/clips.json."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate_manifest(manifest: object) -> tuple[list[str], set[str]]:
    errors = []
    clips = set()
    if not isinstance(manifest, list):
        return ["data/clips.json: Wurzel muss eine Liste sein"], clips
    required = ("measurement", "clip", "source", "timestamps")
    for index, entry in enumerate(manifest):
        if not isinstance(entry, dict):
            errors.append(f"data/clips.json[{index}]: Eintrag muss ein Objekt sein")
            continue
        valid = True
        for field in required:
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"data/clips.json[{index}].{field}: muss ein nichtleerer String sein")
                valid = False
        if valid:
            clips.add(entry["clip"])
    return errors, clips


def slug(heading: str) -> str:
    """GitHub's anchor for a heading: lower case, punctuation dropped, every space a hyphen."""
    text = re.sub(r"[^\w\s-]", "", heading.strip().lower())
    return re.sub(r"\s", "-", text)


def anchors_of(text: str) -> set[str]:
    """Anchors a Markdown page offers: explicit <a id="..."> plus the slug of every heading (repeats get -1, -2 ...)."""
    found = set(re.findall(r'<a\s+id="([^"]+)"', text))
    seen: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, flags=re.MULTILINE):
        base = slug(heading)
        count = seen.get(base, 0)
        found.add(base if count == 0 else f"{base}-{count}")
        seen[base] = count + 1
    return found


def check_anchors(root: Path) -> list[str]:
    """Links into this repository's pages must name an existing anchor and never a line number (#L123), which drifts with
    every inserted row."""
    pages = {page: page.read_text(encoding="utf-8") for page in root.rglob("*.md")}
    offered: dict[Path, set[str]] = {}
    errors = []
    for page, text in pages.items():
        for target, fragment in re.findall(r"\]\(([^)#\s]*)#([^)\s]+)\)", text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            goal = (page.parent / target).resolve() if target else page
            if goal not in pages:
                continue
            where = page.relative_to(root)
            if re.fullmatch(r"L\d+(?:-L\d+)?", fragment):
                errors.append(f"{where}: Zeilenanker #{fragment} – benannten Anker (<a id=...>) verwenden")
                continue
            if goal not in offered:
                offered[goal] = anchors_of(pages[goal])
            if fragment not in offered[goal]:
                errors.append(f"{where}: Anker fehlt: {target}#{fragment}")
    return errors


def main() -> int:
    errors = check_anchors(ROOT)
    for page in ROOT.rglob("*.md"):
        text = page.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (page.parent / target).exists():
                errors.append(f"{page.relative_to(ROOT)}: Verweis fehlt: {target}")
    try:
        manifest = json.loads((ROOT / "data/clips.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"data/clips.json: ungültige JSON-Datei: {exc}")
        manifest = []
    manifest_errors, clips = validate_manifest(manifest)
    errors.extend(manifest_errors)
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
