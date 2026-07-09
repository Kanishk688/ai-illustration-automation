#!/usr/bin/env python3
"""Flatten a transparent (RGBA) PNG onto a solid background (white by default).

Illustration tools often deliver PNGs whose background is transparent; a naive
RGB conversion turns those areas BLACK. This composites them onto white (or any
colour) and can optionally snap near-white pixels to pure #FFFFFF for clean
print output.

Usage:
    python transparent_to_white.py in.png out.png [--bg 255,255,255] [--clean]
"""
import argparse

from PIL import Image


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--bg", default="255,255,255", help="background R,G,B")
    ap.add_argument("--clean", action="store_true",
                    help="snap near-white (>=248) pixels to pure white")
    a = ap.parse_args()

    bg = tuple(int(x) for x in a.bg.split(","))
    im = Image.open(a.src).convert("RGBA")
    flat = Image.new("RGB", im.size, bg)
    flat.paste(im, mask=im.split()[-1])

    if a.clean:
        import numpy as np
        arr = np.array(flat)
        m = ((arr[:, :, 0] >= 248) & (arr[:, :, 1] >= 248) & (arr[:, :, 2] >= 248))
        arr[m] = [255, 255, 255]
        flat = Image.fromarray(arr)

    flat.save(a.dst)
    print(f"Flattened {a.src} onto {bg} -> {a.dst}")


if __name__ == "__main__":
    main()
