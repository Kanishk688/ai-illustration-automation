# End-to-end workflow

The pipeline for taking one illustration from **reviewer feedback** to a
**finished, print-ready asset**.

## 1. Fetch feedback (Google Drive MCP)

Reviewers leave comments on the delivered PNG in a shared Drive folder. Instead
of copying notes by hand, the comments are read straight from the file:

- `read_file_content(fileId, includeComments=true)` returns each open comment
  (e.g. *"Remove the call out."*, *"Make the plant smaller"*).
- File metadata gives the source name and the chapter folder it lives in.

## 2. Prepare the source

Two gotchas that silently ruin an edit if skipped:

- **Transparency → black.** Many delivered PNGs are RGBA with a *transparent*
  background. Converting to RGB naively fills it **black**. Always flatten onto
  white first — `scripts/transparent_to_white.py`. Check the alpha channel
  before anything else.
- **Unsupported aspect ratio.** Some edit models only accept a fixed set of
  ratios. For a 2:1 banner, pad to 21:9 (`scripts/pad_to_aspect.py pad`), run
  the edit, then crop the padding back off (`... crop`). This preserves the
  exact framing instead of letting the model re-crop the composition.

## 3. AI edit (Magnific MCP)

Reference-guided editing — the original image is passed as a reference so the
model changes **only** what the note asks and keeps everything else:

- **Nano Banana Pro** (`imagen-nano-banana-2`) — best fidelity for keeping
  faces, characters and brand marks identical across an edit.
- **GPT image** (`gpt-2`, quality `low`/`medium`/`high`, `1k`/`2k`/`4k`) —
  strong for text/layout-heavy panels.

Prompting rules that matter:
- State the **one or two changes** explicitly, then a hard "keep everything
  else 100% identical" clause naming the characters and elements to preserve.
- If a real logo/wordmark must survive untouched, feed it as its own reference
  and instruct the model to reproduce it exactly — never let the model invent a
  logo.

## 4. Verify

Regeneration can drift. Crop the faces/critical details from the original and
the edit into a side-by-side strip and eyeball them before shipping. A
`contact_sheet.py` montage works well for batch review.

## 5. Finish

- **Upscale 4×** (Magnific enhance, *precision* mode to stay faithful).
- **Set 300 DPI** and the exact target pixel size — `scripts/set_dpi.py`.
- Deliver back to the review folder. Keep the original untouched; version the
  corrected file (`* - CORRECTED.png`) rather than overwriting.

## Conventions

- Never overwrite an original — always write a new versioned file.
- Soft, feathered edges should feather into **white**, not a hard crop.
- No baked-in body text/labels — leave space for the designer's typesetting.
