# paper-academic-poster

A Claude Code skill that transforms academic papers into visually striking vertical conference-grade posters using a divide-and-compose production workflow.

## Overview

This skill takes an academic paper (PDF, DOI, URL, pasted text, or extracted manuscript) and produces a composed vertical academic poster image. It handles the full workflow: paper retrieval, content analysis, visual triage, region planning, component generation/redraw, deterministic poster composition, QC, and final delivery.

## Usage

Invoke this skill when a user asks for:
- 学术海报 / 论文海报
- Conference poster / research poster
- A0 poster
- 把论文做成海报
- Soulful poster / 设计感海报 / 特色锚点海报

## Key Features

- **Divide-and-compose default** — plans semantic poster regions, produces each component with the right method, then composes a deterministic final A0-ratio canvas
- **Evidence-aware** — classifies visuals into evidence, concept, and atmosphere; preserves high-signal source crops when fidelity matters
- **Deterministic text and diagrams** — renders titles, authors, captions, numeric claims, tables, and concept diagrams locally for reliability
- **GPT Image 2 sub-images** — uses GPT Image 2 for bounded hero visuals, no-text atmosphere panels, icon sheets, illustrative mockups, and stylized components
- **One-shot option** — still supports direct whole-poster GPT Image 2 generation when the user explicitly asks for 一站式 / direct whole-poster / model-only authorship
- **Multiple quality tiers** — supports standard, 4K evidence-dense, and anchor-driven design variants

## Project Structure

```
├── SKILL.md                           # Main skill definition
├── agents/
│   └── openai.yaml                   # Agent configuration
└── references/
    ├── academic-paper-style.md
    ├── academic-paper-style-prompt-template.md
    ├── anchor-driven-design.md
    ├── codex_direct_image_gen.py     # GPT Image 2 sub-image helper
    ├── direct-provider-comparison.md
    ├── gpt-image-2-direct-reference-assets.md
    ├── hybrid-deterministic-composition.md
    ├── production-contract.md
    └── 4k-evidence-dense-posters.md
```

## Default Route

The default route is **divide-and-compose**:

1. Retrieve/extract the paper text, figures, tables, screenshots, and metadata.
2. Plan poster regions such as header, context, method/framework, anchor, evidence/results, implications, and footer.
3. Assign each region a strategy: `local-text`, `source-crop`, `deterministic-diagram`, `generated-subimage`, or `mixed-panel`.
4. Generate only bounded GPT Image 2 sub-images when they improve the design.
5. Compose the final poster deterministically with local fonts, exact text, source crops, diagrams, and generated components.
6. Export PNG/PDF and record a manifest with route, assets, dimensions, and QC.

For one-shot direct whole-poster generation, the user must explicitly request GPT Image 2 一站式生成, direct whole-poster, or model-only authorship.

## Routing Boundaries

| Skill | Use Case |
|-------|----------|
| `paper-academic-poster` | Paper → single vertical poster |
| `paper-explainer` | Long-form paper explanations |
| `infographic-composer` | Generic infographics (not paper-anchored) |
| `ppt-image-pages` | 16:9 slide/page images |

## Non-Negotiable Rules

1. Read enough of the paper to supply accurate prompt facts before generating
2. Preserve exact numbers, dates, model names, metrics, and qualifiers
3. Do not invent results, institutions, or datasets
4. Classify visuals before production — evidence vs. concept vs. atmosphere
5. Centerpiece belongs to what *only this paper demonstrates*, not widely-discussed themes
6. Render Chinese and exact text locally whenever possible; generated sub-images should avoid dense text

## Style

Default style: **academic_paper** — validated for peer-reviewed papers with:
- Ivory + navy + brick-red palette (no gold/coral fields)
- Serif title + sans-serif body
- Prose abstract top-left, concept-shift diagram top-right
- Centerpiece = paper's unique exhibit
- 4 navy impact cards at bottom
- ORCID footer

## Requirements

- Hermes agent venv with Codex access
- `HERMES_AGENT_HOME` set to Hermes agent directory (defaults to `~/.hermes/hermes-agent`)
- Local rendering stack suitable for deterministic composition, such as HTML/CSS, SVG, PIL, Cairo, or equivalent
