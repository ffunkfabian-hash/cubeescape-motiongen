#!/usr/bin/env python3
"""Read-only report on the reference cache (docs/standard.md, section 'Aufräumen').

    python3 tools/cache_report.py [--root DIR] [--limit-gb 15]

Prints size per work folder and how much of it is downloaded video. Exit code 1 when the total exceeds the limit
(a warning, nothing is ever deleted).
"""
from __future__ import annotations

import argparse
import os
import sys

VIDEO = (".mp4", ".webm", ".mkv", ".part")
DEFAULT_ROOT = os.path.expanduser("~/Library/Caches/CubeEscape/reference")


def scan(root: str) -> dict[str, list[int]]:
    """Return {top-level folder: [total bytes, video bytes]}; symlinks are skipped."""
    out: dict[str, list[int]] = {}
    if not os.path.isdir(root):
        return out
    for top in sorted(os.listdir(root)):
        path = os.path.join(root, top)
        total = video = 0
        for cur, _dirs, files in os.walk(path):
            for name in files:
                full = os.path.join(cur, name)
                if os.path.islink(full):
                    continue
                size = os.path.getsize(full)
                total += size
                if name.lower().endswith(VIDEO) or ".part" in name:
                    video += size
        out[top] = [total, video]
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--limit-gb", type=float, default=15.0)
    args = ap.parse_args()
    data = scan(args.root)
    total = sum(v[0] for v in data.values())
    for top, (size, video) in sorted(data.items(), key=lambda kv: -kv[1][0]):
        print(f"{size / 1e9:7.1f} GB  davon Video {video / 1e9:6.1f} GB  {top}")
    print(f"{total / 1e9:7.1f} GB  gesamt (Grenze {args.limit_gb:g} GB)")
    if total > args.limit_gb * 1e9:
        print("WARNUNG: Cache über der Grenze - Videos und .part der abgeschlossenen Themen löschen "
              "(docs/standard.md, Aufräumen).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
