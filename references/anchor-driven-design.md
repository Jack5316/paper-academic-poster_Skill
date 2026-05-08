# Anchor-Driven Adaptive Design Route

Load this reference whenever the poster brief leans on **design quality** rather than evidence-density: explicit signals are 设计感 / 灵魂 / 特色锚点 / soulful poster / "不要模板感" / "像信息图杂志特稿那样" / "海报本身要好看", or any time the user clearly cares more about how the poster *feels* than about preserving every original figure verbatim.

This route is end-to-end automatic: no mid-flow style/density/palette/size questions to the user, and the only deliverables are the poster image plus a 1-2 sentence Chinese design note. It overrides hybrid/deterministic compositing routes when active.

## Hard Constraints (binding for this route)

1. **GPT Image 2 only** for the final poster image. Never silently substitute Nano Banana Pro / Gemini Image / Qwen-Image / Seedream / any non-GPT Image 2 model.
2. **Native large only — absolutely no post-generation enlargement.** No `Image.resize` upscale, no AI super-resolution, no waifu2x, no Real-ESRGAN, no "delivery resize to 4K". If the returned image's long edge is below the floor, regenerate or fall down the chain — never enlarge a small image to fake resolution.
3. **No post-processing of any kind on the rendered poster.** No local text overlay (PIL/Cairo/SVG/Inkscape/Pillow draw), no logo / QR / footer stamping, no figure stitching, no border crop, no compositing layer over the AI image. The poster the model returns is the poster the user receives.
4. **A0 portrait 2:3** is fixed. Request the closest portrait ratio the chosen route supports (2:3 if available, else 3:4 or 9:16 as the model permits).
5. **Native long-edge floor: 2304 px** (the user-validated YouMind sample baseline). Verify with PIL or equivalent after generation; if below floor, regenerate or move down the chain.
6. **Maximum 2 regeneration retries.** If 3 attempts on the same route all fail QC, drop down the chain. If the entire chain is exhausted, surface the boundary and the manual-fix suggestion to the user — do not silently downgrade resolution or switch to hybrid/deterministic compositing.

## Native-Large GPT Image 2 Fallback Chain

Use the highest-confirmed-native-resolution route first. Verify actual pixel dimensions after each attempt; never trust labels rendered inside the image.

1. **Codex / OpenAI Responses direct** — `image_generation` tool with `model: "gpt-image-2"`, `quality: "high"`, and the largest valid native portrait size the route accepts. Prefer `2416x3424` for A-series-ish posters or `2160x3840` for 4K portrait. Pass only classified evidence-class originals as `input_image` reference assets; concept/structure figures become redraw sub-prompts.
2. **YouMind** — `createChat` with `chatModel: "gpt-image-2-2026-04-21"`, `tools.imageGenerate.useTool: "required"`, `tools.imageGenerate.quality: "high"`, and the largest currently supported portrait size. Verify wrapper schema, accepted size, and downloaded pixels on every run. Reference assets via `atReferences` of type `AtReferenceMaterialDto` / `AtReferenceInlineImageDto`, limited to classified evidence-class originals.
3. **ListenHub** — `generate-image.sh "<prompt>" 4K 2:3 "<comma-separated-reference-urls>" gpt-image-2`. Documented `--size 4K` parameter is the largest advertised; reliability has been uneven (occasional 504 / service-busy), so try at least one reduced-complexity retry before declaring it failed.

Routes explicitly excluded from this chain (cannot meet the long-edge floor or violate the GPT Image 2 rule):

- Hermes built-in `image_generate` — fixed small output, no `size` parameter.
- Any non-GPT Image 2 model on any provider.

## Six-Phase Workflow

### Phase 1 — Paper Analysis

**Metadata extraction**: full title; full author list (do not abbreviate unless ≥ 6 authors, then `first author et al.` per the project metadata-compression rule); top-level affiliations; venue / journal / conference name; year; DOI / arXiv id (recorded for the manifest, not rendered on the poster).

**Identifier hygiene** (the venue-ribbon trap — do not skip):

- *Allowed on the poster*: formal journal/conference name, journal logo, ISSN / CN ID, official volume/issue.
- *Forbidden on the poster*: 网络首发 placeholder pagination (e.g. "002", "网络首发页", "待定页码"), preprint watermark bars, "Under review as a conference paper" tags, "For peer review" tags, peer-review line numbers, "DOI placeholder", "To appear in" hedges, arXiv preprint version ribbons, peer-review red marks.
- *Litmus test*: would this identifier still exist on the page after the paper is officially published? If not, drop it.
- If the official year is uncertain, use submission/acceptance year — never the 网络首发 forecast date.

**Academic substance**: abstract verbatim; author-claimed contributions (their words, not your interpretation); method (core algorithm / model / experimental design); key results with exact numbers, metrics, baselines, datasets; conclusion / implications; limitations / future work.

**Three-axis classification** (drives every later decision):

- *Type*: theory / experimental / methodological / survey / position / dataset-or-resource.
- *Length*: short (< 6 pages, workshop / letter) / medium (6–12 pages, conference) / long (12+ pages, journal / thesis).
- *Field*: CS-AI / Bio-Med / Physics-Chem / Math / Humanities / Social Science / Interdisciplinary.

**Distinctive Anchor Identification** (the soul of the poster — without this step the poster is generic):

- Ask: *what is irreplaceable about this paper? What can no one else in the same field claim?*
- Typical anchor forms: a named open-source system architecture; a real UI / dialogue / experiment-scene screenshot; a unique dataset-sample visualization; an original named term diagram; a named-case process figure; an author-coined paradigm diagram (e.g. a four-element framework figure).
- **Identify at least 1–2 anchors.** They must occupy a dedicated section, OR sit at the visual center, OR be the largest figure on the poster.
- Generic words like "Framework / Method / Architecture" must not replace concrete anchor presentation.
- If the anchor is evidence-class (UI screenshot, scene photo, dialog capture), apply Phase 2's evidence-class strategy.

**Hook-style highlight extraction** (3–5 highlights):

- At least 1–2 must point to the anchor with named, story-shaped, specific language (a real system, a real case, a real number).
- Reorganized for an outside reader — *not* a mechanical compression of the abstract.
- One or two sentences each; if a precise number exists in the paper, reuse the exact number.
- Hook quality: not "We propose a new method"; instead "Dispensing with recurrence entirely — architecture based solely on attention".
- Negative example: "本文构建了多智能体协同框架"（空泛）. Positive: "OpenClaw：GPT-4 提问、Claude 反驳、Gemini 裁决——三款大模型在飞书群里的情报辩论"（锚点具体）.

### Phase 2 — Figure Triage

For every figure and table in the paper, decide a strategy:

| Class | Strategy |
|---|---|
| Diagram / framework / pipeline / architecture / concept figure | **Redraw** under unified poster style; preserve every key label, ordering, arrow, grouping |
| Data chart with exact numbers (curves, bars, scatter, ROC, ablations) | **Preserve original** — extract crop, attach as reference/material image to GPT Image 2 |
| Observation data (microscopy, medical imaging, sample photo, qualitative result) | **Preserve original** |
| **Evidence-class visuals** (UI screenshot / dialog capture / experiment-scene photo / chat bubbles / terminal session) | **Prefer preserving original**. If extraction is infeasible, redraw as a high-fidelity **Mockup** that (a) reproduces the platform's visual language correctly (Feishu / WeChat / web / terminal etc.), (b) renders the actual dialog / UI text **verbatim**, (c) carries a "示意图 / Illustrative Mockup" corner badge, (d) matches the poster's overall visual style. Never replace evidence-class visuals with abstract boxes — that erases the paper's distinctiveness. |
| Small comparison table (≤5 rows, ≤4 cols) | **Re-typeset** as visual cards |
| Large benchmark table | **Preserve original** or **omit** |
| Important formula | **Render as text inside the prompt** (GPT Image 2 handles math symbols well) |

For each *preserve* entry: record PDF page + figure number for asset extraction.
For each *redraw* entry: write a detailed redraw sub-prompt covering elements, structure, logical relations, and labels to retain.
For each *Mockup redraw* entry: the sub-prompt must explicitly include (a) the platform's visual language, (b) verbatim UI / dialog text, (c) the mandatory "示意图 / Illustrative Mockup" badge, (d) style-unity constraint with the master poster.

Output a **figure manifest** listing each figure's strategy and (where applicable) its sub-prompt.

### Phase 3 — Adaptive Design Decisions

#### 3.1 Visual style (driven by paper type)

- *Theory / mathematical* → minimalist geometric: lots of whitespace, serif title, geometric accents.
- *Experimental / engineering / AI* → modern infographic: clear hierarchy, supporting icons, sans-serif, visual leading lines.
- *Survey / position* → editorial feature: large titles, refined magazine-style typography.
- *Bio / Med / life science* → choose between modern-infographic and scientific-illustration based on the paper's emotional tone.
- *Dataset / benchmark* → data-dashboard: emphasized data-viz hierarchy.

#### 3.2 Color palette (fully adaptive — never hardcode subject → color)

**Rule: never reason "CS uses blue, Bio uses warm tones".** Decide the palette from the paper's content emotion:

- Emotional tone — serious / playful / cold / warm / cutting-edge / classical / mysterious.
- The research subject's intrinsic color language — neurons can be warm or cold; quantum can be deep neon or pure-white minimalist; "the answer comes from the paper, not the field".
- Target audience expectation.
- The author's likely aesthetic, glimpsed from the original PDF's typesetting and figure colors.

Output a **3–5 color palette** with HEX values and roles:

- *Dominant* — largest area
- *Secondary* — support
- *Accent* — key data / highlight
- *Background*
- *Text*

All combinations must satisfy WCAG AA contrast.

#### 3.3 Information density

- short paper → *classic-complete*: full Abstract / Intro / Method / Results / Conclusion.
- medium paper → *balanced*: selected elements; method and results get larger area.
- long paper → *minimalist-visual*: only the 3–5 strongest highlights and the key figures.
- survey → main structure diagram + key branches.

#### 3.4 Layout (must reserve a C-position for the anchor)

- 3-column classic — full elements (short paper preferred).
- 2-column + central hero figure — method paper with one dominant figure; the anchor goes central.
- Asymmetric visual center — single dramatic conclusion paper.
- Top hero + multi-column below — survey or story-shaped paper.
- **Distinctive Anchor Spotlight section** — regardless of overall layout, dedicate one section to the anchor (typically architecture diagram + evidence screenshot/Mockup). This section's area must be **≥ 20% of the poster body**. It is the poster's memory hook.

#### 3.5 Typography

- Title and body fonts must contrast but feel coherent within the chosen visual style.
- For Chinese papers, specify both a CJK and a Latin font.
- Recommended sources: Google Fonts, Adobe Fonts, the 思源 family, IBM Plex, Inter.

### Phase 4 — Asset Preparation

- For *preserve* figures: extract bitmap data; ready as reference/material `input_image` assets for whichever route in the chain accepts them.
- For *redraw* figures: confirm the sub-prompt is style-aligned with the master poster.
- For *Mockup redraw* figures: confirm platform language, verbatim text, "示意图" badge, and style unity are all in the sub-prompt.
- Compile the reference image list and pre-assigned poster placements. The reference image list must contain preserve-class evidence originals only; concept/structure redraws stay in text instructions.

### Phase 5 — Master Prompt Construction

Assemble one structured long prompt with the following blocks:

```
[TASK]
A single A0 portrait academic research poster. Aspect ratio 2:3 portrait, ~841×1189mm scale. Print-quality, conference-grade.

[PAPER]
Title: "<exact title>"
Topic: <1–2 sentences>
Distinctive anchor: <one sentence naming the anchor, e.g. "OpenClaw multi-agent debate framework with real Feishu chat evidence">

[VISUAL STYLE]
Overall aesthetic: <Phase 3.1 chosen style>
Style anchors: <2–3 concrete sentences, e.g. "modern infographic with clean geometric accents, generous whitespace, editorial-grade typography">

[COLOR PALETTE — strict]
Dominant: #XXXXXX (<role>)
Secondary: #XXXXXX (<role>)
Accent: #XXXXXX (<role>)
Background: #XXXXXX (<role>)
Text: #XXXXXX (<role>)

[TYPOGRAPHY]
Title font: <font>, weight: bold
Body font: <font>, weight: regular
(Chinese paper) CJK font: <font>

[LAYOUT]
<top-to-bottom region map; mark the Distinctive Anchor Spotlight zone explicitly>

[TOP HEADER ZONE]
- Main title (rendered exactly as written, no modification): "<exact title>"
- Authors (verbatim): "<exact author list>"
- Affiliation: "<institution>"
- Venue: "<formal journal/conference + year>" — use the formal name only (logo / ISSN allowed); never preprint pagination, watermarks, peer-review markings

[CONTENT SECTIONS — every quoted string is rendered verbatim]
Section 1 — <Background / Motivation>:
  Text (verbatim): "<exact content>"
Section 2 — Method:
  Text (verbatim): "<exact content>"
  Figure: <if redraw — full sub-prompt; if preserve — "use reference image #N at center of this section">
Section 3 — Key Results:
  Text (verbatim): "<exact content with all key numbers>"
  Figure: <as above>
Section 4 — Distinctive Anchor Spotlight (mandatory):
  - 1–2 figures: typically architecture/flow redraw + evidence screenshot or UI Mockup
  - Each carries 1–2 sentences naming the case, with real dialogue snippets or runtime data
  - Highest visual weight on the poster
Section 5 — Conclusion / Impact:
  Text (verbatim): "<exact content>"

[DECORATIVE ELEMENTS]
- Margins: ~40–60px equivalent, balanced
- Whitespace rhythm: <matches the chosen style>
- Accent elements: <geometric lines / icons / gradients / illustration, per style>
- Section dividers: <how each section is separated>

[STRICT PROHIBITIONS]
- NO QR code anywhere
- NO DOI / URL bottom bar
- NO placeholder boxes labeled "[Figure X]"
- NO "Scan me" / "Read more" callouts
- NO lorem ipsum
- NO preprint pagination stubs ("002", 网络首发页码, "DOI placeholder number", arXiv preprint watermark, "Under review", "For peer review", peer-review line numbers); only formal venue / logo / ISSN
- NO abstract framework boxes replacing evidence visuals — evidence-class visuals must be original or labeled "示意图 / Illustrative Mockup"; abstract boxes do not count
- All rendered text must be spelled correctly — especially author names, technical terms, numeric values

[REFERENCE IMAGES]
Image #1: <description + placement>
Image #2: <description + placement>
...

[QUALITY TARGETS]
- Print-ready at A0 size
- Clear visual hierarchy readable from 1–2 meters
- No visual clutter, no crowded text blocks
- Unified color and typographic system throughout
- The distinctive anchor is visually dominant and unmistakable
```

### Phase 6 — Generation and Self-Audit

**Generate**: call the highest-tier route in the chain still untried, passing the master prompt + reference images. Specify portrait ratio (2:3 first, fall back to 3:4 only if the route rejects 2:3). Request the highest-quality / largest-size parameter the route exposes.

**Verify pixel dimensions** with PIL / `identify` / equivalent on the downloaded file. The label rendered inside the poster is irrelevant; only the file's actual dimensions count.

**Self-audit checklist (every item must pass)**:

- [ ] Title, authors, affiliation spelled correctly
- [ ] 3–5 hook-style highlights, not abstract regurgitation
- [ ] Distinctive anchor visually prominent (dedicated section or visual center), not buried in abstract theory
- [ ] All Phase 2 *preserve* figures integrated correctly
- [ ] All Phase 2 *Mockup redraw* figures carry the "示意图 / Illustrative Mockup" badge with correct platform visual language
- [ ] Layout is portrait, ratio close to 2:3
- [ ] No gibberish, no spelling errors, no hallucinated numbers (cross-check with paper)
- [ ] Color and typography match the chosen Phase 3 style
- [ ] No QR code, no DOI bottom bar, no placeholder boxes
- [ ] No 网络首发 pagination, no preprint watermark, no peer-review markings; the formal venue label sits in a sensible location
- [ ] Visual hierarchy clear; main message readable from 1–2 meters
- [ ] **Long edge ≥ 2304 px** verified by file inspection
- [ ] **No upscale / no overlay / no compositing** has been applied to the returned image

**Severe issues** (text misalignment, ratio error, missing key info, gibberish, leaked preprint pagination, anchor buried, dimension below floor): adjust the prompt and retry on the same route, **maximum 2 retries**. If 3 attempts on a route all fail, drop down the chain. If the entire chain is exhausted, surface the boundary to the user with a manual-fix suggestion — never patch the result locally.

## Final Delivery (this route only)

Show the user only:

1. The poster image — `MEDIA:/absolute/path/to/poster.png` or the route's native image URL — exactly as the model returned it.
2. A 1–2 sentence Chinese design note covering: chosen visual style, why this paper merited that choice, how the anchor is presented, and the emotional rationale for the palette.

Do **not** show: design rationale doc, asset bundle, raw prompt, figure manifest, theoretical exposition, route comparison summary unless the user asked for one.

This concise response does **not** waive local file saving, manifest creation, or platform delivery (Telegram for non-synced deliverables) per the project's standard contract.

## Locked Adaptive Decisions (do not interrupt the user mid-flow)

Style, density, palette, layout, typography, ratio (A0 portrait 2:3), and redraw-vs-preserve decisions are all derived by this skill from the paper's content. Ask the user only when:

- No source can be retrieved.
- Multiple papers match an ambiguous title.
- Choosing among equally valid evidence sets would change the paper's scientific message.

## Anti-Patterns (must do)

- ✅ Read enough of the paper to ground every poster claim before designing.
- ✅ Three-axis classification (type / length / field) drives every later decision.
- ✅ Filter out 网络首发 pagination and preprint markings during identifier hygiene.
- ✅ Identify and visually dominate at least 1–2 distinctive anchors (≥ 20% of poster body).
- ✅ Triage figures: redraw concept; preserve data + observation + evidence-class; Mockup-redraw evidence-class only when extraction is impossible, with the "示意图" badge.
- ✅ Derive the palette from the paper's content emotion, not from the field.
- ✅ A0 portrait 2:3, native long edge ≥ 2304 px verified by file inspection.
- ✅ Every quoted string renders verbatim — title, authors, key numbers, dialogue.
- ✅ Self-audit before delivery; ≤ 2 retries per route.

## Anti-Patterns (must not do)

- ❌ Hardcoded "field → color" mapping (CS → blue, Bio → warm).
- ❌ Any QR code, DOI bottom bar, URL watermark.
- ❌ Any 网络首发 pagination, preprint watermark, peer-review line number, "Under review" tag.
- ❌ Abstract framework boxes / generic concepts replacing the paper's distinctive anchor.
- ❌ Replacing evidence-class visuals with abstract diagrams (preserve original or labeled high-fidelity Mockup, no third option).
- ❌ Fabricated data, authors, conclusions, dialogue.
- ❌ Rewriting title, author names, or core numbers in your own voice.
- ❌ **Upscaling, resizing-to-larger, or super-resolution on the returned image** — if it's small, regenerate; do not enlarge.
- ❌ **Local text overlay, logo / footer stamping, figure stitching, border crop, or any post-AI compositing** — the model's output is the final deliverable.
- ❌ Designing before reading the source.
- ❌ Producing anything beyond the poster image + 1–2 sentence design note.
- ❌ Mid-flow style / density / size / palette questions to the user.
- ❌ Long-form design theory or pedagogical explanation in the user-facing response.
- ❌ Silently switching to non-GPT Image 2 models (Nano Banana Pro, Gemini Image, Qwen-Image, Seedream, etc.).
- ❌ Silently switching to deterministic / hybrid compositing after a chain failure — surface the boundary instead.
