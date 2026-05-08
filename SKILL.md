---
name: paper-academic-poster
description: |
  Turn an academic paper (PDF, DOI, URL, pasted text, or extracted manuscript) into a composed vertical academic poster image using a divide-and-compose workflow. Use when the user asks for “学术海报”, “论文海报”, “conference poster”, “research poster”, “A0 poster”, “把论文做成海报”, “灵魂海报 / 设计感海报 / 特色锚点海报 / soulful poster”, or a visually attractive poster summarizing a paper. The workflow reads and understands the paper first, decomposes the poster into semantic regions and visual assets, generates/redraws sub-images where useful, preserves evidence crops when source fidelity matters, then deterministically composes the final poster with local text, layout, and QC.
---

# Paper Academic Poster

Create one vertical conference-grade academic poster from a paper. The default final artifact is a deterministic final canvas assembled from independently prepared regions: locally rendered text, source-preserved evidence crops, deterministic diagrams/tables, and GPT Image 2 generated sub-images for visual anchors, backgrounds, icons, and illustrative panels.

## Load Before Execution

Load `references/production-contract.md` and `references/hybrid-deterministic-composition.md` for every run. They are the source of truth for retrieval order, figure/material extraction, divide-and-compose production, manifest, and QC.

Load `references/gpt-image-2-direct-reference-assets.md` only when using GPT Image 2 to generate sub-images or when the user explicitly asks for a one-shot GPT Image 2 whole-poster preview.

**Default style: `academic_paper`.** When the source is a finished journal article (peer-review or pre-print) with named authors, ISSN/DOI, and a formal abstract, load `references/academic-paper-style.md` and use the region/component skeleton in `references/academic-paper-style-prompt-template.md`. Key rules: ivory + navy + brick-red (no gold/coral fields), serif title + sans-serif body, prose abstract top-left, concept-shift diagram top-right, centerpiece = paper's *unique* exhibit (architecture / case anatomy / debate transcript), 4 navy impact cards at bottom, ORCID footer.

If the user explicitly requests one-shot GPT Image 2, direct whole-poster, “一站式生成”, “不要本地排版”, or model-only authorship, treat that as an opt-out from the default divide-and-compose route. Load `references/gpt-image-2-direct-reference-assets.md`, name the trade-off, and do not silently promise exact text/evidence fidelity.

If the user asks for 4K output, stronger density, full-paper coverage, or original PDF screenshots/dialogue captures/data evidence as visible evidence, also load `references/4k-evidence-dense-posters.md`; follow its high-resolution divide-and-compose route.

If the user asks to compare multiple GPT Image 2 providers, compare them as **sub-image generators** unless the request explicitly says whole-poster model authorship. Load `references/direct-provider-comparison.md`.

If the user wants the poster to feel **design-driven / soulful / 设计感强 / 特色锚点突出 / 像信息图杂志特稿那样**, load `references/anchor-driven-design.md`. That route remains divide-and-compose: design decisions choose the regions, anchors, and generated sub-images; final typography and layout stay deterministic.

## Routing Boundaries

- Use this skill for paper → single vertical poster.
- Use `paper-explainer` for long-form paper explanations.
- Use `infographic-composer` for generic infographics not anchored to a paper.
- Use `ppt-image-pages` for 16:9 slide/page images.
- Once source material is available, do not ask for style/palette/layout. Ask only when no source can be retrieved or when choosing among equally valid evidence sets changes the scientific message.

## Non-Negotiable Rules

1. Read enough of the paper to supply accurate prompt facts, title, authors, central thesis, and material/evidence choices before generating.
2. Preserve exact numbers, dates, model names, baselines, metrics, datasets, sample sizes, and qualifiers.
3. Do not invent results, institutions, venues, affiliations, limitations, or datasets.
4. Default visual handling starts with classification, not blanket attachment. Preserve selected evidence-class originals (UI/dialogue screenshots, terminal/session logs, experiment-scene photos, observation artifacts, and data charts/tables with exact values) as source crops inside the final composition. Use GPT Image 2 for stylized sub-images only when exact fidelity is not required.
5. Concept/structure visuals (framework diagrams, box/arrow figures, pipelines, architecture diagrams) are redrawn as deterministic diagrams by default. Use source labels, ordering, arrows, groupings, and logic; do not paste an original concept diagram beside its redraw unless the source artifact itself is the evidence.
6. If text rendering, factual fidelity, or visual hierarchy fails, fix the affected region and re-export the composed poster. Do not patch a flawed whole-poster AI image; rebuild the region or composition from its source components.
7. **Centerpiece selection**: For papers, the largest visual slot belongs to what *only this paper demonstrates* (system actually built, experiment actually run, transcript actually captured), NOT to theoretical reframing themes that appear in many papers. Demote widely-discussed themes to a secondary band.
8. **Chinese text rule**: Render Chinese text locally in the final composition whenever possible. If a GPT Image 2 sub-image must contain Chinese, keep it to short display labels and still verify it by OCR/vision before composing.

## Image Toolchain

- **Default route for posters: deterministic A0-ratio composition.** Build the final poster with HTML/CSS, SVG, PIL, Cairo, or another local deterministic renderer. Use local fonts for title, body, metadata, labels, exact numbers, tables, and captions. Export a final PNG, and PDF when useful.
- **Sub-image generation route:** Use the bundled helper at `references/codex_direct_image_gen.py` to generate individual GPT Image 2 panels when needed (hero image, no-text atmosphere, stylized evidence backdrop, icon sheet, low-text mockup, or concept illustration). Prefer panel sizes matched to the final slot rather than generating a whole poster.
- **Fallback chain for sub-images:** Hermes `image_generate` (acceptable for small decorative/preview panels) → YouMind GPT Image 2 (`createChat` with `gpt-image-2-2026-04-21`) → ListenHub `gpt-image-2`.
- **Single-route 504/524 = immediate downgrade.** Do not retry the same route 3 × 600s after the first gateway failure. Switch routes or simplify the prompt instead.
- For exact A0/A-series portrait ratio, render the final canvas at 841:1189 ratio. Use at least `2480x3508`; for 4K delivery use `2896x4096` or higher. Verify actual dimensions on the final exported file.
- Never silently switch to Nano Banana Pro / Gemini / non-GPT routes. If GPT Image 2 routes fail, report the boundary unless the user explicitly authorizes another route.

### Hermes built-in lock (background, non-blocking)

Hermes' built-in `image_gen` tool hardcodes `_SIZES["portrait"] = "1024x1536"` in `plugins/image_gen/openai-codex/__init__.py`. This is by design: the tool is meant for fast, cheap, in-chat image generation (~30-60s), not for high-res poster work. The hardcode has no env/config override path, and `hermes update` rebases from the upstream NousResearch/hermes-agent repo — so any local plugin patch is lost on next upgrade.

This Skill therefore does NOT depend on the Hermes built-in for final poster production. The direct-helper script gets full size control by reusing Hermes' OAuth token only, while making its own `responses.stream(...)` call for sub-image generation.

## Workflow Summary

1. **Retrieve/extract**: follow the reference contract for DOI/title/URL/PDF/text; extract text plus candidate figures/tables; create `~/Downloads/paper-academic-poster-<slug>-<provenance_tag>-<YYYYMMDD>/`.
2. **Understand**: capture metadata, research question, contributions, method logic, key results with exact data, conclusion/limitations, type/length/field, and 3-5 concrete hook highlights.
3. **Plan regions**: divide the poster into semantic slots such as header/metadata, abstract/context, method or framework, centerpiece anchor, evidence/result panels, impact/limitations, and footer. Assign each slot an owner: local text, source crop, deterministic diagram, generated sub-image, or mixed.
4. **Triage visuals**: classify assets as evidence / concept / atmosphere. Preserve high-signal evidence-class originals as crops; redraw concept/structure figures deterministically; use GPT Image 2 for atmosphere, illustrative mockups, icon sheets, and stylized panels that do not carry exact facts.
5. **Produce components**: generate or render each region independently. Keep sub-image prompts slot-specific and avoid dense text inside generated panels. Save intermediate assets with stable names and record their source/action in the manifest.
6. **Compose**: build the final A0-ratio canvas deterministically with local fonts, exact text, measured layout, source crops, diagrams, and generated sub-images. Export `poster.png`; export `poster.pdf` when print delivery is useful.
7. **QC**: inspect components and final image; verify title/metadata, exact numbers, source evidence, text wrapping, no clipped panels, no QR code/placeholders, no redundant original concept diagrams beside redraws, actual pixel dimensions, and phone-preview hierarchy. Write `manifest.json` or `RUN_INFO.md`.

## Final Delivery

User-facing response must contain only:

1. `MEDIA:/absolute/path/to/poster.png` or a native image URL.
2. A 1-2 sentence Chinese design note explaining style, palette rationale, layout rationale, and figure handling.

This concise response does not waive local file saving, manifest creation, or platform delivery obligations for non-synced deliverables.
