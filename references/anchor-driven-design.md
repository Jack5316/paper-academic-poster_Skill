# Anchor-Driven Adaptive Design Route

Load this reference whenever the poster brief leans on design quality rather than evidence density: explicit signals are 设计感 / 灵魂 / 特色锚点 / soulful poster / "不要模板感" / "像信息图杂志特稿那样" / "海报本身要好看", or any time the user clearly cares about how the poster feels.

This route is still divide-and-compose. Design decisions drive the region plan, generated sub-images, source crops, deterministic diagrams, palette, and hierarchy; final typography and layout are composed locally for fidelity.

## Hard Constraints

1. **Distinctive anchor first.** Identify at least 1-2 anchors: named system, real UI/dialogue/experiment evidence, unique dataset sample, original named term diagram, named-case process, or author-coined paradigm diagram.
2. **Anchor area is large.** The strongest anchor should occupy a dedicated section, visual center, or the largest figure slot; target at least 20% of the poster body unless the paper's structure clearly argues against it.
3. **Final poster is deterministic composition.** Use local text, source crops, deterministic diagrams, and generated sub-images. Do not use a full AI poster as the final canvas unless the user explicitly asks for one-shot model authorship.
4. **GPT Image 2 is a component generator.** Use it for hero visuals, atmosphere, icon sheets, stylized mockups, or other bounded regions. Avoid dense text inside generated sub-images.
5. **Native clarity is real.** Final export long edge should meet the requested delivery floor; for 4K use `2896x4096` or higher. Verify actual file dimensions.
6. **No silent non-GPT substitution for generated components.** If GPT Image 2 routes fail for a generated sub-image, report the boundary or ask before using another image model.

## Six-Phase Workflow

### Phase 1 — Paper Analysis

Extract:

- full title;
- author list;
- top-level affiliations;
- venue / journal / conference name;
- year;
- DOI / arXiv id / URL for manifest;
- abstract;
- author-claimed contributions;
- method or analytical model;
- key results with exact numbers, metrics, baselines, datasets;
- conclusion / implications;
- limitations / future work.

Classify the paper:

- `type`: theory / experimental / methodological / survey / position / dataset-or-resource.
- `length`: short (< 6 pages), medium (6-12 pages), long (12+ pages).
- `field`: CS-AI / Bio-Med / Physics-Chem / Math / Humanities / Social Science / Interdisciplinary.

Identifier hygiene:

- Allowed on poster: formal journal/conference name, ISSN / CN ID, official volume/issue, DOI when useful.
- Forbidden on poster: network-first placeholder pagination, preprint watermark bars, "Under review", "For peer review", line numbers, DOI placeholders, arXiv version ribbons.
- If official year is uncertain, use submission/acceptance/publication year only when source-supported; otherwise omit.

Distinctive anchor identification:

- Ask: what is irreplaceable about this paper? What can no one else in the same field claim?
- Anchor language must be concrete. Avoid generic "Framework / Method / Architecture" when a named system, case, dataset, transcript, or exact experiment exists.
- At least 1-2 hook highlights should point to the anchor with named, story-shaped, specific language.

### Phase 2 — Figure Triage

For every figure and table, decide a strategy:

| Class | Strategy |
|---|---|
| Diagram / framework / pipeline / architecture / concept figure | Redraw deterministically under unified poster style; preserve every key label, ordering, arrow, grouping |
| Data chart with exact numbers | Preserve original crop, or reconstruct deterministically only when source data is explicit |
| Observation data (microscopy, medical imaging, sample photo, qualitative result) | Preserve original crop |
| UI screenshot / dialog capture / experiment-scene photo / chat bubbles / terminal session | Preserve original crop; if extraction is impossible, create a high-fidelity generated mockup and label it "示意图 / Illustrative Mockup" locally |
| Small comparison table (<=5 rows, <=4 cols) | Re-typeset deterministically |
| Large benchmark table | Preserve original crop or omit |
| Important formula | Render deterministically |
| Atmosphere / metaphor / decorative visual | Generate as a sub-image if it sharpens the anchor |

Output a figure manifest listing each figure's strategy and final poster role.

### Phase 3 — Adaptive Design Decisions

Visual style:

- Theory / mathematical: minimalist geometric, whitespace, serif title, precise diagrams.
- Experimental / engineering / AI: modern infographic, technical blueprint, clear hierarchy.
- Survey / position: editorial feature, strong conceptual map.
- Bio / Med / life science: scientific illustration or evidence-led panel, depending on the paper tone.
- Dataset / benchmark: data-dashboard with evidence hierarchy.

Palette:

- Derive the palette from the paper's content emotion, source figures, and audience expectation, not from a fixed field-color mapping.
- Output 3-5 color tokens with HEX values and roles: dominant, secondary, accent, background, text.
- Check contrast for title, headings, body, evidence captions, and dark cards.

Information density:

- Short paper: classic-complete.
- Medium paper: balanced.
- Long paper: anchor + selected argument path + evidence map.
- Survey: main structure diagram + key branches.

Layout:

- 3-column classic for full coverage.
- 2-column + central hero figure for method papers.
- Asymmetric visual center for a dramatic anchor.
- Top hero + multi-column below for story-shaped papers.
- Evidence wall when source artifacts are the contribution.

### Phase 4 — Region and Asset Plan

Create a region plan before generating:

```text
Region: <name>
Role: <why this region matters>
Strategy: local-text / source-crop / deterministic-diagram / generated-subimage / mixed-panel
Inputs: <paper section, figure ids, extracted crops, prompt path>
Final placement: <approximate x/y/w/h or grid area>
QC risk: <text / evidence / low-res / clutter / hallucination>
```

Generated sub-images should be bounded: hero art, atmosphere, icon sheet, stylized evidence backdrop, connector visual, or illustrative mockup. They should not carry exact body text or dense labels.

### Phase 5 — Composition

Build the final poster locally:

- A0/A-series portrait ratio, typically `2480x3508` or higher.
- Local fonts for all Chinese and English text.
- Deterministic headers, captions, labels, cards, tables, diagrams, and footers.
- Source crops placed at inspected resolution.
- Generated sub-images placed as components, not as the whole page.
- Stable spacing, measured margins, and consistent line weights.

### Phase 6 — Self-Audit

Every item must pass:

- Title, authors, affiliation spelled correctly.
- 3-5 hook-style highlights are concrete, not abstract regurgitation.
- Distinctive anchor is visually prominent and not buried in abstract theory.
- Evidence-class originals are preserved or generated mockups are clearly labeled.
- Deterministic diagrams preserve source logic.
- Layout is portrait, ratio close to A-series.
- No gibberish, no spelling errors, no hallucinated numbers.
- Color and typography match the chosen design direction.
- No QR code, placeholder boxes, watermark, or fake logos.
- No preprint pagination, review watermark, or line numbers.
- Visual hierarchy is clear at phone preview and 50% zoom.
- Final long edge meets requested resolution and is verified by file inspection.

Severe issues: fix the affected region and re-export. Regenerate only the failed generated sub-image unless the overall region plan is wrong.

## Locked Adaptive Decisions

Style, density, palette, layout, typography, ratio, region strategy, and redraw-vs-preserve decisions are derived by this skill from the paper's content. Ask the user only when:

- No source can be retrieved.
- Multiple papers match an ambiguous title.
- Choosing among equally valid evidence sets would change the paper's scientific message.
- The user explicitly requires one-shot model-only authorship, which conflicts with exact text/evidence fidelity.

## Anti-Patterns

Must do:

- Read enough of the paper to ground every poster claim before designing.
- Identify and visually dominate at least 1-2 distinctive anchors.
- Triage figures: redraw concept; preserve data/observation/evidence; mockup-redraw evidence only when extraction is impossible and label it.
- Derive palette from content emotion, not from field stereotypes.
- Compose final A0 portrait locally with exact text and source-aware evidence handling.
- Self-audit before delivery.

Must not do:

- Hardcode "field -> color" mapping.
- Add QR code, DOI bottom bar, URL watermark unless explicitly requested.
- Include network-first placeholder pagination or peer-review markings.
- Replace the paper's distinctive anchor with generic abstract boxes.
- Fabricate data, authors, conclusions, dialogue, or limitations.
- Put dense exact text inside generated sub-images.
- Use a full generated poster as a base layer and patch it locally.
- Silently switch to non-GPT Image 2 models for generated components.

## Final Delivery

Show the user only:

1. The poster image: `MEDIA:/absolute/path/to/poster.png`.
2. A 1-2 sentence Chinese design note covering the chosen visual style, palette, layout, anchor handling, and figure handling.
