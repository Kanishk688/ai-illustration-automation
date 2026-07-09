#!/usr/bin/env python3
"""Batch-optimise images to web-friendly WebP: resize the longest edge and
re-encode. Used to prep gallery images for a fast static portfolio site.

Usage:
    python optimize_webp.py <in_dir> <out_dir> [--max 1600] [--quality 82]
"""
import argparse
import glob
import os

from PIL import Image

EXTS = (".png", ".jpg", ".jpeg", ".webp")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("in_dir")
    ap.add_argument("out_dir")
    ap.add_argument("--max", type=int, default=1600, help="longest edge in px")
    ap.add_argument("--quality", type=int, default=82)
    a = ap.parse_args()

    os.makedirs(a.out_dir, exist_ok=True)
    files = [f for f in glob.glob(os.path.join(a.in_dir, "*"))
             if f.lower().endswith(EXTS)]

    for fp in files:
        im = Image.open(fp).convert("RGB")
        im.thumbnail((a.max, a.max), Image.LANCZOS)
        name = os.path.splitext(os.path.basename(fp))[0] + ".webp"
        out = os.path.join(a.out_dir, name)
        im.save(out, "WEBP", quality=a.quality, method=6)
        print(f"{fp} -> {out}  ({im.size[0]}x{im.size[1]})")

    print(f"Done: {len(files)} images")


if __name__ == "__main__":
    main()
