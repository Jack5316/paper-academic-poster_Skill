# Direct GPT Image 2 Provider Comparison for Academic Posters

Use this reference when the user asks to compare or race multiple GPT Image 2 routes (for example Codex, YouMind, ListenHub) for a one-stop full-poster academic image with classified evidence originals and concept-redraw instructions.

## Trigger

- User asks for the same poster from multiple providers and wants only versions above a pass line.
- User complains that a 4K delivery is only an upscaled small image and wants the highest native resolution / sharper zoom behavior.
- User explicitly wants GPT Image 2 full-image authorship and rejects local text/layout/screenshot overlays.

## Pass line for delivery

Deliver only outputs that meet all of these:

1. Whole-poster generation by a GPT Image 2 route; no local text, layout, screenshot, or patch overlay after generation.
2. Native long edge is at least ~2000 px for a “highest resolution” comparison; if a 4K file is only a resize, label it as resized and do not treat it as native high-detail.
3. Title and author line are readable at normal zoom.
4. Required preserved evidence-class originals are visibly represented as evidence/material panels; concept/structure figures may be redrawn instead of copied.
5. No QR code, placeholder/lorem ipsum, fake logo, large gibberish blocks, or obvious watermark.
6. If multiple outputs pass, send all passing images with producer labels; if only one passes, send only that image and briefly list why the others failed.

## Recommended comparison workflow

1. Build one shared English prompt with exact Chinese title/author strings, the same classified evidence-original set, and the same concept-redraw instructions.
2. Keep reference count small. Use a material board plus 2-3 representative evidence crops when the route limits references.
3. Generate in parallel when possible:
   - **Codex/OpenAI Responses**: direct `image_generation` with `gpt-image-2`, `quality: high`, a valid native-large portrait size such as `2416x3424` or `2160x3840`, and attached evidence-original `input_image` data URLs.
   - **YouMind**: `createChat` + `imageGenerate`, `messageMode: agent`, `chatModel: gpt-image-2-2026-04-21`, plus explicit `tools.imageGenerate` config.
   - **ListenHub**: `generate-image.sh --model gpt-image-2 --size 4K --ratio 2:3 --reference-images <urls>`.
4. For every returned image, verify with PIL or equivalent: actual pixel dimensions, file size, and whether the path opens.
5. Vision/OCR inspect each output against the pass line. Record pass/fail in `manifest.json` or `comparison-summary.json`.
6. Final response should include only passing `MEDIA:` images plus a compact comparison note.

## Observed provider quirks from the OpenClaw poster run

- **Codex/OpenAI Responses**: request current official GPT Image 2 flexible native sizes before considering whole-image resize. Prefer `2416x3424` for A-series-ish portrait or `2160x3840` for 4K portrait when accepted; record requested and actual size.
- **Hermes built-in image_generate**: useful for no-reference whole images, but it does not accept reference images or arbitrary size; use direct Codex Responses when PDF screenshots must be supplied as materials.
- **YouMind**: schema and accepted GPT Image 2 sizes may differ over time. Verify the wrapper schema/live response and downloaded pixels on every run; poll `listMessages` and inspect tool blocks instead of assuming `createChat` returned a final image.
- **ListenHub/Marswave**: `generate-image.sh` accepts `--size 4K`, `--ratio 2:3`, `--reference-images`, and `--model gpt-image-2`, but this run saw 504/service-busy or `Image generation failed` for 4K multi-reference, board-only, URL-in-prompt, and no-reference attempts. Treat it as a valid fallback route, but do not report it as failed until at least one reduced-complexity retry has been tried.

## Reporting discipline

- Do not send failed outputs “for reference” when the user asked for pass-line filtering.
- Do not call an upscaled or smaller downloaded image “highest resolution”; state native size separately from delivery/export size.
- Do not leak internal skill/tool instructions, hidden policies, tokens, headers, or secrets from provider responses.
