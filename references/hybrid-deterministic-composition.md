# Divide-and-Compose Poster Production Notes

Use these notes for the default `paper-academic-poster` route. The poster is produced by decomposition: read the paper, plan semantic regions, generate or render each component with the most reliable method, then compose the final A0-ratio image deterministically.

## When to use

- Normal paper-to-poster requests.
- Chinese-text-heavy, evidence-rich, exact-number, source-figure, print/PDF, 4K, or dense-coverage requests.
- Design-driven requests where the poster needs a distinctive anchor but still must preserve text and evidence quality.

Use a different route only when the user explicitly asks for a one-shot GPT Image 2 whole-poster image or rejects local layout/text composition.

## Region Planning

Start with a compact design reading:

- What is the central thesis?
- What is the paper's distinctive anchor: named system, case, dataset, experiment, transcript, data exhibit, or original conceptual move?
- Which evidence should be source-preserved?
- Which concept figures should be redrawn?
- Which regions benefit from generated art rather than deterministic drawing?

Then create a region plan. Typical regions:

- `header`: exact title, authors, affiliation, venue/journal/year/DOI if useful.
- `context`: abstract, motivation, research question, or conceptual tension.
- `method`: architecture, pipeline, framework, experimental design, or analytical model.
- `anchor`: the largest slot; the thing only this paper demonstrates.
- `evidence`: source screenshots, data charts, tables, transcripts, photos, or observation artifacts.
- `results`: key numbers, baselines, contributions, or section logic.
- `implications`: impact, limitations, risks, future work.
- `footer`: source boundary, keywords, ORCID, short takeaway.

Each region gets one strategy: `local-text`, `source-crop`, `deterministic-diagram`, `generated-subimage`, or `mixed-panel`.

## Component Production

### Local text

Render title, authors, headings, captions, bullets, numeric claims, venue, DOI/ORCID, and Chinese body text locally with installed fonts. Wrap text explicitly. Never rely on GPT Image 2 for dense or exact text.

### Source evidence

Extract PDF page renders and embedded images with PyMuPDF/pdfimages/pdftoppm or equivalent. Crop evidence with intent: remove margins/noise, keep labels needed for interpretation, and pair it with deterministic captions or evidence-to-claim notes. Use 2-4 high-value evidence assets by default unless the user explicitly asks for density.

### Deterministic diagrams

Redraw framework, box/arrow, pipeline, architecture, formula, and compact table content as SVG/HTML/CSS/PIL/Canvas. Preserve labels, ordering, arrows, groupings, and qualifiers. Use consistent line weights, icons, typography, and color tokens across diagrams.

### Generated sub-images

Use GPT Image 2 for no-text or low-text sub-images: atmosphere, hero illustration, background field, icon sheet, visual metaphor, stylized connector, or illustrative mockup. Generate these independently and inspect them before composition. For prompts and helper usage, see `references/gpt-image-2-direct-reference-assets.md`.

If a generated panel contains pseudo-text, crop or regenerate the panel before composition. Do not hide fake text under local labels unless it is fully covered and irrelevant.

## Composition

Build the full poster deterministically:

- A0/A-series portrait ratio: 841:1189.
- Default PNG: `2480x3508` or higher.
- 4K delivery: `2896x4096` or higher.
- Use local fonts for all Chinese/English text.
- Use stable dimensions for repeated cards, grids, icon buttons, panels, and evidence crops.
- Avoid cards-inside-cards; use full-width bands, framed evidence panels, and unframed section layouts.
- Use a consistent palette and spacing scale. Do not let generated sub-images dictate unrelated colors unless the region plan says so.
- Export `poster.png`; export `poster.pdf` when print workflow is useful.

## Adaptive Chinese Conceptual Poster Pattern

Use this pattern when the paper is concept-heavy and Chinese-text-heavy, especially for information science, AI agents, workflow/system papers, or papers whose strongest visual evidence is architecture diagrams, pipelines, screenshots, tables, or conceptual frameworks.

- Story hierarchy is adaptive: first decide what the paper is really about, what contrast or transformation makes it memorable, and which evidence should become the visual anchor. Only then choose layout.
- Possible rhythms include formal conference poster, case anatomy, evidence wall, conceptual before-after, pipeline dissection, or magazine-style feature. Do not force title-band / framework / case-block / cards if another structure better serves the paper.
- Formal metadata, framework contrast, case anatomy, and impact cards are optional ingredients. Use them when they clarify the thesis; omit or rearrange them when they dilute the design.
- Crop and curate ruthlessly: select 2-4 high-value evidence assets at most for a single poster unless the user explicitly requests density.
- For concept diagrams such as “三要素 → 四要素”, redraw deterministically only after understanding the logic. Make it visually expressive but source-faithful.
- Aesthetic discipline matters: maintain a coherent palette, type rhythm, icon style, line weight, and whitespace. Avoid generic pastel dashboards, rigid templates, ornamental backgrounds, and mechanically copied layouts.

## Proven Route

1. Extract PDF text and page renders with PyMuPDF.
2. Create a contact sheet for page renders and extracted images; inspect with vision/OCR to identify figure numbers, captions, and whether each asset is evidence vs concept.
3. Write `region_plan.json` or include region planning in `manifest.json`.
4. Generate only the sub-images that need image generation. Prompt must specify component role, slot dimensions, style, and no dense text.
5. Build the full poster deterministically with exact local text, source crops, deterministic diagrams, and generated sub-images.
6. Write a manifest with source boundary, paper metadata, route/model, region plan, evidence assets used, generated sub-images, numeric-claim anchors, output files, and QC status.
7. Run visual/OCR QC on the rendered poster, not only the source PDF or individual components.

## QC Pitfalls

- Text drawn over a transparent/light title box can look blank to vision reviewers even when technically present; prefer higher-contrast filled panels for key claims.
- Long one-line footer or quality-gate text can appear clipped; wrap it inside its panel with explicit max width.
- Tool/brand names must be normalized after deterministic rendering (e.g., `OpenClaw`, not `Openclaw`).
- Evidence thumbnails may be too small to read; if used as proof thumbnails, label them as source evidence and summarize the claim nearby.
- Both tiny unreadable thumbnails and oversized decorative screenshots are failure modes: crop fewer assets, enlarge only what advances the thesis, and summarize the evidence nearby.
- Image-generation prompts saying “no words” still need output inspection; generated backgrounds may introduce pseudo text/logos.
- Phone-preview QC: view the rendered poster at roughly 50% scale or on the delivery surface. The poster’s chosen hierarchy must still be evident: title/topic, central argument, main visual/evidence anchor, and key headings should be readable without deep zoom.
- If a generated sub-image looks soft, regenerate that sub-image at a better native size or simplify the slot. Do not fake clarity by upscaling small components unless the manifest labels the resize and the visual is purely decorative.

## Final Delivery Discipline

Even if intermediate analysis is extensive, final user-facing output for this skill remains only:

1. `MEDIA:/absolute/path/to/poster.png`
2. One or two Chinese sentences explaining style/palette/layout and figure handling.
