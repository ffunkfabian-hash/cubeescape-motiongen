#!/usr/bin/env python3
"""Measures reference footage frame by frame (docs/destiny2.md › 2; Cube Escape Docs/FIRST_PERSON_EQUIPMENT.md › 1).

The reference for the first-person feel is Destiny 2; its timings (ADS blend, sprint pose, recoil return, reload events, bow
draw …) are read off 60-fps Twitch clips: contact sheets with a burned-in timestamp, sighted picture by picture. This tool is the
whole way, so a session can repeat or extend the measurement without rediscovering it:

    python3 tools/reference_frames.py list <channel> [--top 100]           # the channel's most viewed clips: id|url|title|s|views
    python3 tools/reference_frames.py fetch <clip url|slug> [--out DIR]    # download (yt-dlp, 60-fps video up to 1080p), print fps
    python3 tools/reference_frames.py overview <clip.mp4> [--out PREFIX]   # 2 pictures/s, 6 × 5 per sheet = 15 s - find the moments
    python3 tools/reference_frames.py sheet <clip.mp4> START END [--fps 10|native] [--out PREFIX] [--cols 6 --rows 5 --tile 480]
                                                                           # 10/s to narrow down, 60/s (native) to measure;
                                                                           # --cross marks the screen centre (where the game aims)

    python3 tools/reference_frames.py measure <clip.mp4> START END --fps native --cross
        [--measurement TEXT --clip-url URL --source 'channel, date'] [--out /tmp/times.txt]
        [--sheet-out /tmp/sheet]   # native frame list, text file, sheets and a clips.json draft; outputs outside this repo

Reading a measurement: the label on each tile is the clip time in h:mm:ss.fff; at the clip's native rate one tile is one picture, so
a span in pictures is the difference of the labels divided by the frame time (16.7 ms at 60/s). Accuracy is ±1 picture at the
native rate and ±0.05 s on a 10/s sheet. Write the result into the table of › 1.2a with the clip (channel, slug, date), the
timestamps and what was seen; the numbers of one clip are an example of one weapon with unknown stats, never a type's mean.

Cloud sessions: YouTube is blocked (bot check); Twitch clips load. Nothing here touches the repository - clips and sheets belong in
the session's scratch folder (--out). Needs yt-dlp and ffmpeg/ffprobe on PATH. Without the drawtext filter (ffmpeg built without
freetype, e.g. Homebrew's default formula) the sheets are labelled with ImageMagick (`magick` or `montage`) instead.
"""
from __future__ import annotations

import argparse
import functools
import json
import re
import math
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FONT_CANDIDATES = ("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",       # Linux / cloud
                   "/System/Library/Fonts/Supplemental/Courier New Bold.ttf",       # macOS
                   "/System/Library/Fonts/Menlo.ttc")
TWITCH_CLIP_PREFIX = "https://clips.twitch.tv/"
# Twitch clips are single progressive streams; YouTube offers 60-fps video only as separate video streams (no combined
# stream above 360p), so `best[height<=1080]` fails there. Prefer 60-fps H.264 video, then any video up to 1080p, then
# whatever is best; audio is not needed for measuring.
FETCH_FORMAT = ("bv*[height<=1080][fps>=59][vcodec^=avc1]/bv*[height<=1080][fps>=59]/bv*[height<=1080]/best[height<=1080]/best")
REPO_ROOT = Path(__file__).resolve().parents[1]


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


def frame_records(path: str, start: float, end: float) -> list[tuple[int, float]]:
    """Return source frame indexes and presentation times in [start, end)."""
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_frames",
                                   "-show_entries", "frame=best_effort_timestamp_time", "-of", "json", path])
    result = []
    for index, frame in enumerate(json.loads(out).get("frames", [])):
        value = frame.get("best_effort_timestamp_time")
        if value not in (None, "") and start <= float(value) < end:
            result.append((index, float(value)))
    return result


def scratch_path(path: str) -> Path:
    """Resolve an output path and refuse the repository, including symlink aliases."""
    target = Path(path).expanduser().resolve()
    if target == REPO_ROOT or REPO_ROOT in target.parents:
        raise ValueError(f"Ausgabepfad liegt im Repository: {target}")
    return target


def measure(clip: str, start: float, end: float, fps: str, cross: bool, output: str | None,
            measurement: str, clip_url: str, source: str, sheet_out: str | None = None,
            cols: int = 6, rows: int = 5, tile: int = 480) -> int:
    if not math.isfinite(start) or not math.isfinite(end) or start < 0 or end <= start:
        raise ValueError("Ungültiges Intervall: T0 muss >= 0 und T1 größer als T0 sein.")
    text_target = scratch_path(output or str(Path(tempfile.gettempdir()) / f"{Path(clip).stem}_measurements.txt"))
    prefix = scratch_path(sheet_out or str(Path(tempfile.gettempdir()) / f"{Path(clip).stem}_measure"))
    _, duration, _, _ = info(clip)
    if end > duration:
        raise ValueError(f"Intervall endet bei {end:g} s, Clipdauer ist {duration:g} s.")
    if fps != "native":
        raise ValueError("measure unterstützt derzeit nur --fps native.")
    if cols <= 0 or rows <= 0 or tile <= 0:
        raise ValueError("cols, rows und tile müssen positive Ganzzahlen sein.")
    records = frame_records(clip, start, end)
    times = [timestamp for _, timestamp in records]
    if not records:
        raise ValueError("Im angegebenen Intervall wurden keine Bildzeiten gefunden.")
    sheet_paths = [scratch_path(f"{prefix}_{index:02d}.jpg") for index in range(math.ceil(len(records) / (cols * rows)))]
    print("Bildzeiten (Bildnummer, Sekunde):")
    for index, timestamp in enumerate(times, 1):
        print(f"{index}, {timestamp:.6f}")
    # Select the original decoded frames by source index; this preserves one tile per
    # listed native PTS, including fractional rates and intervals off the nominal frame grid.
    prefix.parent.mkdir(parents=True, exist_ok=True)
    outputs = []
    for index in range(0, len(times), cols * rows):
        page = index // (cols * rows)
        page_records = records[index:index + cols * rows]
        selection = "+".join(f"eq(n\\,{frame_index})" for frame_index, _ in page_records)
        render_sheet(["-copyts", "-i", clip, "-map", "0:v:0"], None, f"select='{selection}',", tile, cols, rows, cross,
                     str(sheet_paths[page]))
        outputs.append(str(sheet_paths[page]))
    suggestion = {"measurement": measurement, "clip": clip_url, "source": source,
                  "timestamps": ", ".join(f"{t:.6f} s" for t in times)}
    print("Entwurf für data/clips.json (keine Metadaten ergänzt):")
    print(json.dumps(suggestion, ensure_ascii=False, indent=2))
    text_target.parent.mkdir(parents=True, exist_ok=True)
    text_target.write_text("Bildnummer, Sekunde\n" + "".join(f"{i}, {t:.6f}\n" for i, t in enumerate(times, 1)), encoding="utf-8")
    print(f"Zeitstempeldatei: {text_target}")
    for output_sheet in outputs:
        print(f"Kontaktbogen: {output_sheet}")
    return 0


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


def font_file() -> str | None:
    """The first monospace font that exists on this machine, or None (drawtext then falls back to fontconfig)."""
    return next((path for path in FONT_CANDIDATES if Path(path).is_file()), None)


@functools.lru_cache(maxsize=1)
def drawtext_available() -> bool:
    """True when the ffmpeg on PATH has the drawtext filter (it needs freetype, which some builds leave out)."""
    try:
        filters = subprocess.run(["ffmpeg", "-hide_banner", "-filters"], capture_output=True, text=True, check=False).stdout
    except OSError:
        return False
    return re.search(r"\sdrawtext\s", filters) is not None


def filter_graph(fps: float | None, tile_width: int, cols: int, rows: int, cross: bool, labelled: bool = True) -> str:
    """Build a sheet filter; fps=None keeps selected source frames without resampling. labelled=False leaves out the burned-in
    time and the tiling (the ImageMagick fallback labels and tiles the pictures itself)."""
    centre = ("drawbox=x=iw/2-1:y=0:w=2:h=ih:color=cyan@0.5:t=fill,drawbox=x=0:y=ih/2-1:w=iw:h=2:color=cyan@0.5:t=fill,"
              "drawbox=x=iw/2-ih/40:y=ih/2-ih/40:w=ih/20:h=ih/20:color=cyan@0.8:t=2," if cross else "")
    sampling = f"fps={fps}," if fps is not None else ""
    if not labelled:
        return f"{sampling}{centre}scale={tile_width}:-2"
    font = font_file()
    label = (f"fontfile='{font}':" if font else "") + "text='%{pts\\:hms}':x=6:y=6:fontsize=20:fontcolor=yellow:box=1:boxcolor=black@0.6"
    return f"{sampling}{centre}scale={tile_width}:-2,drawtext={label},tile={cols}x{rows}:padding=2:color=black"


def clock(seconds: float) -> str:
    """The clip time as h:mm:ss.fff, the format of ffmpeg's %{pts:hms} label."""
    hours, rest = divmod(seconds, 3600)
    minutes, secs = divmod(rest, 60)
    return f"{int(hours)}:{int(minutes):02d}:{secs:06.3f}"


def imagemagick() -> list[str]:
    """Command prefixes for annotating and tiling with ImageMagick 7 (`magick`) or 6 (`convert`/`montage`)."""
    if shutil.which("magick"):
        return ["magick"], ["magick", "montage"]
    if shutil.which("convert") and shutil.which("montage"):
        return ["convert"], ["montage"]
    raise OSError("ffmpeg ohne drawtext-Filter und kein ImageMagick gefunden – Kontaktbögen brauchen eins von beiden.")


def render_sheet(input_args: list[str], fps: float | None, select: str, tile_width: int, cols: int, rows: int, cross: bool,
                 output: str) -> None:
    """Write one contact sheet. With drawtext, ffmpeg labels and tiles; without it, ffmpeg writes the pictures (showinfo gives each
    picture's source time) and ImageMagick burns in the same h:mm:ss.fff label and tiles them with the same 2-px gaps."""
    if drawtext_available():
        graph = select + filter_graph(fps, tile_width, cols, rows, cross)
        subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", *input_args, "-vf", graph, "-frames:v", "1", "-q:v", "4", output])
        return
    convert, montage = imagemagick()
    with tempfile.TemporaryDirectory(prefix="sheet_") as scratch:
        graph = select + filter_graph(fps, tile_width, cols, rows, cross, labelled=False) + ",showinfo"
        result = subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "info", *input_args, "-vf", graph,
                                 "-frames:v", str(cols * rows), "-fps_mode", "passthrough", os.path.join(scratch, "p%04d.png")],
                                capture_output=True, text=True, check=True)
        times = [float(value) for value in re.findall(r"pts_time:\s*([0-9.]+)", result.stderr)]
        pictures = sorted(Path(scratch).glob("p*.png"))
        if not pictures or len(pictures) != len(times):
            raise ValueError(f"Kontaktbogen: {len(pictures)} Bilder, aber {len(times)} Zeitstempel.")
        font = font_file()
        labelled = []
        for picture, seconds in zip(pictures, times):
            target = picture.with_name(picture.stem + "_l.png")
            subprocess.check_call([*convert, str(picture), *(["-font", font] if font else []), "-fill", "yellow",
                                   "-undercolor", "#00000099", "-pointsize", "20", "-gravity", "northwest",
                                   "-annotate", "+6+6", clock(seconds), str(target)])
            labelled.append(str(target))
        subprocess.check_call([*montage, *labelled, "-tile", f"{cols}x{rows}", "-geometry", "+1+1", "-background", "black",
                               "-quality", "90", output])


def sheet(path: str, prefix: str, start: float, end: float, fps: float | None, cols: int, rows: int, tile_width: int,
          cross: bool = False) -> list[str]:
    """Contact sheets covering [start, end) at `fps`, cols × rows tiles each, the clip time burned into every tile; `cross` draws
    the screen centre (the aim point of the game) into every picture, so the offset of muzzle, sight and tracer can be read off.
    fps=None preserves source frame indexes and PTS without resampling."""
    _, duration, _, _ = info(path)
    outputs = []
    if fps is None:
        records = frame_records(path, start, min(end, duration))
        for index in range(0, len(records), cols * rows):
            page_records = records[index:index + cols * rows]
            selection = "+".join(f"eq(n\\,{frame_index})" for frame_index, _ in page_records)
            output = f"{prefix}_{index // (cols * rows):02d}.jpg"
            render_sheet(["-copyts", "-i", path, "-map", "0:v:0"], None, f"select='{selection}',", tile_width, cols, rows, cross,
                         output)
            outputs.append(output)
        return outputs
    for index, (t0, t1) in enumerate(windows(start, min(end, duration), fps, cols * rows)):
        output = f"{prefix}_{index:02d}.jpg"
        render_sheet(["-ss", f"{t0:.3f}", "-to", f"{t1:.3f}", "-copyts", "-i", path], fps, "", tile_width, cols, rows, cross, output)
        outputs.append(output)
    return outputs


def yt_dlp_command() -> list[str]:
    """Return a command prefix for yt-dlp, using the installed module as a fallback."""
    executable = shutil.which("yt-dlp")
    return [executable] if executable else [sys.executable, "-m", "yt_dlp"]


def list_clips(channel: str, top: int) -> int:
    url = f"https://www.twitch.tv/{channel}/clips?filter=clips&range=all"
    command = yt_dlp_command() + ["--flat-playlist", "--print", "%(id)s|%(url)s|%(title)s|%(duration)s|%(view_count)s",
                                  "--playlist-end", str(top), url]
    return subprocess.call(command)


def fetch(clip: str, out_dir: str) -> int:
    url = clip if clip.startswith("http") else TWITCH_CLIP_PREFIX + clip
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    template = os.path.join(out_dir, "%(uploader)s_%(id)s.%(ext)s")
    code = subprocess.call(yt_dlp_command() + ["-q", "--no-warnings", "-f", FETCH_FORMAT, "-o", template, url])
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
    measurer = commands.add_parser("measure", help="list frame times and propose a clips.json row")
    measurer.add_argument("clip")
    measurer.add_argument("start", type=float)
    measurer.add_argument("end", type=float)
    measurer.add_argument("--fps", choices=("native",), default="native", help="native source rate (default)")
    measurer.add_argument("--cross", action="store_true", help="mark the screen centre on each contact sheet frame")
    measurer.add_argument("--out", help="text output path (must be outside the repository)")
    measurer.add_argument("--measurement", default="", help="measurement description for the proposed row")
    measurer.add_argument("--clip-url", default="", help="clip URL for the proposed row")
    measurer.add_argument("--source", default="", help="source/channel/date for the proposed row")
    measurer.add_argument("--sheet-out", help="contact sheet prefix (default: system scratch)")
    measurer.add_argument("--cols", type=int, default=6)
    measurer.add_argument("--rows", type=int, default=5)
    measurer.add_argument("--tile", type=int, default=480)
    args = parser.parse_args(argv)

    if args.command == "list":
        return list_clips(args.channel, args.top)
    if args.command == "fetch":
        return fetch(args.clip, args.out)
    if args.command == "measure":
        return measure(args.clip, args.start, args.end, args.fps, args.cross, args.out,
                       args.measurement, args.clip_url, args.source, args.sheet_out, args.cols, args.rows, args.tile)
    stem = Path(args.clip).with_suffix("")
    if args.command == "overview":
        _, duration, _, _ = info(args.clip)
        outputs = sheet(args.clip, args.out or f"{stem}_overview", 0.0, duration, 2, 6, 5, 400)
    else:
        fps = None if args.fps == "native" else float(args.fps)
        outputs = sheet(args.clip, args.out or f"{stem}_{args.start:.1f}", args.start, args.end, fps, args.cols, args.rows, args.tile,
                        args.cross)
    for output in outputs:
        print(output)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except (ValueError, subprocess.CalledProcessError, OSError) as error:
        print(f"FEHLER: {error}", file=sys.stderr)
        sys.exit(2)
