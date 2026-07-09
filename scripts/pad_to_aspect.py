#!/usr/bin/env python3
"""Pad an image to a target aspect ratio, then crop the padding back off.

Some generative edit models only accept a fixed set of aspect ratios. To edit a
2:1 banner on a model that supports 21:9 but not 2:1: pad 2:1 -> 21:9, run the
edit, then crop the same fraction back to recover the original framing (instead
of letting the model re-crop your composition).

Usage:
    pad:   python pad_to_aspect.py pad  in.png padded.png --ratio 21:9 [--fill 255,255,255]
    crop:  python pad_to_aspect.py crop edited.png out.png --pad-frac 0.0714 [--axis width]
"""
import argparse

from PIL import Image


def pad(src, dst, ratio, fill):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    rw, rh = (int(x) for x in ratio.split(":"))
    target = rw / rh
    cur = w / h

    if target > cur:                       # need wider -> add width
        new_w, new_h = round(h * target), h
        px, py, axis = (new_w - w) // 2, 0, "width"
    else:                                  # need taller -> add height
        new_w, new_h = w, round(w / target)
        px, py, axis = 0, (new_h - h) // 2, "height"

    canvas = Image.new("RGB", (new_w, new_h),
                       tuple(int(x) for x in fill.split(",")))
    canvas.paste(im, (px, py))
    canvas.save(dst, quality=95)
    frac = (px / new_w) if axis == "width" else (py / new_h)
    print(f"Padded to {new_w}x{new_h} ({ratio}).")
    print(f"After editing, crop back with:  --pad-frac {frac:.4f} --axis {axis}")


def crop(src, dst, frac, axis):
    im = Image.open(src)
    w, h = im.size
    if axis == "width":
        cut = round(w * frac)
        out = im.crop((cut, 0, w - cut, h))
    else:
        cut = round(h * frac)
        out = im.crop((0, cut, w, h - cut))
    out.save(dst)
    print(f"Cropped {frac} off each {axis} -> {out.size}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("pad")
    p.add_argument("src")
    p.add_argument("dst")
    p.add_argument("--ratio", required=True, help="e.g. 21:9")
    p.add_argument("--fill", default="255,255,255")

    c = sub.add_parser("crop")
    c.add_argument("src")
    c.add_argument("dst")
    c.add_argument("--pad-frac", type=float, required=True)
    c.add_argument("--axis", choices=["width", "height"], default="width")

    a = ap.parse_args()
    if a.cmd == "pad":
        pad(a.src, a.dst, a.ratio, a.fill)
    else:
        crop(a.src, a.dst, a.pad_frac, a.axis)
