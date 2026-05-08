# Hybrid Deterministic Poster Composition Notes

Use these notes only when the user explicitly requests or authorizes local deterministic/hybrid composition for exact text, exact layout, PDF export, or source-faithful evidence reproduction. Dense claims, Chinese text, exact numbers, or evidence figures are no longer enough by themselves to leave the default GPT Image 2 direct route.

Scope boundary: do not use this hybrid deterministic route for normal paper-to-poster requests. Use the direct GPT Image 2 route in `production-contract.md`: attach source images as references, generate one complete poster, and only resize the whole generated image if 4K delivery is needed and the active route allows it. Enter this file only after explicit user authorization for local composition.

## When to use

- User asks for a locally composed, source-faithful, exact-text academic poster.
- User asks for print/PDF production where deterministic text/evidence fidelity outranks GPT Image 2 direct authorship.
- Direct GPT Image 2 attempts fail QC and the user authorizes switching to deterministic/hybrid composition.

## Adaptive Chinese conceptual poster design pattern

Use this pattern inside the hybrid/deterministic family when the paper is concept-heavy and Chinese-text-heavy, especially for information science, AI agents, workflow/system papers, or papers whose strongest visual evidence is architecture diagrams, pipelines, screenshots, tables, or conceptual frameworks. Treat the pattern as a design discipline, not a template.

- Story hierarchy is adaptive: first decide what the paper is really about, what contrast or transformation makes it memorable, and which evidence should become the visual anchor. Only then choose layout.
- Possible rhythms include formal conference poster, case anatomy, evidence wall, conceptual before→after, pipeline dissection, or magazine-style feature. Do not force title-band / framework / case-block / cards if another structure better serves the paper.
- Formal metadata, framework contrast, case anatomy, and impact cards are optional ingredients. Use them when they clarify the thesis; omit or rearrange them when they dilute the design.
- Crop and curate ruthlessly: select 2–4 high-value evidence assets at most for a single poster unless the user explicitly requests density. Enlarge what matters, remove margins/noise, and pair evidence with a short interpretive claim.
- For concept diagrams such as “三要素 → 四要素”, redraw deterministically only after understanding the logic. Make it visually expressive but source-faithful.
- Aesthetic discipline matters: maintain a coherent palette, type rhythm, icon style, line weight, and whitespace. Avoid generic pastel dashboards, rigid templates, ornamental backgrounds, and mechanically copied layouts.
- If using GPT Image 2 for a no-text background, atmosphere panel, or design exploration, compare available routes when practical. YouMind is acceptable and may be preferred when it gives sharper or more poster-like native results; final choice must be based on inspected output quality, not provider habit.

## Proven route

1. Extract PDF text and page renders with PyMuPDF.
2. Create a contact sheet for page renders and extracted images; inspect with vision/OCR to identify figure numbers, captions, and whether each asset is evidence vs concept.
3. Use GPT Image 2 only for a no-text atmosphere/background or hero visual. Prompt must explicitly say no words, no letters, no QR code, no logos, no watermark.
4. Build the full A0-ratio poster deterministically (e.g., PIL/SVG/HTML):
   - A0 canvas ratio: 841:1189; delivery PNG can be 2480×3508 or higher. If the user asks for 4K, use an actual 4K long edge such as 2896×4096 px and verify it from the saved file.
   - Use local fonts for all Chinese/English text.
   - Draw concept diagrams with explicit nodes/arrows copied from the source logic.
   - Insert evidence screenshots/tables/photos from original crops; do not recreate them with image generation.
5. Write a manifest with source boundary, paper metadata, route/model, evidence assets used, numeric-claim anchors, output files, and QC status.
6. Run vision/OCR QC on the rendered poster, not only the source PDF.

## QC pitfalls found in practice

- Text drawn over a transparent/light title box can look blank to vision reviewers even when technically present; prefer higher-contrast filled panels for key claims.
- Long one-line footer or quality-gate text can appear clipped; wrap it inside its panel with explicit max width.
- Tool/brand names must be normalized after deterministic rendering (e.g., `OpenClaw`, not `Openclaw`).
- Evidence thumbnails may be too small to read; if used as proof thumbnails, label them as source evidence and summarize the claim nearby. For source-PDF screenshots explicitly requested by the user, include a dedicated evidence gallery plus an evidence-to-claim mapping, not just decorative thumbnails.
- For adaptive Chinese conceptual posters, both tiny unreadable thumbnails and oversized decorative screenshots are failure modes: crop fewer assets, enlarge only what advances the thesis, and summarize the evidence nearby.
- Image-generation prompts saying “no words” still need output inspection; generated backgrounds may introduce pseudo text/logos.
- Phone-preview QC: view the rendered poster at roughly 50% scale or on the delivery surface. The poster’s chosen hierarchy must still be evident: title/topic, central argument, main visual/evidence anchor, and key headings should be readable without deep zoom.
- If the final image looks soft, do not hide behind “4K” labels; inspect native dimensions and try a clearer GPT Image 2 provider/size or deterministic export path.

## Final delivery discipline

Even if intermediate analysis is extensive, final user-facing output for this skill remains only:

1. `MEDIA:/absolute/path/to/poster.png`
2. One or two Chinese sentences explaining style/palette/layout and figure handling.
