# GPT Image 2 Sub-Image Generation and Reference Assets

Use this note when `paper-academic-poster` needs GPT Image 2 as a component generator inside the default divide-and-compose workflow, or when the user explicitly opts into a one-shot GPT Image 2 whole-poster preview.

## Core lesson

The default poster is not a single model-returned image. GPT Image 2 produces bounded sub-images: hero visuals, no-text atmosphere panels, icon sheets, stylized evidence backdrops, illustrative mockups, or low-text concept illustrations. The final poster is composed deterministically with local text, source crops, diagrams, and these generated components.

Preserved evidence-class originals are source assets for the final composition. Do not replace exact evidence with model-rendered approximations unless extraction is impossible and the panel is clearly labeled as an illustrative mockup.

## When to use

- A poster region needs visual richness that deterministic drawing would make too flat: hero art, background texture, editorial vignette, concept atmosphere, or icon family.
- An evidence-class visual cannot be extracted cleanly and a labeled high-fidelity mockup is acceptable.
- A user asks to compare GPT Image 2 providers for generated **sub-images**.
- A user explicitly says “GPT Image 2 一站式生成”, “全图生成”, “direct whole-poster”, or “不要本地填文字/排版”; in that case this note also covers the opt-in one-shot route.

## Material preparation

1. Extract PDF text and candidate visuals as usual.
2. Classify every candidate as evidence / concept / atmosphere before prompting.
3. Preserve selected evidence-class originals as source crops for final composition.
4. Convert concept/structure visuals into deterministic redraw specs when exact labels and arrows matter.
5. Use GPT Image 2 for sub-images that can tolerate stylization, especially those with no text or only large display labels.
6. Create clean crops or compact material boards only for sub-image prompts that genuinely need visual reference.
7. Keep a manifest of which visuals were preserved, redrawn, generated, or omitted as redundant.

## Sub-image prompt pattern

Use short English prompts with a precise slot role and no dense text:

```text
Create one poster component, not a full poster.
Component role: <hero / background / icon sheet / illustrative mockup / concept visual>.
Final slot size: <width>x<height> px inside an A0 portrait poster.
Use the attached reference only for visual structure/material cues.
No QR code, no watermark, no fake logos, no lorem ipsum.
Avoid small text. Leave clean negative space where local labels will be overlaid later.
Style: <palette, line weight, texture, perspective, mood>.
```

For Chinese papers, keep generated sub-image text to zero whenever possible. Render Chinese titles, labels, captions, and numeric claims locally during composition. If the sub-image must contain Chinese, use only a few large labels and verify them before using the asset.

For evidence mockups, include:

```text
This is an illustrative mockup panel, not a real screenshot.
Recreate the platform visual language: <Feishu / WeChat / terminal / web UI>.
Use only the specified large labels; avoid tiny body text.
Reserve a corner badge area for the local text label "示意图 / Illustrative Mockup".
```

## Hermes/Codex implementation note

Use the bundled helper script `references/codex_direct_image_gen.py` for GPT Image 2 sub-images. It calls Codex Responses' `image_generation` tool directly with `model=gpt-image-2`, explicit `size`, and `quality=high`, bypassing Hermes' built-in `image_gen` 1024x1536 size lock. The helper reuses Hermes' `_build_codex_client()` for OAuth only.

Invocation:

```bash
HERMES_AGENT_HOME="${HERMES_AGENT_HOME:-$HOME/.hermes/hermes-agent}"
HERMES_PY="$HERMES_AGENT_HOME/venv/bin/python3"
cd "$HERMES_AGENT_HOME"
"$HERMES_PY" "/path/to/paper-academic-poster/references/codex_direct_image_gen.py" \
    /path/to/subimage_prompt.txt \
    /path/to/subimage.png \
    1536x1024 \
    high
```

Choose size from the final slot, not from the whole poster. Common choices: `1536x1024` for wide panels, `1024x1536` for vertical panels, `2048x2048` for square icon/texture sheets, `2048x3072` or `2416x3424` only for large hero panels or explicit one-shot previews.

For GPT Image 2 generation with reference images, extend the helper or call Codex Responses directly attaching selected inputs as `input_image`. Save the returned image as an intermediate asset, inspect it, then place it into the deterministic final composition.

## Optional one-shot whole-poster route

Use only when the user explicitly asks for direct whole-poster/model-only authorship.

- Generate one complete vertical A0-style poster as a single GPT Image 2 image.
- Keep text short and accept that small text/evidence may be unreliable.
- Do not add local text or patches after generation if the user requested model-only authorship.
- If exact text, source fidelity, or print layout matters, recommend the default divide-and-compose route instead.

## QC checklist

- The sub-image matches its assigned slot and does not look like a complete poster unless the one-shot route was explicitly requested.
- Generated sub-images contain no unreadable fake text in areas that should be clean.
- Evidence-class originals are preserved as source crops unless the manifest marks a generated mockup as illustrative.
- Concept/structure visuals are deterministic redraws when exact labels/arrows matter.
- No QR code, fake logo, placeholder, lorem ipsum, large gibberish blocks, or watermark.
- Manifest states each generated sub-image's prompt path, provider/model, requested size, actual size, placement, and QC result.

## Pitfall

Do not use a one-shot GPT Image 2 poster as a background and then patch it locally. In divide-and-compose mode, generate components only; in one-shot mode, deliver the model image as-is and accept the trade-off.
