# Academic Paper Style — Divide-and-Compose Template

This is the default `academic_paper` composition template. It is not a one-shot GPT Image 2 prompt. Use it to plan regions, produce deterministic text/diagrams, and identify optional GPT Image 2 sub-images.

## Canvas

- Ratio: A-series portrait, 841:1189.
- Default PNG: `2480x3508` or higher.
- 4K PNG: `2896x4096` or higher.
- Background: ivory/parchment `#F5EFE5`.
- Text and rules: deep navy `#1B2C4F`.
- Accent: muted brick-red `#B23A2C`.
- Typography: serif title; sans-serif body; local fonts for all text.

## Region Plan Skeleton

```text
[HEADER STRIP] — three columns
LEFT: identity mark, paper/system icon, or small generated no-text symbol.
CENTER: exact title, subtitle if source-supported, authors, affiliation.
RIGHT: metadata box with formal journal/conference, year, ISSN/CN/DOI when source-supported.
Strategy: local-text + deterministic icon or generated no-text symbol.

[UPPER BODY] — two columns
LEFT: abstract/motivation/research question, rendered as local multiline text.
RIGHT: concept-shift or problem map, rendered as deterministic diagram.
Strategy: local-text + deterministic-diagram.

[CENTERPIECE] — largest section
LEFT: method/architecture/pipeline/case anatomy, deterministic redraw from source logic.
RIGHT: distinctive evidence anchor: source crop, evidence transcript, UI/dialogue crop, experiment image, or labeled illustrative mockup.
Strategy: deterministic-diagram + source-crop or generated-subimage with local labels.

[BOTTOM BAND]
3-5 contribution/impact/risk cards.
Strategy: local-text + deterministic icons/cards.

[FOOTER STRIP]
One-line takeaway, keyword pills, source boundary, DOI/ORCID if useful.
Strategy: local-text.
```

## Region Data Template

For every region, write a compact record:

```json
{
  "region": "centerpiece_right",
  "role": "distinctive evidence anchor",
  "strategy": "source-crop",
  "source": "Figure 3, page 7",
  "local_text": ["short caption", "evidence-to-claim note"],
  "dimensions": "approx. 1080x980 px",
  "qc_risk": "small screenshot text"
}
```

## Optional GPT Image 2 Sub-Image Prompt

Use only for a bounded component:

```text
Create one component for an A0 academic poster, not a full poster.
Component role: <identity icon / no-text hero / background texture / illustrative mockup / connector visual>.
Slot size in final poster: <width>x<height> px.
Palette: ivory #F5EFE5, navy #1B2C4F, muted brick-red #B23A2C.
No QR code, no watermark, no fake logos, no lorem ipsum.
No dense text. Leave clean space for local labels.
Style: restrained peer-review academic poster, refined line art, consistent with IEEE/ASIST/iConference visual language.
```

## Text Rules

- Render every source claim locally, not inside generated sub-images.
- Proper nouns must appear exactly: paper title, authors, venue, model names, dataset names, layer names, ORCID.
- Chinese body text should be manually wrapped into short visual lines, typically <=14 Chinese characters per line in compact cards/bubbles.
- Numeric claims must be copied from the paper and checked before final export.

## Composition Directives

- Use generous but not sparse whitespace; target roughly 30-35% empty space.
- Keep the largest visual slot for what only this paper demonstrates.
- Demote general theoretical themes to secondary cards unless the theory itself is the unique contribution.
- Use deterministic line art for schematic diagrams.
- Use source crops for evidence-class figures.
- Use generated art only as components; never as the full poster base.
- No QR code, fake logos, lorem ipsum, watermark, preprint pagination, or peer-review markings.
