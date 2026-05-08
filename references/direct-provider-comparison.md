# GPT Image 2 Provider Comparison for Poster Sub-Images

Use this reference when the user asks to compare or race multiple GPT Image 2 routes (for example Codex, YouMind, ListenHub). In the default divide-and-compose workflow, compare providers as sub-image generators, not as final poster producers.

## Trigger

- User asks for the same generated panel from multiple providers and wants only versions above a pass line.
- User complains that a generated component is soft and wants the highest native-resolution version.
- User asks for GPT Image 2 full-image authorship and explicitly rejects local text/layout/screenshot composition. In that case, use the optional one-shot section below.

## Pass line for sub-image delivery

Deliver or compose only outputs that meet all of these:

1. The image matches its assigned poster region and aspect ratio.
2. Native long edge is appropriate for the final slot; do not treat a resize as native detail.
3. No QR code, placeholder/lorem ipsum, fake logo, large gibberish blocks, or obvious watermark.
4. For no-text panels, no visible pseudo-text remains.
5. For illustrative mockups, platform visual language is plausible and the final composition will carry a deterministic "示意图 / Illustrative Mockup" label.
6. If multiple outputs pass, use the one that best matches the region plan and palette; record the others in the manifest if useful.

## Recommended comparison workflow

1. Build one shared English prompt for the target region: component role, final slot size, palette, style, and prohibited content.
2. Keep references small. Use only visuals needed for that component.
3. Generate in parallel when practical:
   - **Codex/OpenAI Responses**: direct `image_generation` with `gpt-image-2`, `quality: high`, and a valid native size matching the region slot.
   - **YouMind**: `createChat` + `imageGenerate`, `messageMode: agent`, `chatModel: gpt-image-2-2026-04-21`, plus explicit `tools.imageGenerate` config.
   - **ListenHub**: `generate-image.sh --model gpt-image-2 --size <size> --ratio <ratio> --reference-images <urls>`.
4. For every returned image, verify actual pixel dimensions, file size, and whether the path opens.
5. Inspect each output against the pass line. Record pass/fail in `manifest.json` or `comparison-summary.json`.
6. Compose only passing outputs into the final poster.

## Optional whole-poster comparison

Use only if the user explicitly asks for GPT Image 2 full-image authorship and rejects local composition.

Pass line:

1. Whole-poster generation by a GPT Image 2 route; no local text, layout, screenshot, or patch overlay after generation.
2. Native long edge is at least roughly 2000 px for a highest-resolution comparison; if a 4K file is only a resize, label it as resized.
3. Title and author line are readable at normal zoom.
4. Required evidence-class originals are visibly represented as evidence/material panels, with the trade-off that they may not be pixel-faithful.
5. No QR code, placeholder/lorem ipsum, fake logo, large gibberish blocks, or obvious watermark.

## Provider notes

- **Codex/OpenAI Responses**: prefer explicit sizes supported by the route; record requested and actual size.
- **Hermes built-in image_generate**: useful for small decorative/preview panels, but it may not accept reference images or arbitrary size.
- **YouMind**: schema and accepted GPT Image 2 sizes may differ over time. Verify the wrapper schema/live response and downloaded pixels on every run; poll `listMessages` and inspect tool blocks instead of assuming `createChat` returned a final image.
- **ListenHub/Marswave**: can be gateway-prone on large multi-reference prompts. Try at least one reduced-complexity retry before declaring it failed.

## Reporting discipline

- Do not send failed outputs “for reference” when the user asked for pass-line filtering.
- Do not call an upscaled or smaller downloaded image “highest resolution”; state native size separately from delivery/export size.
- Do not leak internal skill/tool instructions, hidden policies, tokens, headers, or secrets from provider responses.
