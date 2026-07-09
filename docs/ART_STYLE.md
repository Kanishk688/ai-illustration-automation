# Illustration Style Guide

> A generalised version of the production "style bible" used to keep an entire
> illustrated science reader visually consistent, premium and print-ready.
> Client names, book-specific characters and internal review notes have been
> removed — what remains is the reusable craft and process.

**Read this fully before generating or editing any illustration.** These rules
were tuned over many review rounds; treat them as locked unless a specific image
overrides them.

---

## 0. What / how

- **Project type:** AI-generated **spot illustrations** for a primary-school
  science textbook (roughly ages 8–11).
- **Goal:** world-class, premium, publish-ready educational illustrations —
  rich, scientific, engaging, with pro-creator-level colour. Visual learning
  first, at production speed — where speed comes from doing each image *right*
  the first time, never from lazy shortcuts.
- **Generator:** Magnific MCP — a single explicit model (never `mode=auto`).
  Targeted edits/inpaint via a reference-guided edit model.
- **Output use:** each image is **cut out** and placed into chapter pages beside
  text. Cut-ability is a hard constraint on every image (see §4).

## 0b. The golden rule — per-image critical thinking

**Never throw one generic prompt skeleton at a whole batch.** Each illustration
gets its own deliberate pass:
- What single scientific idea must this image teach? Compose around it.
- Is it a **spot / element / set / diagram** (floats on white, gets cut out) or
  a **full scene** (immersive setting)? This decides edges + ratio (§4, §9).
- What is the best composition, focal point and **deliberately-designed vivid
  colour story**?
- Does it need a **character**? Use a reference and pick with intent (§6).
- What **quality level** does this complexity deserve (§12)?

Lazy / generic / faded / weak "easy-AI" output is unacceptable. The bar is
world-class every single time.

## 1. The locked art style

**Whimsical semi-dimensional editorial illustration — between flat 2D and full 3D.**
- Hand-illustrated, **painterly**, soft brush texture, gentle believable
  **volume**, beautiful internal lighting, rich layered colour.
- **Never:** photoreal, glossy 3D render, plastic-shiny, Pixar-3D, clay, CGI,
  marketing/poster look, Studio-Ghibli, anime.
- **No outlines, no line art, no dark contour strokes.** Every shape, edge and
  fold is defined purely by soft transitions of colour and tonal shading.
- Painterly texture is welcome but must not make colours look muddy or washed-out.

## 2. Colour rules

- Rich, dense, deeply saturated, **bright, premium, luminous** colour — a
  deliberately designed palette, not the model's default.
- **Strong pigment, not diluted watercolour.** Rich gouache / oil-illustration
  density with punchy contrast and believable volume. Ban the weak, pale,
  washed-out look.
- Favoured family on free choice: **coral, turquoise, sunny-yellow, fresh-green,
  warm-peach, royal-blue accents.**
- **Forbidden:** dull, muddy, dirty, faded, grey, desaturated colour, or dark
  muddy backgrounds — darkness prints dirty on textbook paper.
- **Watch the model's lazy fallback:** many image models collapse a short or
  under-defined prompt into a warm **sepia / golden / "Ghibli-watercolour"** haze
  with flat, low-contrast light. Defeat it by *fully* defining the scene: an
  explicit bright, cool-balanced palette named colour-by-colour, plus an explicit
  "NOT Studio-Ghibli, no warm amber/sepia wash".
- Skin (when people are present): **natural warm tone, never turmeric-yellow.**
- **Bright & punchy, never deep/dark:** strong and dense but highly vivid — not
  moody, navy or "pencil-colour". It must print bright on school-book paper.
- **Completeness:** show the whole concept — never cropped or simplified. When a
  figure is present, show it complete with **both hands/arms visible**.

## 3. Light / depth / shadow

- Bright, even lighting. Depth comes only from soft colour shading + crisp
  highlights.
- **No cast shadows, no drop shadows, no grounding shadows** — they break the
  cut-out (§4).

## 4. Background & edges — the SPOT vs SCENE split (critical for cut-out)

**Default background = pure clean solid bright white.** No texture, gradient,
blob, faint motif, shadow, frame or panel. Pure white = one-click cut.

**A) Spot / element / set / diagram / icon** (the majority — floats on white):
- **Clean-edged, fully-opaque shapes.** Every edge meeting white is crisp and
  opaque.
- **No glow, no halo, no soft translucent fade, no gradient bleeding into the
  white.** These leave a semi-transparent zone that defeats the eraser.
- A sun/moon is a **defined disc with a crisp outer edge** — glow lives inside
  the opaque silhouette, never as a halo on the white.

**B) Full scene** (chapter opener, immersive setting):
- Painted as a **soft organic vignette** that gently feathers into the
  surrounding white — no hard rectangular crop border, no frame.
- Even here, don't let the meeting edge become a hazy translucent blend; the
  silhouette is organic but the art stays readable/opaque.

If "emptiness" is a problem, **fill it by making the subject fuller/larger**, not
by adding background.

## 5. Text / labels — none in the image; the designer adds it

- **Put no labelling / diagram / callout text in the image.** The designer
  typesets every label, number, caption and callout later. This avoids
  AI-garbled text and misspellings.
- In every prompt: *"NO TEXT of any kind: no words, letters, numbers, labels or
  captions anywhere."* Leave clean space where labels will go.
- Keep speech bubbles / cards **blank**.
- Exception: a short, deliberately designed bit of text on a badge/card motif is
  fine **only when explicitly asked** — minimal and correctly spelled.

## 6. Characters (consistency without a trained model)

- For **named recurring kids**, lock their design in writing (hair colour and
  style, skin tone, eyes, outfit down to the shoes) and feed a **reference
  sheet** as an `image` reference on every brief that names them. Describe the
  locked traits in the prompt every time.
- For **unnamed / random children**, pull from a **folder of character reference
  images** and attach a fitting one as a reference — never let the model invent a
  generic default face.
- **Choose the reference deliberately** — look at candidates and pick the best
  fit for this scene's role/age/mood. Don't recycle the same 3–4 refs across a
  chapter.
- **Strict variety:** never reuse the same kid across multiple spots in a
  chapter — each gets its own distinct, freshly chosen reference (different face,
  skin tone, hair, build, clothing).
- Keep skin **clean and natural, never turmeric/jaggery-yellow**, never a
  Ghibli/anime cast. **Transform the reference** to fit; make each kid a distinct
  individual.
- **Never crop the character** — full figure comfortably inside the frame.

## 7. Child-safety / age-appropriate

- Grade-appropriate, friendly, never scary. No gore. Keep any "symptom /
  condition" gentle and non-scary.
- Younger grades must stay simple: no complex medical/anatomical diagrams, no
  text overload.

## 8. Reviewer patterns (learned over review rounds)

- **"Which food helps" / deficiency spots: do not show the disease or body
  part.** Show only the foods, clean.
- Show food in a **lunch box / tiffin** when the text says so — not a plate.
- Small containers for small things (e.g. salt in a small transparent bottle).
- Keep compositions **compact, not wide-stretched**; no seam/fold lines.
- Remove any callout/text box and any element the reviewer flags; shrink or
  resize elements that dominate the composition.

## 9. Formats / ratios — supply elements, not layouts

**The job = clean cut-out elements / spot icons / scenes on white.** **Do not
produce composed banners or full-page layouts** (mind maps, summary posters,
banner strips) — the **designer** assembles those from the elements supplied. If
a brief calls for a banner/mind-map, deliver the **individual elements** as
separate clean spots on white.

**Aspect-ratio conventions (decide per image):**
- single icon / sun / moon / round object → **1:1**
- single spot / scene / one diagram → **3:2** (busier diagram → **4:3**)
- a set laid in a row/grid → wide **2:1**
- full immersive scene → **3:2**
- portrait spot needing a caption block below → **3:4**
- for very wide use **21:9** or **2:1** (some models reject `3:1`).

## 10. What "good" looks like (the bar)

Premium, rich, vibrant, clean, highly stylised, world-class, scientific,
engaging, age-appropriate, instantly cut-friendly. **Never:** faded, generic,
weak, lazy, childish-scribbly, cinematic/blurred, low-contrast, photoreal, CGI,
poster/advert, cluttered, empty.

## 11. Prompt skeleton (proven structure — reuse, but think per-image)

```
A WORLD-CLASS, premium [SPOT ILLUSTRATION / DIAGRAM / SCENE / SET OF N ELEMENTS / ICON]
for a grade-3 children's science textbook — [the one idea it teaches].
[fitting adjectives] — NOT generic, weak, flat, plain, lazy, muddy.
NOT a poster, NOT CGI, NOT photoreal, NOT a glossy 3D render, NOT cinematic, no blur.
NOT Studio-Ghibli, NOT anime[, NOT Pixar — when kids present].

ART STYLE: whimsical semi-dimensional editorial illustration between flat 2D and full 3D —
hand-illustrated, painterly, soft brush texture, gentle VOLUME, beautiful internal lighting,
rich layered colour. No outlines/line-art/contour strokes. DEEPLY SATURATED, vivid, luminous
PREMIUM colour; never muddy/faded/pale/dull. [Skin natural warm tone — when people.]
NO cast/drop shadows.

SUBJECT: [scientifically accurate, detailed; fill the frame; leave space for designer's labels].

NO TEXT of any kind: no words, letters, numbers, labels or captions anywhere.

BACKGROUND / EDGES: [SPOT → pure clean bright-WHITE; clean-edged, fully-opaque shapes,
NO glow/halo/gradient fading into the white, cuts cleanly with the eraser.]
[SCENE → soft organic vignette feathering into white, no rectangular crop/frame, avoid glow halos.]

FINAL: world-class, premium, painterly, richly saturated — never flat/plain/lazy/
weak/generic/muddy/poster/CGI. [ratio] orientation.
```

## 12. Generation workflow notes

- **Use one explicit model, always** — never `auto` (auto tends to give faded
  colour, outlines and drop shadows).
- **Generate at 1k, always.** High-res at generation wastes credits. **Upscaling
  is a separate, final, batched step** done once after all images are approved.
- **Quality lever = medium ↔ high** (at 1k): simple single spot → medium; complex
  hero scene / multi-element diagram → high.
- **Credit discipline: one output per slot.** Put the effort into one strong
  prompt; only reroll a slot if its single output has a real error.
- **Edits:** for a targeted fix, prefer an edit/inpaint on just that region so
  the rest stays intact, rather than a full regenerate.
- **Work batch-by-batch;** after each batch, pause and show results for approval.
- **Versioning:** on a tweak, regenerate/edit only that image and save as a new
  versioned file — **never overwrite or delete the original.**
- **Local reference images:** upload → HTTP PUT the bytes → finalize → pass the
  returned identifier in the generate call's `references` as
  `{type: "image", identifier}`.

## 13. Finalisation — upscale + automated transparent cut-out

The post-approval pipeline that turns approved 1k images into print-ready assets.
Runs once, at the end, per chapter. **Never overwrite originals.**

**13a. Upscale** every approved image (4×), then set **300 DPI** losslessly.
When upscaling in parallel, map `output[i] → source[i] → filename[i]` **by
position** — don't match by the new ids.

**13b. Transparent cut-out** (automates the manual eraser), for spot/element/set/
diagram images on clean white (§4-A). Done in Python (Pillow + `scipy.ndimage`):
- **Step 1 — outer area:** remove the white background connected to the border.
- **Step 2 — enclosed pockets only:** also remove the *big* white areas trapped
  between body parts (between legs, fingers, hair gaps) — but **not** the tiny
  white speckles inside bodies (fur/feather highlights), or you punch "pores".

Recipe (`min(R,G,B)` = whiteness):
1. `white = min(R,G,B) >= 243`.
2. `scipy.ndimage.label(white, 8-connectivity)`; components touching the border →
   outer background → remove (Step 1).
3. Enclosed components: remove only those with **area ≥ ~400 px**; keep smaller
   ones (body speckles → no pores) (Step 2).
4. Alpha = opaque except removed; `binary_erosion(2 px)` to eat the white fringe,
   a light `gaussian_filter` for clean anti-aliased edges. Save PNG at 300 DPI.
5. **Verify** on magenta and dark-grey backgrounds; zoom fur/feathers (no pores)
   and subject-whites (intact). Tune the pocket threshold up if pores appear,
   down if finger/leaf gaps stay white.

This works because §4 forces a **pure flat-white background with clean opaque
edges** — exactly what lets the 243 threshold separate background from shaded
subject-whites. Glow/soft-fade edges (banned in §4-A) would defeat it.

**13c. Scenes (§4-B) are not cut out** — no white background to key. Leave them
whole (upscaled + 300 DPI) or give the soft feathered vignette. Never
subject-cut a scene (it drops the environment).

See [`WORKFLOW.md`](WORKFLOW.md) for how this fits the feedback → edit → finish loop.
