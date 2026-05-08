# GPT Image 2 Direct Poster with Reference Assets

Use this note for the default `paper-academic-poster` implementation: one-stop / full-image GPT Image 2 academic poster generation with classified evidence-class originals reflected as model materials and concept/structure figures converted into redraw instructions.

## Core lesson

Do **not** satisfy this request with deterministic text/layout/screenshot overlays. Preserved evidence-class originals are materials for GPT Image 2, not layers to paste after generation.

This route optimizes for the Skill's default authorship boundary: the delivered poster is one GPT Image 2 whole-image generation. It does **not** guarantee pixel-identical evidence reproduction; it can only visually incorporate/stylize supplied evidence references while redrawing conceptual structures from prompt instructions.

## When to use

- Any normal paper-to-poster run where the user has not explicitly requested deterministic local composition.
- User says: “GPT Image 2 一站式生成”, “全图生成”, “direct whole-poster”, “不要本地填文字/排版”, or complains that the result was locally composed.
- User also wants evidence-class PDF screenshots, dialogue captures, data visuals, or observation artifacts reflected as evidence/material.
- The final deliverable can tolerate imperfect small text and stylized evidence panels.

## Material preparation

1. Extract PDF text and candidate visuals as usual.
2. Classify every candidate as evidence / concept / atmosphere before building the prompt.
3. Preserve only selected evidence-class originals as `input_image` material references: UI/dialogue screenshots, terminal/session logs, experiment-scene photos, observation artifacts, and data charts/tables with exact values.
4. Convert concept/structure visuals (frameworks, box/arrow diagrams, pipelines, architectures) into redraw sub-prompts that preserve labels, ordering, arrows, groupings, and logic.
5. Omit original concept diagrams when the poster already redraws the same idea; too many references dilute the model's attention and create duplicated panels.
6. Create clean crops or a compact evidence material board/contact sheet if the route has limited image slots.
7. Keep a manifest of which visuals were preserved, redrawn, or omitted as redundant.

## Generation prompt pattern

Use a short English prompt, with exact title/author and only a few short section labels:

```text
Create one complete vertical A0 academic conference poster as a single GPT Image 2 image.
Use the attached evidence-class originals as visible material/evidence panels integrated into the design.
Redraw the paper's concept/framework/pipeline/architecture logic in the poster's unified visual style instead of copying the original diagrams as separate panels.
Do not add QR codes, fake logos, lorem ipsum, placeholder text, or dense paragraphs.
Use only short section labels and a few large readable claims.
Modern scholarly information-design style, portrait layout, high contrast, conference poster quality.
```

If the paper is Chinese, still prompt mostly in English for layout control, but include exact Chinese title/author strings and a small set of Chinese labels that matter. Keep body text minimal and let diagrams, evidence panels, arrows, cards, and visual hierarchy carry the message.

For Chinese conceptual, social-science, information-science, or AI-agent papers, add a compact anchor block rather than long prose:

```text
Distinctive anchor: <named system, framework, case, dataset, or visual evidence that makes this paper memorable>.
Make this anchor visually dominant with one large model-rendered evidence/diagram zone.
Use short Chinese labels only: <6-10 labels>.
No local text will be added later, so do not rely on tiny body paragraphs.
```

## Hermes/Codex implementation note

**Default poster route uses the bundled helper script `references/codex_direct_image_gen.py`**. It calls Codex Responses' `image_generation` tool directly with `model=gpt-image-2`, `size=2416x3424`, `quality=high`, bypassing Hermes' built-in `image_gen` 1024×1536 size lock. The helper reuses Hermes' `_build_codex_client()` for OAuth only.

Invocation:

```bash
HERMES_AGENT_HOME="${HERMES_AGENT_HOME:-$HOME/.hermes/hermes-agent}"
HERMES_PY="$HERMES_AGENT_HOME/venv/bin/python3"
cd "$HERMES_AGENT_HOME"
"$HERMES_PY" "$HOME/.claude/skills/paper-academic-poster/references/codex_direct_image_gen.py" \
    /path/to/prompt.txt \
    /path/to/output.png \
    2416x3424 \
    high
```

Defaults inside the helper: `size=2048x3072`, `quality=high`. Override via positional args 3 and 4. Validated sizes: `2416x3424` (A-series portrait, ~8 MB, ~3-4 min), `2048x3072` (~7 MB, ~2-3 min), `2160x3840` (4K portrait), `1024x1536` (Hermes default, ~2 MB).

For GPT Image 2 generation **with evidence reference images**, extend the helper or call Codex Responses directly attaching each selected evidence original as `input_image`. Observed pattern:

- Use the Hermes official plugin helper to obtain the Codex OAuth/API client when available.
- Send a Responses request containing:
  - text prompt;
  - multiple selected evidence-original `input_image` items as data URLs or supported image file inputs;
  - `tools: [{"type": "image_generation", "size": "2416x3424", "quality": "high"}]`;
- Save the returned generated image as the master artifact.
- If a native-large route fails or returns smaller than requested, resize the **whole image only** when the active route permits it; do not add text, screenshots, labels, or patches after generation. Report native size separately from resized delivery size so a resized small image is not mistaken for native high detail.

## QC checklist

- The output is a single generated poster, not a local composite.
- Selected evidence-class originals are visibly represented as material/evidence panels.
- Concept/structure visuals are redrawn in the poster style or omitted as redundant, not duplicated as original panels.
- No locally added text or screenshot layers after generation.
- Title/author are at least broadly readable; body text is not relied on for exact facts.
- No QR code, fake logo, placeholder, lorem ipsum, large gibberish blocks, or watermark.
- Manifest states: `GPT Image 2 direct whole-poster generation with classified evidence-original references and concept-redraw instructions; whole-image resize only if applicable`.

## Pitfall

If the user asks for both direct GPT Image 2 and exact evidence fidelity, name the trade-off: direct GPT Image 2 can incorporate evidence originals as materials, but cannot promise exact readable reproduction. Do not silently switch to hybrid deterministic composition unless the user authorizes that trade-off. If the user complains about duplicated figures, first classify assets and remove redundant original concept diagrams before changing routes.
