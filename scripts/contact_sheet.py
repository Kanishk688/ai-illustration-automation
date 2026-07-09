#!/usr/bin/env python3
"""Build a labelled thumbnail grid (contact sheet) from a folder of images.

Handy for reviewing many illustration variants at a glance.

Usage:
    python contact_sheet.py <folder> [--out sheet.jpg] [--cols 4] [--thumb 340]
"""
import argparse
import glob
import os

from PIL import Image, ImageDraw

EXTS = (".png", ".jpg", ".jpeg", ".webp")


def build(folder, out, cols, thumb, pad=26, label_h=34):
    files = sorted(f for f in glob.glob(os.path.join(folder, "*"))
                   if f.lower().endswith(EXTS))
    if not files:
        raise SystemExit(f"No images found in {folder}")

    rows = (len(files) + cols - 1) // cols
    W = cols * thumb + (cols + 1) * pad
    H = rows * (thumb + label_h) + pad
    sheet = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(sheet)

    for i, fp in enumerate(files):
        im = Image.open(fp).convert("RGB")
        im.thumbnail((thumb, thumb))
        r, c = divmod(i, cols)
        x = pad + c * (thumb + pad)
        y = pad + r * (thumb + label_h)
        sheet.paste(im, (x, y + 22))
        draw.text((x, y + 4), os.path.basename(fp), fill="black")

    sheet.save(out, quality=88)
    print(f"Saved {out}  ({len(files)} images, {sheet.size[0]}x{sheet.size[1]})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("folder")
    ap.add_argument("--out", default="contact_sheet.jpg")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--thumb", type=int, default=340)
    a = ap.parse_args()
    build(a.folder, a.out, a.cols, a.thumb)
