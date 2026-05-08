---
name: paper-academic-poster
description: |
  Turn an academic paper (PDF, DOI, URL, pasted text, or extracted manuscript) into a single GPT Image 2 direct-generated vertical academic poster image. Use when the user asks for “学术海报”, “论文海报”, “conference poster”, “research poster”, “A0 poster”, “把论文做成海报”, “灵魂海报 / 设计感海报 / 特色锚点海报 / soulful poster”, or a visually attractive poster summarizing a paper. The workflow reads and understands the paper first, classifies visuals into evidence originals versus concept redraws, supplies compact paper facts plus selected evidence-class materials and redraw instructions to GPT Image 2, then delivers the model-returned poster image plus a 1-2 sentence Chinese design note. Do not locally fill text, paste screenshots, or compose layout after generation unless the user explicitly requests deterministic source-faithful composition.
---

# Paper Academic Poster

Create one vertical conference-grade academic poster from a paper. The default final artifact is one GPT Image 2 whole-poster generation; scientific reading guides the prompt and material selection, but the returned model image is not patched locally.

## Load Before Execution

Load `references/production-contract.md` and `references/gpt-image-2-direct-reference-assets.md` for every run. They are the source of truth for retrieval order, figure/material extraction, direct GPT Image 2 generation, manifest, and QC.

**Default style: `academic_paper`.** When the source is a finished journal article (peer-review or pre-print) with named authors, ISSN/DOI, and a formal abstract, load `references/academic-paper-style.md` and use the prompt skeleton in `references/academic-paper-style-prompt-template.md`. This is the validated style for peer-reviewed posters (validated 2026-05-03 on the OpenClaw / 图书情报知识 paper). Key rules: ivory + navy + brick-red (no gold/coral fields), serif title + sans-serif body, prose abstract top-left, concept-shift diagram top-right, centerpiece = paper's *unique* exhibit (architecture / case anatomy / debate transcript), 4 navy impact cards at bottom, ORCID footer.

If the user explicitly requests deterministic exact text rendering, pixel/source-faithful evidence preservation, a local A0 composition, poster PDF export, or authorizes local layout after a direct-generation failure, also load `references/hybrid-deterministic-composition.md`. That route is an opt-in exception, not the default for Chinese-text-heavy or evidence-rich papers.

If the user asks for 4K output, stronger density, full-paper coverage, or original PDF screenshots/dialogue captures/data evidence as visible evidence, also load `references/4k-evidence-dense-posters.md`; follow its classified direct GPT Image 2 override unless the user explicitly wants deterministic source-faithful composition.

If the user says “GPT Image 2 一站式生成 / 全图生成 / direct whole-poster / 不要本地填文字或排版”, treat that as confirmation of the default route and enforce it strictly: no local text/layout/screenshot overlay, no crop/pad patching, and no deterministic fallback without asking.

If the user asks to compare multiple GPT Image 2 providers, or asks for the highest native resolution after an upscaled result looked soft, also load `references/direct-provider-comparison.md`; deliver only outputs that pass its QC line.

If the user wants the poster to feel **design-driven / soulful / 设计感强 / 特色锚点突出 / 像信息图杂志特稿那样**, load `references/anchor-driven-design.md`. That route is a stricter variant of the default GPT Image 2 direct path: native-large only, no upscale, no local overlay.

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
4. Default visual handling starts with classification, not blanket attachment. Preserve selected evidence-class originals (UI/dialogue screenshots, terminal/session logs, experiment-scene photos, observation artifacts, and data charts/tables with exact values) as GPT Image 2 reference/material inputs or cited reference URLs when slots are unavailable.
5. Concept/structure visuals (framework diagrams, box/arrow figures, pipelines, architecture diagrams) are redrawn in a unified poster style by default. Use the source only to extract labels, ordering, arrows, groupings, and logic; do not also include the original source diagram as a visible evidence panel when the poster already redraws the same idea.
6. If text rendering, factual fidelity, or visual hierarchy fails, regenerate with GPT Image 2 direct mode, simplify the prompt/reference set, or ask before switching to deterministic composition. Do not crop, pad, paste, overpaint, or overlay a flawed generated poster as the final fix.
7. **Centerpiece selection**: For papers, the largest visual slot belongs to what *only this paper demonstrates* (system actually built, experiment actually run, transcript actually captured), NOT to theoretical reframing themes that appear in many papers. Demote widely-discussed themes to a secondary band.
8. **Chinese long-sentence rule**: GPT Image 2 corrupts long Chinese sentences (typical: `情` → `忄忄青`). Body-level Chinese must be broken into multiple visual lines of ≤14 characters each. Proper nouns (title, authors, journal, model names, layer names, ORCID) must be listed as a "must-not-abbreviate" block in the prompt — otherwise the model over-generalizes the short-phrase rule and shrinks the title too. See `references/academic-paper-style.md` for the two-layer rule.

## Image Toolchain

- **Default route for posters: Codex Responses direct call at native `2416x3424` portrait, `quality=high`.** Use the bundled helper at `references/codex_direct_image_gen.py`, invoked with the Hermes venv python from the local Hermes checkout. Set `HERMES_AGENT_HOME` to the user's Hermes agent directory if it is not `~/.hermes/hermes-agent`. The helper reuses Hermes' `_build_codex_client()` to obtain the Codex OAuth token and then calls `responses.stream(tools=[image_generation], size, quality)` directly — bypassing Hermes' built-in `image_gen` size lock. This produces ~7-9 MB native PNGs in ~2-4 minutes.
- **Fallback chain (only if the direct helper fails)**: Hermes `image_generate` (locked at 1024×1536, ~2 MB — acceptable only as preview/last resort) → YouMind GPT Image 2 (`createChat` with `gpt-image-2-2026-04-21`, double-credit) → ListenHub `gpt-image-2` (gateway-prone to 504/524 on long Chinese prompts).
- **Single-route 504/524 = immediate downgrade.** Do not retry the same route 3 × 600s after the first gateway failure. Switch routes or simplify the prompt instead.
- For exact A0/2:3 print ratio, the default `2416x3424` is the calibrated choice (very close to A-series 1:√2 in portrait). Use `2160x3840` only when the user explicitly asks for 16:9 inverse / 4K portrait. Whole-image resize is allowed only when the user requests a specific delivery size and the route permits it; never add local text, screenshots, labels, borders, or layout patches. **The anchor-driven-design route forbids even whole-image resize — see that reference for the native-large-only chain and size parameters.**
- For "4K / clear large image / 清晰大图" requests, verify actual pixel dimensions on the downloaded file (long-edge floor 2304 px); do not rely on labels rendered inside the image.
- Never silently switch to Nano Banana Pro / Gemini / non-GPT routes. If GPT Image 2 routes fail, report the boundary unless the user explicitly authorizes another route.

### Hermes built-in lock (background, non-blocking)

Hermes' built-in `image_gen` tool hardcodes `_SIZES["portrait"] = "1024x1536"` in `plugins/image_gen/openai-codex/__init__.py`. This is by design: the tool is meant for fast, cheap, in-chat image generation (~30-60s), not for high-res poster work. The hardcode has no env/config override path, and `hermes update` rebases from the upstream NousResearch/hermes-agent repo — so any local plugin patch is lost on next upgrade.

This Skill therefore does NOT depend on the Hermes built-in for its primary route. The direct-helper script gets full size control by reusing Hermes' OAuth token only, while making its own `responses.stream(...)` call.

## Workflow Summary

1. **Retrieve/extract**: follow the reference contract for DOI/title/URL/PDF/text; extract text plus candidate figures/tables; create `~/Downloads/paper-academic-poster-<slug>-<provenance_tag>-<YYYYMMDD>/`.
2. **Understand**: capture metadata, research question, contributions, method logic, key results with exact data, conclusion/limitations, type/length/field, and 3-5 concrete hook highlights.
3. **Triage visuals**: classify assets as evidence / concept / atmosphere before prompting. Preserve only high-signal evidence-class originals as GPT Image 2 material references; convert concept/structure figures into redraw sub-prompts; omit redundant originals when the poster already redraws that logic. For direct generation, evidence panels are model-rendered from source materials, not locally pasted.
4. **Compress content**: use short section labels and bullets; include only numbers/claims traceable to source; compress authors/venue/DOI per reference. For “not dense enough” feedback, increase substantive coverage of the paper’s argument structure (sections, risks, limits, evidence-to-claim mapping), not merely font count.
5. **Produce**: default to GPT Image 2 direct whole-poster generation with prompt facts, selected evidence originals, and concept-redraw instructions. For Chinese conceptual, social-science, information-science, or agent-system papers, identify the central tension and strongest visual/evidence anchor before prompting, but still generate the final poster as one GPT Image 2 image. Use deterministic/hybrid routes only when the user explicitly requests or authorizes local composition.
6. **QC**: inspect the final image; verify it is a single generated poster with no local overlay/composition after generation, title/metadata broadly correct, key labels plausible, no QR code, no placeholders, no large 乱码/gibberish, preserved evidence-class visuals represented when supplied, and no redundant original concept diagrams duplicating redrawn logic. Write `manifest.json` or `RUN_INFO.md`.

## Final Delivery

User-facing response must contain only:

1. `MEDIA:/absolute/path/to/poster.png` or a native image URL.
2. A 1-2 sentence Chinese design note explaining style, palette rationale, layout rationale, and figure handling.

This concise response does not waive local file saving, manifest creation, or platform delivery obligations for non-synced deliverables.
