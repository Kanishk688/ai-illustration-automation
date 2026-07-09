#!/usr/bin/env python3
"""Set print DPI metadata (default 300) on an image, optionally resizing to
exact pixel dimensions.

Pixels are unchanged unless --width/--height are given; only the DPI metadata is
written (which controls the physical print size).

Usage:
    python set_dpi.py in.png out.png [--dpi 300] [--width 6144 --height 3072]
"""
import argparse

from PIL import Image


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--width", type=int)
    ap.add_argument("--height", type=int)
    a = ap.parse_args()

    im = Image.open(a.src)
    if a.width and a.height:
        im = im.resize((a.width, a.height), Image.LANCZOS)
    im.save(a.dst, dpi=(a.dpi, a.dpi))

    w, h = im.size
    print(f"{a.dst}: {w}x{h} @ {a.dpi} dpi "
          f"-> {w / a.dpi:.2f}in x {h / a.dpi:.2f}in")


if __name__ == "__main__":
    main()
