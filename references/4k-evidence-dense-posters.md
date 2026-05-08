# 4K Evidence-Dense Academic Posters

Use this reference when the user explicitly asks for 4K resolution, stronger information density, full-paper coverage, A0 print, or original evidence visuals to be visible in the poster. It extends the default divide-and-compose route.

## Trigger signals

- User says the poster is not dense enough to cover the whole paper.
- User asks for `4K`, `A0 print`, `PDF`, or a specific high-resolution output.
- User says screenshots, dialogue captures, data visuals, or other evidence-class originals from the paper must appear as evidence.
- The paper is Chinese-text-heavy or contains exact numbers, screenshots, tables, or diagrams that need careful rendering.

## High-resolution divide-and-compose route

4K/high-density means higher native clarity and better argument coverage, not blanket visual inclusion or tiny fonts.

1. Build the final poster at true A-series portrait ratio. For 4K delivery, use `2896x4096` px (ratio approx. 0.707, close to 841:1189) or higher. Verify the actual final dimensions.
2. Classify visuals before production: preserve selected evidence-class originals as source crops, redraw framework/pipeline/architecture diagrams deterministically, and omit redundant source diagrams when the poster already redraws their logic.
3. Create a contact sheet of candidate crops and inspect it before composition. If a crop clips a figure/caption, redo the crop before rendering.
4. Increase density with substantive content:
   - metadata + research question;
   - literature/problem context;
   - method or conceptual framework;
   - key contribution/argument flow;
   - major results/sections with exact numbers;
   - risks/limitations/governance implications;
   - conclusion boundaries/future work;
   - evidence-to-claim mapping.
5. Add a dedicated evidence gallery only when evidence is central. Label every retained evidence asset by figure number/source and short caption.
6. Summarize each evidence asset nearby; do not rely on tiny embedded screenshots as the only place where key claims are readable.
7. Use GPT Image 2 only for sub-images that benefit from visual generation: no-text atmosphere, hero illustration, icon sheets, stylized dividers, or illustrative mockups. Do not ask GPT Image 2 to render dense tables or exact Chinese text.
8. Export both `poster.png` and optionally `poster.pdf`; write `manifest.json` with resolution, route boundary, source PDF, evidence assets, generated sub-images, and QC status.

## QC checklist additions

- Verify actual image dimensions with PIL or equivalent; do not rely on text printed inside the poster.
- Confirm portrait orientation and A0/A-series ratio (`width/height` approx. `0.707`).
- Confirm all required evidence-class originals are visibly present and labeled.
- Confirm concept/structure figures are redrawn or omitted as redundant; do not duplicate original diagrams beside their redraws.
- Confirm density increased by adding substantive content, not just smaller fonts.
- Check for empty card space, clipped footers, text overlap, and evidence thumbnails too small to interpret.
- Verify local text remains readable in phone/Telegram preview and at 50% zoom.
- If a generated sub-image is soft, regenerate only that sub-image or reduce its visual role; do not upscale a small full poster and call it 4K.

## Pitfall

A sparse whole-image AI poster may look attractive but fail three user expectations: true 4K delivery, visible evidence-class originals, and coverage of the full argument. For evidence-dense posters, keep the final artifact as a deterministic composition and improve region planning, crop quality, concept redraws, native export size, and component-level QC.
