#!/usr/bin/env python3
"""Measures reference footage frame by frame (docs/destiny2.md › 2; Cube Escape Docs/FIRST_PERSON_EQUIPMENT.md › 1).

The reference for the first-person feel is Destiny 2; its timings (ADS blend, sprint pose, recoil return, reload events, bow
draw …) are read off 60-fps Twitch clips: contact sheets with a burned-in timestamp, sighted picture by picture. This tool is the
whole way, so a session can repeat or extend the measurement without rediscovering it:

    python3 Tools/reference_frames.py list <channel> [--top 100]           # the channel's most viewed clips: id|url|title|s|views
    python3 Tools/reference_frames.py fetch <clip url|slug> [--out DIR]    # download (yt-dlp, best stream up to 1080p), print fps
    python3 Tools/reference_frames.py overview <clip.mp4> [--out PREFIX]   # 2 pictures/s, 6 × 5 per sheet = 15 s - find the moments
    python3 Tools/reference_frames.py sheet <clip.mp4> START END [--fps 10|60] [--out PREFIX] [--cols 6 --rows 5 --tile 480]
                                                                           # 10/s to narrow down, 60/s (native) to measure;
                                                                           # --cross marks the screen centre (where the game aims)

Reading a measurement: the label on each tile is the clip time in h:mm:ss.fff; at the clip's native rate one tile is one picture, so
a span in pictures is the difference of the labels divided by the frame time (16.7 ms at 60/s). Accuracy is ±1 picture at the
native rate and ±0.05 s on a 10/s sheet. Write the result into the table of › 1.2a with the clip (channel, slug, date), the
timestamps and what was seen; the numbers of one clip are an example of one weapon with unknown stats, never a type's mean.

Cloud sessions: YouTube is blocked (bot check); Twitch clips load. Nothing here touches the repository - clips and sheets belong in
the session's scratch folder (--out). Needs yt-dlp and ffmpeg/ffprobe on PATH.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
from pathlib import Path

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
TWITCH_CLIP_PREFIX = "https://clips.twitch.tv/"


def info(path: str) -> tuple[float, float, int, int]:
    """Frame rate, duration, width, height of the first video stream."""
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                   "stream=r_frame_rate,width,height,duration", "-of", "json", path])
    stream = json.loads(out)["streams"][0]
    num, den = stream["r_frame_rate"].split("/")
    duration = float(stream.get("duration") or 0)
    if duration <= 0:   # some containers keep it on the format only
        out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", path])
        duration = float(json.loads(out)["format"].get("duration") or 0)
    return float(num) / float(den), duration, int(stream["width"]), int(stream["height"])


def windows(start: float, end: float, fps: float, per_sheet: int) -> list[tuple[float, float]]:
    """The [t0, t1) spans of the sheets covering [start, end) at `fps` with `per_sheet` pictures each; a last span that would hold
    no picture is left out."""
    if end <= start or fps <= 0 or per_sheet <= 0:
        return []
    total = int(math.ceil((end - start) * fps))
    spans = []
    for index in range(int(math.ceil(total / per_sheet))):
        t0 = start + index * per_sheet / fps
        t1 = min(end, t0 + per_sheet / fps)
        if t1 - t0 < 0.5 / fps:
            break
        spans.append((t0, t1))
    return spans


def filter_graph(fps: float, tile_width: int, cols: int, rows: int, cross: bool) -> str:
    """The ffmpeg video filter of one sheet: sample at `fps`, optionally the centre cross, scale, time label, tile."""
    label = "text='%{pts\\:hms}':x=6:y=6:fontsize=20:fontcolor=yellow:box=1:boxcolor=black@0.6"
    centre = ("drawbox=x=iw/2-1:y=0:w=2:h=ih:color=cyan@0.5:t=fill,drawbox=x=0:y=ih/2-1:w=iw:h=2:color=cyan@0.5:t=fill,"
              "drawbox=x=iw/2-ih/40:y=ih/2-ih/40:w=ih/20:h=ih/20:color=cyan@0.8:t=2," if cross else "")
    return f"fps={fps},{centre}scale={tile_width}:-2,drawtext=fontfile={FONT}:{label},tile={cols}x{rows}:padding=2:color=black"


def sheet(path: str, prefix: str, start: float, end: float, fps: float, cols: int, rows: int, tile_width: int,
          cross: bool = False) -> list[str]:
    """Contact sheets covering [start, end) at `fps`, cols × rows tiles each, the clip time burned into every tile; `cross` draws
    the screen centre (the aim point of the game) into every picture, so the offset of muzzle, sight and tracer can be read off."""
    _, duration, _, _ = info(path)
    outputs = []
    for index, (t0, t1) in enumerate(windows(start, min(end, duration), fps, cols * rows)):
        output = f"{prefix}_{index:02d}.jpg"
        subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t0:.3f}", "-to", f"{t1:.3f}", "-copyts", "-i", path,
                               "-vf", filter_graph(fps, tile_width, cols, rows, cross), "-frames:v", "1", "-q:v", "4", output])
        outputs.append(output)
    return outputs


def list_clips(channel: str, top: int) -> int:
    url = f"https://www.twitch.tv/{channel}/clips?filter=clips&range=all"
    command = ["yt-dlp", "--flat-playlist", "--print", "%(id)s|%(url)s|%(title)s|%(duration)s|%(view_count)s",
               "--playlist-end", str(top), url]
    return subprocess.call(command)


def fetch(clip: str, out_dir: str) -> int:
    url = clip if clip.startswith("http") else TWITCH_CLIP_PREFIX + clip
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    template = os.path.join(out_dir, "%(uploader)s_%(id)s.%(ext)s")
    code = subprocess.call(["yt-dlp", "-q", "--no-warnings", "-f", "best[height<=1080]", "-o", template, url])
    if code != 0:
        return code
    newest = max(Path(out_dir).glob("*.mp4"), key=lambda p: p.stat().st_mtime)
    fps, duration, width, height = info(str(newest))
    print(f"{newest} {width}x{height} {fps:g}/s {duration:.1f} s")
    return 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    lister = commands.add_parser("list", help="most viewed clips of a Twitch channel")
    lister.add_argument("channel")
    lister.add_argument("--top", type=int, default=100)
    fetcher = commands.add_parser("fetch", help="download one clip")
    fetcher.add_argument("clip", help="clip URL or Twitch slug")
    fetcher.add_argument("--out", default=".")
    overview = commands.add_parser("overview", help="2 pictures/s over the whole clip")
    overview.add_argument("clip")
    overview.add_argument("--out", help="prefix of the sheets (default: next to the clip)")
    window = commands.add_parser("sheet", help="a window at 10/s (search) or the native rate (measure)")
    window.add_argument("clip")
    window.add_argument("start", type=float)
    window.add_argument("end", type=float)
    window.add_argument("--fps", default="60", help="pictures per second, or 'native' for the clip's own rate (default 60)")
    window.add_argument("--out")
    window.add_argument("--cols", type=int, default=6)
    window.add_argument("--rows", type=int, default=5)
    window.add_argument("--tile", type=int, default=480)
    window.add_argument("--cross", action="store_true", help="draw the screen centre (aim point) into every picture")
    args = parser.parse_args(argv)

    if args.command == "list":
        return list_clips(args.channel, args.top)
    if args.command == "fetch":
        return fetch(args.clip, args.out)
    stem = Path(args.clip).with_suffix("")
    if args.command == "overview":
        _, duration, _, _ = info(args.clip)
        outputs = sheet(args.clip, args.out or f"{stem}_overview", 0.0, duration, 2, 6, 5, 400)
    else:
        source_fps = info(args.clip)[0]
        fps = source_fps if args.fps == "native" else float(args.fps)
        outputs = sheet(args.clip, args.out or f"{stem}_{args.start:.1f}", args.start, args.end, fps, args.cols, args.rows, args.tile,
                        args.cross)
    for output in outputs:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
