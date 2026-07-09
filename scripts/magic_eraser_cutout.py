#!/usr/bin/env python3
"""'Magic-eraser' cutout for flat illustrations: make the background
transparent while preserving fine detail on the subject.

Algorithm (tuned for clean line-art / storybook spot art):
  1. Mark near-white pixels (min channel >= THRESHOLD) as candidate background.
  2. Label connected white regions.
  3. Remove (make transparent) any white region that either touches the image
     border (the outer background) OR is a large enclosed pocket
     (area >= MIN_POCKET).
  4. KEEP tiny enclosed white specks (eye glints, highlights, texture) so the
     subject doesn't end up full of 'pores'.

Requires: pillow, numpy, scipy

Usage:
    python magic_eraser_cutout.py in.png out.png [--threshold 243] [--min-pocket 400]
"""
import argparse

import numpy as np
from PIL import Image
from scipy import ndimage


def cutout(src, dst, threshold, min_pocket):
    im = Image.open(src).convert("RGBA")
    arr = np.array(im)
    white = arr[:, :, :3].min(axis=2) >= threshold      # candidate background

    labels, n = ndimage.label(white)
    if n == 0:
        im.save(dst)
        print("No background detected; saved unchanged.")
        return

    # labels appearing on any border = the outer background
    border = (set(labels[0, :]) | set(labels[-1, :]) |
              set(labels[:, 0]) | set(labels[:, -1]))
    border.discard(0)

    sizes = ndimage.sum(np.ones_like(labels), labels, index=range(1, n + 1))

    remove = np.zeros_like(white)
    for lab in range(1, n + 1):
        if lab in border or sizes[lab - 1] >= min_pocket:
            remove |= (labels == lab)

    arr[:, :, 3][remove] = 0
    Image.fromarray(arr).save(dst)

    kept = int((white & ~remove).sum())
    print(f"{dst}: background + large pockets removed, kept {kept} speckle px")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--threshold", type=int, default=243)
    ap.add_argument("--min-pocket", type=int, default=400)
    a = ap.parse_args()
    cutout(a.src, a.dst, a.threshold, a.min_pocket)
