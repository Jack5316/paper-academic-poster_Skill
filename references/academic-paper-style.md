# Academic Paper Style — Default for Peer-Reviewed Posters

Use this style for posters anchored to a real journal article (peer-review or pre-print). Default for `paper-academic-poster` when the source is a finished paper with formal abstract, named authors, ISSN/DOI, and publishable claims. Validated 2026-05-03 on the OpenClaw / 图书情报知识 paper (v7).

## Visual Identity

- **Palette**: ivory/parchment background `#F5EFE5` + deep navy `#1B2C4F` + ONE muted brick-red `#B23A2C` accent. The brick-red is reserved for: a small mascot/identity icon, key brand words inside the title (e.g. `OpenClaw`), agent-letter dot markers (Ⓐ Ⓑ), small ① ② ③ ④ numerals. NO gold, NO bright coral as field color.
- **Typography**: clean serif for the main title only (gives academic gravitas); sans-serif for everything else. Hierarchy via size + weight, never via different fonts.
- **Whitespace**: ~30-35% (denser than Mike Morrison billboard, looser than commercial infographics).
- **Tone**: like an IEEE / ASIST / iConference dense academic poster, not a marketing infographic.

## Structural Template

```
┌─ HEADER STRIP (3 columns) ──────────────────────────────────┐
│ [lobster/mascot]  TITLE (2 lines, serif, navy)              │
│                   English subtitle (italic gray)            │
│                   Authors / WANG Shuyi · XU Jie             │
│                   Affiliation / English affiliation         │
│                                                             │
│ [Right metadata box: 《期刊名》/ Journal / ISSN / 网络首发] │
├─ UPPER BODY (2 columns) ───────────────────────────────────┤
│ Prose abstract paragraph     | Concept-shift diagram        │
│ (multi-line short clauses)   | (small old → big new)        │
├─ CENTERPIECE (2 halves) ───────────────────────────────────┤
│ ARCHITECTURE (5-layer        | DEBATE/CASE EXHIBIT          │
│  vertical stack with         |  topic banner +              │
│  bilingual labels +          |  ≥4 chat bubbles with        │
│  sub-component pills)        |  agent identities and        │
│                              |  multi-line short quotes     │
├─ BOTTOM IMPACT BAND ────────────────────────────────────────┤
│ Title: 「四维冲击与挑战 · Four Impacts on ...」              │
│ 4 navy-filled cards in a row, each with:                    │
│   ① brick-red numeral  + bilingual title + multi-line desc │
├─ FOOTER STRIP ──────────────────────────────────────────────┤
│ One-line takeaway | keyword pills | ORCID                   │
└─────────────────────────────────────────────────────────────┘
```

## Why this layout

1. **Mascot + title row**: identity is preserved (the brick-red lobster says "this is OpenClaw") but doesn't dominate (it's small and monochrome-ish).
2. **Prose abstract paragraph (top-left)**: gives readers paper-style context within 5 seconds. Better than bullets for academic gravitas.
3. **Concept-shift diagram (top-right)**: the paper's headline framework move (here: 三要素 → 四要素), placed where the eye lands second.
4. **Architecture + Case exhibit centerpiece**: this is the slot where the paper's *unique* contribution lives. For OpenClaw paper it's the 5-layer multi-agent architecture + the live multi-agent debate transcript — the things only this paper has.
5. **Four-impact band**: distillation of theoretical claims, given as navy cards so they read as "secondary structure" rather than as the headline.
6. **ORCID footer**: small academic credibility signal, like a journal byline.

## Critical Text Rules (avoid GPT Image 2 corruption)

GPT Image 2 corrupts long Chinese sentences (typical failure: 竖心旁 doubling, e.g. `情` → `忄忄青`). Two-layer rule:

### Proper nouns must render in full

In the prompt, list these as a "must-not-abbreviate" block:
- Paper title, English subtitle, authors line, affiliation
- Journal name, ISSN, CN number, network publication date
- All model identifiers (e.g. `GLM-5-Turbo`, `MiniMax M2.7`, `GPT-5.4`)
- Architecture layer names (`用户触发层`, `会话编排层`, etc.)
- ORCID

### Body Chinese: ≤14 chars per visual line

For abstract paragraphs, debate quote bubbles, impact-card descriptions, and any other body-level Chinese, BREAK the text into multiple short visual lines, each ≤14 Chinese characters, joined by line breaks. Render verbatim — do not paraphrase.

Example (debate bubble):
```
持续的主动推送
会使用户从主动寻者
退化为被动接受者，
削弱其认知能力。
```

Not this (will corrupt):
```
持续的主动推送会使用户从主动寻者退化为被动接受者，削弱其认知能力。
```

If after generation any character looks corrupted (compare 「情」 「报」 「学」 against expected), regenerate with the same prompt — same-prompt different-seed runs typically clear up isolated corruption.

## Material Selection Principle

The centerpiece slot ("OpenClaw 案例剖面" / "Case Anatomy") is for **what only this paper demonstrates**, not for the theoretical claims that other papers also touch:

- For OpenClaw paper: featured the **multi-agent debate** + **5-layer architecture**, demoted the four impact themes (信息行为 / 知识生产 / 人机角色 / 风险挑战) to a secondary band, because those themes are widely discussed elsewhere.
- General principle: identify which figures/exhibits in the paper are *first-of-its-kind / experiment-actually-run / system-actually-built*. Those go in the centerpiece. The reframing/conceptual claims go in the secondary band.

## Validated reference output

`output/poster_v7_dense.png` (2416×3424, 6.9 MB) — generated 2026-05-03, prompt at `output/poster_v7_prompt.txt`.

## Prompt Template

See `references/academic-paper-style-prompt-template.md` for the full prompt structure. Adapt by replacing paper-specific content (title, abstract, architecture layers, debate transcript, impact cards) while preserving the layout skeleton, palette rules, and text rules.
