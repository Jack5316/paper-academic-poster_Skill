# 4K Evidence-Dense Academic Posters

Use this reference when the user explicitly asks for 4K resolution, stronger information density, or original evidence visuals to be visible in the poster. It extends the default direct GPT Image 2 route; deterministic composition remains opt-in.

## Trigger signals

- User says the poster is not dense enough to cover the whole paper.
- User asks for `4K`, `A0 print`, or a specific high-resolution output.
- User says screenshots, dialogue captures, data visuals, or other evidence-class originals from the paper must appear as evidence.
- The paper is Chinese-text-heavy or contains exact numbers, screenshots, tables, or diagrams that need careful prompt/material selection.

## Direct GPT Image 2 default

By default, classify visuals before prompting: preserve selected evidence-class originals as reference/material `input_image` assets, convert framework/pipeline/architecture diagrams into redraw instructions, and omit redundant source diagrams when the poster already redraws their logic. 4K/high-density means higher native clarity and better argument coverage, not blanket visual inclusion. Ask for one complete native-large portrait poster, preferably `2416x3424` for A-series-ish output or `2160x3840` for 4K portrait when the route accepts it, and after generation only resize the whole image if needed and allowed by the active route. Do not add local labels, local evidence galleries, deterministic text, or screenshot overlays. If this direct route fails QC, regenerate with GPT Image 2 direct mode or ask before changing routes.

## Deterministic exception route

Use this exception route only when the user explicitly wants 4K, density, and source evidence fidelity through local deterministic composition, or authorizes local composition after direct GPT Image 2 attempts fail QC.

1. Keep GPT Image 2 for no-text visual atmosphere only. Prompt: `no words, no letters, no QR code, no logos, no watermark`.
2. Build the full poster deterministically at true A-series portrait ratio. For 4K delivery, use `2896×4096` px (ratio ≈ 0.707, close to 841:1189) or higher.
3. Extract/crop evidence-class originals with PyMuPDF/page renders or embedded images when available. Convert concept/structure diagrams into deterministic redraws only in this explicit deterministic exception route; otherwise keep them as redraw instructions.
4. Create a contact sheet of crops and visually inspect before composition. If a crop clips a figure/caption, redo the crop before rendering.
5. Use a high-density multi-column layout rather than a sparse AI-poster layout. Include:
   - metadata + research question;
   - literature/problem context;
   - method or conceptual framework;
   - key contribution/argument flow;
   - major results/sections with exact numbers;
   - risks/limitations/governance implications;
   - conclusion boundaries/future work;
   - evidence-to-claim mapping.
6. Add a dedicated evidence gallery with all retained evidence-class originals, labeled by figure number/source and short caption.
7. Summarize each evidence asset nearby; do not rely on tiny embedded screenshots as the only place where key claims are readable.
8. Export both `poster.png` and optionally `poster.pdf`; write `manifest.json` with resolution, route boundary, source PDF, evidence assets, and QC status.

## QC checklist additions

- Verify actual image dimensions with PIL or equivalent; do not rely on text printed inside the poster.
- Confirm portrait orientation and A0/A-series ratio (`width/height ≈ 0.707`).
- Confirm all required evidence-class originals are visibly present and labeled.
- Confirm concept/structure figures are redrawn or omitted as redundant; do not duplicate original diagrams beside their redraws.
- Confirm density increased by adding substantive content, not just smaller fonts.
- Check for empty card space, clipped footers, text overlap, and evidence thumbnails too small to interpret.
- If vision review misreports orientation because of platform preview, trust measured pixel dimensions but still inspect the rendered file visually.

## Pitfall from session

A sparse full GPT Image 2 poster may look attractive but fail three user expectations: true 4K delivery, visible evidence-class originals, and coverage of the full argument. For evidence-dense direct posters, keep the result as one GPT Image 2 image but improve the prompt, classified evidence crops, concept-redraw instructions, native size/provider choice, and regeneration strategy. Use deterministic layout only when the user explicitly prioritizes source-fidelity composition over pure AI direct generation.
