# AI Illustration Automation Pipeline

A practical, AI-assisted workflow for producing and **revising illustrated
textbook artwork at scale** — turning reviewer feedback into finished,
print-ready assets with minimal manual pixel-pushing.

Built and used in production to illustrate primary-school Science & English
readers (100s of illustrations across multiple grades). This repo contains the
**reusable automation** — the helper scripts and the documented process — with
**no client artwork included** (all image assets are intentionally git-ignored).

> Portfolio: **https://kannisshk.pages.dev**

---

## What this automates

Illustrating a book is 20% drawing and 80% *iteration*: an auditor leaves
comments ("make the plant smaller", "remove the text box", "no lab coat"), and
every note has to be applied cleanly while keeping the character, style and
resolution intact. This pipeline makes that loop fast and repeatable.

```
   ┌────────────────────────────────────────────────────────────┐
   │  1. FETCH FEEDBACK   Google Drive comments (auditor notes)  │
   │  2. PREP SOURCE      flatten transparency, fix aspect ratio  │
   │  3. AI EDIT          reference-guided edit (Nano Banana Pro / │
   │                      GPT image) — apply only the notes        │
   │  4. VERIFY           side-by-side face/detail check           │
   │  5. FINISH           4× upscale → set 300 DPI → deliver       │
   └────────────────────────────────────────────────────────────┘
```

Steps 1, 3 and 5 are driven through **Claude Code** with the **Magnific** and
**Google Drive** MCP servers; steps 2 and the finishing touches use the small,
dependency-light Python scripts in [`scripts/`](scripts/).

See [`docs/WORKFLOW.md`](docs/WORKFLOW.md) for the full end-to-end process, and
[`docs/ART_STYLE.md`](docs/ART_STYLE.md) for the illustration style guide that
keeps a whole book visually consistent (art style, colour, cut-out edges,
prompt skeleton).

---

## Scripts

| Script | What it does |
|---|---|
| [`scripts/contact_sheet.py`](scripts/contact_sheet.py) | Build a labelled thumbnail grid to review many variants at once |
| [`scripts/transparent_to_white.py`](scripts/transparent_to_white.py) | Flatten transparent PNGs onto white (avoids the classic "transparent → black" bug) |
| [`scripts/pad_to_aspect.py`](scripts/pad_to_aspect.py) | Pad to a supported aspect ratio for editing, then crop back (e.g. 2:1 ↔ 21:9) |
| [`scripts/set_dpi.py`](scripts/set_dpi.py) | Set print DPI (300) and optionally resize to exact pixel dimensions |
| [`scripts/optimize_webp.py`](scripts/optimize_webp.py) | Batch resize + WebP encode for a fast static portfolio site |
| [`scripts/magic_eraser_cutout.py`](scripts/magic_eraser_cutout.py) | Make backgrounds transparent while keeping fine subject detail |

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Review a folder of variants
python scripts/contact_sheet.py ./my_variants --cols 4

# Fix a transparent PNG that would otherwise go black on RGB export
python scripts/transparent_to_white.py in.png out.png --clean

# Finish an approved asset for print
python scripts/set_dpi.py approved.png final.png --dpi 300 --width 6144 --height 3072
```

## Tech / tooling

- **Python** (Pillow, NumPy, SciPy) for the deterministic image ops
- **Claude Code** as the orchestrator
- **Magnific MCP** — reference-guided AI image edit + upscale (Nano Banana Pro, GPT image models)
- **Google Drive MCP** — pulling reviewer comments straight from the review file

## Notes on assets & IP

No client artwork lives in this repository — the `.gitignore` blocks all image
formats by design. The illustrations themselves belong to the publisher; this
repo is only the **automation and process**.

## License

Code released under the [MIT License](LICENSE).
