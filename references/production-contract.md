# Production Contract for Paper Academic Poster

Load this reference for every `paper-academic-poster` run. The default production route is divide-and-compose: decompose the poster into semantic regions, produce each text/diagram/evidence/generated panel through the most reliable method for that region, then deterministically compose the final A0-ratio poster. One-shot GPT Image 2 whole-poster generation is an opt-in exception for briefs that explicitly prioritize model-only authorship over exact text/layout/evidence fidelity.

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
- `action`: preserve-original / redraw-concept / generate-subimage / omit
- `poster_role`: method hero / result proof / example / background / limitation
- `risk`: too dense / low resolution / non-central / copyright-sensitive / none

Rules:

- Evidence-class visuals include UI screenshots, dialogue captures, terminal/session logs, experiment-scene photos, real observation artifacts, and data charts/tables with exact values. By default, preserve selected high-signal originals from this class as cleaned source crops inside the deterministic final composition. Use a generated mockup only when extraction is infeasible; label it clearly as illustrative.
- Concept/structure visuals include framework diagrams, box/arrow concept figures, pipelines, and architecture diagrams. By default, redraw them deterministically in the poster's visual style; keep ordering, labels, arrows, groupings, and hierarchy. Do not paste the original concept diagram beside its redraw unless the source artifact itself is being discussed as evidence.
- Dense tables: do not ask GPT Image 2 to render full unreadable tables. Use a verified excerpt, one key row/column, or a source crop with a nearby deterministic summary label. For source-fidelity claims, preserve the original crop.
- Formulas: include only if central to the contribution. Render formulas deterministically or as source crops, not inside generated image text.
- Captions: shorten aggressively but keep what the evidence demonstrates.
- Redundancy rule: if a source visual is concept/structure class and the poster redraws that idea, mark the original as `omit` rather than sending it as another visible panel.

## 3. Poster-Specific Metadata Compression

- Title: use exact paper title unless it is too long; if shortened, preserve the technical noun phrase and avoid new claims.
- Authors:
  - 1-5 authors: list all if readable.
  - More than 5: use first author + “et al.” unless the paper convention demands all authors.
- Affiliations: include only top-level institution names if space allows; otherwise omit or place in a tiny footer.
- Venue/year/DOI: prefer footer format: `<Venue or Journal>, <Year> · DOI: <doi>`.
- QR code: do not include by default.

## 4. Layout Execution Contract

Choose one route and record it in `manifest.json` or `RUN_INFO.md`. Unless the user explicitly requests one-shot/direct whole-poster model authorship, choose the divide-and-compose route.

### Divide-and-compose route (default)

Use for normal paper-to-poster requests, including Chinese, social-science, information-science, evidence-rich, design-driven, 4K, and print-oriented academic posters. This route optimizes for factual fidelity, local text quality, high-resolution export, and controllable design.

- Build an A0-ratio vertical canvas (841:1189) or user-requested ratio. Use at least `2480x3508`; for 4K delivery use `2896x4096` or higher.
- Divide the poster into named regions before production: header/metadata, motivation or abstract, method/framework, distinctive anchor, evidence/results, implications/limitations, and footer. Adapt region count to the paper; do not force all slots when a different story structure is better.
- Assign each region an asset strategy:
  - `local-text`: exact title, authors, labels, claims, captions, numeric values, venue, DOI/ORCID.
  - `source-crop`: evidence screenshots, data charts, tables, photos, or original artifacts.
  - `deterministic-diagram`: concept diagrams, pipelines, architecture boxes/arrows, small tables, formulas.
  - `generated-subimage`: no-text/low-text atmosphere, hero art, icon sheet, illustrative mockup, stylized connector visual, or background texture.
  - `mixed-panel`: a generated or cropped visual placed under/next to deterministic labels and captions.
- Generate sub-images independently. Prompts must be slot-specific and should avoid dense text; any text inside a generated sub-image is non-authoritative until inspected.
- Compose the final poster deterministically with local fonts, measured margins, explicit grid tracks, source crops, diagrams, and generated sub-images. Do not use a one-shot AI poster as the base layer.
- Export `poster.png`; export `poster.pdf` when useful for print. Record requested and actual output dimensions.
- If QC fails, fix the affected region and re-export. Regenerate only the failed sub-image or redraw the failed diagram; do not restart the whole poster unless the overall design premise is wrong.

### One-shot GPT Image 2 route (explicit opt-in)

Use only when the user explicitly asks for GPT Image 2 一站式生成, direct whole-poster, model-only authorship, or no local layout/text composition.

- Generate the entire poster as one GPT Image 2 image.
- Attach selected evidence-class originals as references only when the route supports them.
- Name the trade-off: this route can be visually coherent but cannot guarantee exact small text, readable evidence, or pixel-faithful source reproduction.
- If QC fails, regenerate in the same one-shot route or ask before switching back to divide-and-compose.

### Adaptive Chinese conceptual / case-anatomy design

Use this design-reading framework for Chinese conceptual, social-science, information-science, library-and-information-science, AI-agent, workflow, or system papers when the user asks for a polished “学术海报”. It is not a separate production route: apply these judgments to the divide-and-compose region plan, source crop selection, deterministic redraws, and generated sub-image prompts.

- Start with a design reading before layout: identify the paper’s central thesis, the conceptual tension or transformation it argues for, the strongest evidence/case anchor, and the 1-2 visual metaphors or structural contrasts that can carry the poster.
- Make aggressive content choices. Do not try to represent every section. Every title, crop, card, icon, and number must earn its space by advancing the central thesis or evidencing a key claim.
- Use formal academic metadata only to the extent it supports the poster: exact Chinese title, optional English subtitle from the paper, authors, institution, venue/journal or network-first date, and compact ISSN/CN/URL/ORCID/keyword metadata when available. Do not invent missing metadata; omit instead.
- The opening visual move should reveal the paper’s argument, not merely enlarge text. Examples include a before-after contrast, a role transition, a conceptual map, a case dissection, or a high-signal evidence juxtaposition. Choose the move that best fits the source.
- Redraw concept-level theoretical diagrams deterministically while preserving labels, ordering, arrows, and qualifiers. Do not attach original source diagrams as visible material panels when the poster redraws the same logic. Do not redraw evidence charts/tables/screenshots unless explicit source data supports reconstruction; otherwise preserve source crops.
- For evidence-class screenshots/tables/data visuals, select only the few that best serve the thesis. Crop with intent: remove margins/noise, keep labels needed for evidence, and add a nearby source-anchored interpretation. Avoid both unreadable tiny galleries and decorative oversized crops that do not advance the argument.
- Use impact/contribution/risk cards only when they sharpen the argument. The number, position, color, and shape of cards are adaptive decisions, not defaults. Keep body text concise and source-anchored.
- Visual tone should be chosen from the paper’s topic and materials: formal academic, magazine-like, technical blueprint, archival/documentary, evidence wall, or other fitting grammar. Maintain aesthetic discipline: strong hierarchy, purposeful whitespace, consistent palette, and no decorative clutter.
- Record in the manifest that the route was divide-and-compose with adaptive Chinese conceptual / case-anatomy design, including the design reading, key omissions, source assets, generated sub-images, deterministic redraws, and final export path.

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
- `visual_assets_used`: list of figure/table/screenshot ids, class, action, and whether the original was preserved, redrawn, generated, or omitted as redundant
- `region_plan`: list of poster regions, asset strategy, source/generator, and final placement
- `generated_subimages`: prompt path, model/provider, requested size, actual size, QC status
- `output_files`: poster image/PDF paths
- `qc_status`: pass/fail plus short notes
- `naming_exception`: if an external tool forces fixed filenames

## 6. Quality Control Checklist

Before delivery, verify:

- Paper title is spelled correctly.
- Authors/venue/year/DOI are either correct or omitted.
- Every numeric claim appears in the source.
- No invented dataset/baseline/result appears.
- Selected evidence-class originals are preserved as source crops or source-data deterministic renderings. Generated mockups are labeled as illustrative.
- Concept/structure diagrams are redrawn or omitted as redundant; if redrawn, they preserve the method’s logical order and relationships.
- No original concept/structure diagram is duplicated as a source evidence panel when the poster already redraws the same logic.
- Text is legible at poster scale; no long paragraphs.
- No QR code, fake logo, placeholder, blank key panel, gibberish, lorem ipsum, pseudo-text, or stray watermark.
- High-contrast key claim panels: vision/OCR should be able to read the claim, not mistake it for an empty placeholder.
- Mobile/Telegram preview hierarchy: at 50% zoom the poster’s chosen hierarchy must still be evident: the title/topic, central argument, main visual/evidence anchor, and key section headings should be readable. If the design only works when fully zoomed in, simplify, crop harder, or recompose before delivery.
- Wrapped text inside panels: long footers, quality-gate notes, and source-boundary notes must not clip at the right edge.
- Brand/model spelling is consistent across the poster (for example, `OpenClaw` must not become `Openclaw`).
- Final image path exists and opens.
- Clarity provenance is explicit in the manifest: final native dimensions, whether any sub-image was upscaled, which sub-images used GPT Image 2/provider routes, and which regions were deterministic/source-preserved.

If any scientific-fidelity item fails, do not deliver. Fix the relevant region, regenerate the failed sub-image, redraw the failed diagram, or simplify the layout and re-export. Do not silently switch to one-shot whole-poster generation after a divide-and-compose QC failure.
