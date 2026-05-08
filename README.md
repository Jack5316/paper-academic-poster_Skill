# paper-academic-poster

A Claude Code skill that transforms academic papers into visually striking vertical conference-grade posters using GPT Image 2 direct generation.

## Overview

This skill takes an academic paper (PDF, DOI, URL, pasted text, or extracted manuscript) and produces a single GPT Image 2 direct-generated vertical academic poster image. It handles the full workflow: paper retrieval, content analysis, visual triage, poster composition, and final delivery.

## Usage

Invoke this skill when a user asks for:
- 学术海报 / 论文海报
- Conference poster / research poster
- A0 poster
- 把论文做成海报
- Soulful poster / 设计感海报 / 特色锚点海报

## Key Features

- **Direct GPT Image 2 generation** — produces high-resolution (2416x3424) native PNG posters without local patching
- **Evidence-aware** — classifies visuals into evidence originals vs. concept redraws; preserves high-signal source materials
- **Academic style presets** — validated style for peer-reviewed papers (ivory + navy + brick-red palette, serif/sans-serif typography)
- **Chinese text handling** — enforces ≤14 character line breaks to prevent GPT Image 2 corruption
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
    ├── codex_direct_image_gen.py     # Direct Codex image generation helper
    ├── direct-provider-comparison.md
    ├── gpt-image-2-direct-reference-assets.md
    ├── hybrid-deterministic-composition.md
    ├── production-contract.md
    └── 4k-evidence-dense-posters.md
```

## Default Route

The default poster generation uses the Codex Responses direct call at native **2416x3424 portrait** resolution via the bundled `codex_direct_image_gen.py` helper. This produces ~7-9 MB native PNGs in 2-4 minutes.

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
4. Classify visuals before prompting — evidence vs. concept vs. atmosphere
5. Centerpiece belongs to what *only this paper demonstrates*, not widely-discussed themes
6. Chinese long-sentence rule: body text must be ≤14 characters per visual line

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
