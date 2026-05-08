# Production Contract for Paper Academic Poster

Load this reference for every `paper-academic-poster` run. The default production route is a single GPT Image 2 direct whole-poster generation; deterministic/hybrid local composition is an opt-in exception for briefs that explicitly prioritize exact text/layout or source-faithful evidence preservation over direct AI authorship.

## 1. Retrieval and Verification Order

Use the strongest available source first. Do not invent missing metadata.

### DOI input

1. Use academic-paper/fulltext tools if available (`ai4scholar`, Semantic Scholar/OpenAlex/Crossref wrappers, or equivalent).
2. Retrieve metadata: title, authors, affiliations if present, venue, year, DOI.
3. Retrieve full text or PDF when legally/technically accessible.
4. If full text is unavailable, ask for PDF/text before designing; abstracts alone are usually insufficient for evidence-rich posters.

### Title input

1. Search title with academic tools to identify DOI/URL.
2. Verify that the top result matches title/authors/year.
3. Continue as DOI input.
4. If multiple papers match, ask the user which one before proceeding.

### URL input

1. Fetch page and identify whether it is HTML full text, abstract page, or PDF.
2. Download/extract PDF when available.
3. Cross-check metadata from the page/PDF first page.

### PDF/local file input

1. Extract text with PDF/OCR tooling (`ocr-and-documents`, PyMuPDF, pdftotext, marker, or equivalent available tools).
2. Extract figures/tables/screenshots using PyMuPDF/pdfimages/pdftoppm or equivalent.
3. Preserve figure numbers/captions and page locations in a small manifest.

## 2. Figure and Table Extraction Contract

For each candidate visual asset, record:

- `id`: paper figure/table number or generated stable id
- `source_page`: PDF page or URL location
- `caption`: exact or shortened caption
- `kind`: evidence / concept / atmosphere
- `action`: preserve-original / redraw-concept / omit
- `poster_role`: method hero / result proof / example / background / limitation
- `risk`: too dense / low resolution / non-central / copyright-sensitive / none

Rules:

- Evidence-class visuals include UI screenshots, dialogue captures, terminal/session logs, experiment-scene photos, real observation artifacts, and data charts/tables with exact values. By default, attach only selected high-signal originals from this class as GPT Image 2 reference/material inputs and treat the result as AI-rendered/stylized evidence panels rather than a source-faithful reproduction. If the user explicitly asks for deterministic evidence fidelity, preserve original crops or recreate deterministically from source data only when data is explicitly available.
- Concept/structure visuals include framework diagrams, box/arrow concept figures, pipelines, and architecture diagrams. For the default direct route, convert them into redraw instructions in the GPT Image 2 prompt; keep ordering, labels, arrows, groupings, and hierarchy. Do not attach the original concept diagram as a visible material panel when the poster already redraws the same logic. Use deterministic redrawing only in an explicitly authorized deterministic/hybrid route.
- Dense tables: do not ask GPT Image 2 to render full unreadable tables. For the default direct route, supply the table crop as a material and summarize it with one short label or claim. Use a verified excerpt, one key row/column, or a source-faithful mini table only in an explicitly authorized deterministic route.
- Formulas: include only if central to the contribution. For the default direct route, keep formulas short or omit them; render formulas deterministically only in an explicitly authorized deterministic route.
- Captions: shorten aggressively but keep what the evidence demonstrates.
- Redundancy rule: if a source visual is concept/structure class and the poster prompt already redraws that idea, mark the original as `omit` rather than sending it as another visible panel.

## 3. Poster-Specific Metadata Compression

- Title: use exact paper title unless it is too long; if shortened, preserve the technical noun phrase and avoid new claims.
- Authors:
  - 1-5 authors: list all if readable.
  - More than 5: use first author + “et al.” unless the paper convention demands all authors.
- Affiliations: include only top-level institution names if space allows; otherwise omit or place in a tiny footer.
- Venue/year/DOI: prefer footer format: `<Venue or Journal>, <Year> · DOI: <doi>`.
- QR code: do not include by default.

## 4. Layout Execution Contract

Choose one route and record it in `manifest.json` or `RUN_INFO.md`. Unless the user explicitly requests deterministic/local composition, choose the direct GPT Image 2 whole-poster route.

### Direct GPT Image 2 whole-poster route (default)

Use for normal paper-to-poster requests, including Chinese, social-science, information-science, evidence-rich, and design-driven academic posters. This route respects the user's authorship boundary: the final image is generated by GPT Image 2, not assembled afterward.

- Generate the entire poster as one GPT Image 2 image. Do not build a deterministic text/layout layer.
- Attach selected evidence-class originals as `input_image` reference/material inputs when the route supports image references. Convert concept/structure visuals into redraw instructions instead of sending every original diagram. In Hermes, the built-in `image_generate` only accepts prompt/aspect ratio; use the Codex Responses `image_generation` route directly when evidence reference images are required. See `references/gpt-image-2-direct-reference-assets.md` for the implementation/QC pattern.
- Prompt the model to incorporate preserved evidence references as visible material/evidence panels and to redraw concept/structure visuals in the unified poster style, but treat the result as AI-rendered/stylized evidence, not a guarantee of pixel-identical source preservation.
- Keep text short: exact title, authors, and a small set of section labels. Avoid long body paragraphs because GPT Image 2 small text will be unreliable.
- **Default native size: `2416x3424` portrait, `quality=high`** (A-series-ish ratio, ~8 MB native PNG, ~3-4 min generation). This is the固化 default — do not silently downgrade to 1024×1536 just because Hermes' built-in `image_gen` is convenient. Use the bundled helper `references/codex_direct_image_gen.py` to bypass Hermes' size lock. Only fall back to smaller sizes (1024×1536 / 2048×3072) when the user explicitly asks for a quick preview or when 2416×3424 fails repeatedly. Do not add local text, layout, screenshots, patches, or overlays after generation. Report requested and actual native dimensions separately from any resized delivery file.
- If comparing multiple GPT Image 2 providers, load `references/direct-provider-comparison.md`, keep prompt/reference inputs comparable, verify actual pixel dimensions, and deliver only pass-line outputs.
- If QC fails, regenerate using the same direct GPT Image 2 route, simplify the prompt/material set, or ask before switching to deterministic/hybrid composition.
- Record in the manifest that the route was direct GPT Image 2 with classified evidence-original references, concept-redraw instructions, requested/actual native size, and whole-image resize only if applicable.

### Evidence-light AI subcase

Use this lighter subcase when exact embedded evidence is not required and no source crops are useful.

- Build a compact English prompt with exact title/author and short section labels.
- Use active GPT Image 2 route only.
- Inspect the image; regenerate if text/logic/facts fail.

### Evidence-rich deterministic route

Use only when the user explicitly requests deterministic exact text/layout, source-faithful figure/table/photo preservation, print/PDF production, or authorizes local composition after direct generation fails QC.

- Build an A0-ratio vertical canvas (841:1189) or user-requested ratio.
- Use deterministic text rendering for title, headings, bullets, numeric claims, citations, formulas, and table excerpts.
- Insert evidence assets from extracted original files.
- Use generated art only for background/conceptual panels, not exact evidence.
- Export `poster.png`; export `poster.pdf` if print workflow is useful.

### Hybrid route

Use only when visual unity is needed but the user explicitly prioritizes text/evidence accuracy over direct GPT Image 2 whole-poster authorship.

- Generate background/hero/concept panel with GPT Image 2, preferably with no text at all (`no words, no letters, no QR code, no logos, no watermark`).
- Compose the entire poster deterministically with exact text and evidence assets.
- Use a true A0-ratio canvas (841:1189; e.g. 2480×3508 for delivery PNG) and local fonts for all Chinese/English text.
- Do not patch a flawed full AI poster; use AI assets as components inside a deterministic whole page.
- If the poster contains dense Chinese text, exact numbers, or multiple source figures, consult `references/hybrid-deterministic-composition.md` before rendering.

### Adaptive Chinese conceptual / case-anatomy route

Use this design-reading framework for Chinese conceptual, social-science, information-science, library-and-information-science, AI-agent, workflow, or system papers when the user asks for a polished “学术海报”. It is not a separate local-composition route by default: apply these judgments to the direct GPT Image 2 prompt and material selection unless the user explicitly authorizes deterministic/hybrid composition.

- Start with a design reading before layout: identify the paper’s central thesis, the conceptual tension or transformation it argues for, the strongest evidence/case anchor, and the 1–2 visual metaphors or structural contrasts that can carry the poster.
- Make aggressive content choices. Do not try to represent every section. Every title, crop, card, icon, and number must earn its space by advancing the central thesis or evidencing a key claim.
- Use formal academic metadata only to the extent it supports the poster: exact Chinese title, optional English subtitle from the paper, authors, institution, venue/journal or network-first date, and compact ISSN/CN/URL/ORCID/keyword metadata when available. Do not invent missing metadata; omit instead.
- The opening visual move should reveal the paper’s argument, not merely enlarge text. Examples include a before→after contrast, a role transition, a conceptual map, a case dissection, or a high-signal evidence juxtaposition. Choose the move that best fits the source.
- For direct GPT Image 2 generation, describe concept-level theoretical diagrams clearly as redraw instructions. Do not attach original source diagrams as visible material panels when the poster redraws the same logic. If and only if deterministic composition is explicitly authorized, redraw concept-level diagrams deterministically while preserving labels, ordering, arrows, and qualifiers. Do not locally redraw evidence charts/tables/screenshots unless explicit source data supports deterministic reconstruction and the deterministic route is active.
- For evidence-class screenshots/tables/data visuals, select only the few that best serve the thesis. Crop with intent: remove margins/noise, keep labels needed for evidence, and add a nearby source-anchored interpretation. Avoid both unreadable tiny galleries and decorative oversized crops that do not advance the argument.
- Use impact/contribution/risk cards only when they sharpen the argument. The number, position, color, and shape of cards are adaptive decisions, not defaults. Keep body text concise and source-anchored.
- Visual tone should be chosen from the paper’s topic and materials: formal academic, magazine-like, technical blueprint, archival/documentary, evidence wall, or other fitting grammar. Maintain aesthetic discipline: strong hierarchy, purposeful whitespace, consistent palette, and no decorative clutter.
- Record in the manifest that the route was direct GPT Image 2 with adaptive Chinese conceptual / case-anatomy prompt design, including the design reading, key omissions, source/material assets supplied, and the image/provider route.

## 5. Manifest Contract

Write `manifest.json` or `RUN_INFO.md` with at least:

- `topic_slug`
- `provenance_tag`
- `artifact_role`: academic_poster
- `primary_framework_or_stack`
- `primary_executor`
- `primary_model_or_route`
- `run_date`
- `input_boundary`: what source was used
- `paper_metadata`: title/authors/venue/year/DOI when available
- `visual_assets_used`: list of figure/table/screenshot ids, class, action, and whether the original was preserved, redrawn, or omitted as redundant
- `output_files`: poster image/PDF paths
- `qc_status`: pass/fail plus short notes
- `naming_exception`: if an external tool forces fixed filenames

## 6. Quality Control Checklist

Before delivery, verify:

- Paper title is spelled correctly.
- Authors/venue/year/DOI are either correct or omitted.
- Every numeric claim appears in the source.
- No invented dataset/baseline/result appears.
- For default direct GPT Image 2 route, selected evidence-class originals were supplied as reference/material images or reference URLs and are visibly represented without local overlay. For deterministic exception routes, evidence figures are original or source-data deterministic.
- Concept/structure diagrams are redrawn or omitted as redundant; if redrawn, they preserve the method’s logical order and relationships.
- No original concept/structure diagram is duplicated as a source evidence panel when the poster already redraws the same logic.
- Text is legible at poster scale; no long paragraphs.
- No QR code, fake logo, placeholder, blank key panel, gibberish, lorem ipsum, pseudo-text, or stray watermark.
- High-contrast key claim panels: vision/OCR should be able to read the claim, not mistake it for an empty placeholder.
- Mobile/Telegram preview hierarchy: at 50% zoom the poster’s chosen hierarchy must still be evident—the title/topic, central argument, main visual/evidence anchor, and key section headings should be readable. If the design only works when fully zoomed in, simplify, crop harder, or regenerate at a clearer native size before delivery.
- Wrapped text inside panels: long footers, quality-gate notes, and source-boundary notes must not clip at the right edge.
- Brand/model spelling is consistent across the poster (for example, `OpenClaw` must not become `Openclaw`).
- Final image path exists and opens.
- Clarity provenance is explicit in the manifest: final native dimensions, whether the image was upscaled, and which GPT Image 2/provider route (native/Codex, YouMind, ListenHub, or deterministic-only) was used.

If any scientific-fidelity item fails, do not deliver. Fix by regeneration in direct GPT Image 2 mode, simplify the prompt/materials, or use deterministic whole-poster composition only when that route is explicitly allowed by the user. Do not silently switch to deterministic/hybrid composition after QC failure.
