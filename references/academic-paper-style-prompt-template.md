# Academic Paper Style — Prompt Template (v7 baseline, 2026-05-03)

This is the validated prompt template for `style=academic_paper`. It produced `poster_v7_dense.png` for the OpenClaw paper (《图书情报知识》, ISSN 1003-2797).

To adapt: replace paper-specific text (between markers) while preserving the layout skeleton, palette rules, and text rules. Pass to `references/codex_direct_image_gen.py` at size `2416x3424`, quality `high`.

---

A vertical academic conference poster, A0 portrait, single GPT Image 2 image, peer-review-grade scholarly style. Inspired by IEEE/ASIST/iConference dense academic posters. Restrained, designer-grade.

PALETTE: ivory/parchment background (#F5EFE5); deep navy (#1B2C4F) for typography and lines; ONE muted brick-red (#B23A2C) used ONLY for the small lobster mascot, the title 「OpenClaw」 word, the four agent dot markers, the small ① ② ③ ④ numerals, and the small "Agent" labels. NO gold, NO bright coral as field color.

TYPOGRAPHY: clean serif for the main title only (gives academic gravitas); clean sans-serif for everything else. Hierarchy via size + weight.

CRITICAL TEXT RULES:
- All Chinese text must render cleanly. No 竖心旁 doubled, no character corruption.
- Inside chat bubbles or detail blocks, break long Chinese into multiple short lines, each line ≤14 Chinese characters. Use line breaks instead of continuous long sentences. Render text VERBATIM as written below — do not paraphrase or shorten.

LAYOUT (top to bottom):

═════════════════════════════════════════════════
[HEADER STRIP] — three columns
LEFT (narrow, ~10%): a small red brick-red line-art lobster mascot (clean two-claw silhouette, simple) labeled "OpenClaw" tiny below.
CENTER (wide): main title in two lines, large serif, navy:
  Line 1: 「OpenClaw 为代表的 AI 智能体」
  Line 2: 「对情报学的影响与启示」
  Below: italic gray English subtitle: "The Impact and Implications of AI Agents Represented by OpenClaw on Information Science"
  Below: "王树义  徐杰  /  WANG Shuyi · XU Jie"
  Below: "天津师范大学管理学院 · School of Management, Tianjin Normal University"
RIGHT (narrow, ~15%): a small framed metadata box, italic body:
  《图书情报知识》
  Documentation, Information & Knowledge
  ISSN 1003-2797 · CN 42-1085/G2
  网络首发论文 · 2026-04-29

═════════════════════════════════════════════════
[UPPER BODY] — two columns
LEFT COLUMN (~45%, prose abstract, multi-line, sans-serif body):
  从对话式工具到行动主体。
  当 AI Agent 具备
  自主感知、自主规划、自主行动
  的主体性三要件，
  情报学既有的"人–信息–技术"
  三要素分析视角被直接挑战。
  本文主张：
  将智能体作为独立要素
  剥离出来。

RIGHT COLUMN (~55%): two side-by-side schematic diagrams with a thick navy arrow between them
  Left side label: 「传统三要素：人–信息–技术」
    Small triangle, three nodes labeled 人 / 信息 / 技术 (line-art, navy strokes)
  Big arrow → in the middle
  Right side label: 「四要素：人–智能体–信息–技术」
    Larger 4-node diamond/tetrahedron with bold labels:
    人 (目标设定者/审查者)
    Agent (多智能体协同) — this Agent label in brick-red
    信息 (含 Agent 产出)
    技术 (共享操作的工具)
    Show edges: "意图传达与监督", "协作与配置", "调用与操作", "创造与使用"

═════════════════════════════════════════════════
[CENTERPIECE — largest section] titled (large serif, navy):
  「OpenClaw 案例剖面 · OpenClaw in Action」

Two equal halves side-by-side:

LEFT HALF — 5-LAYER ARCHITECTURE (vertical stack of 5 layered boxes, navy outline on ivory):

  Layer 1 · 用户触发层 (User Trigger)
    [icon: small human figure]
    "@Agent A @Agent B 讨论话题 X 轮次 Y"

  Layer 2 · 会话编排层 (Orchestration)
    中心控制器 · Conversation Orchestrator
    [six small pill tags arranged in 2 rows of 3]
    Leader 选举 · UUID 会话隔离 · Round-robin 轮询
    flock 并发控制 · 相似度检测 · 会话记录累积

  Layer 3 · 异构智能体层 (Heterogeneous Agents)
    Three vertical sub-cards in a row, each navy-outlined:
      Agent A — GLM-5-Turbo
        独立人格文件
        技能集合
        隔离上下文
      Agent B — MiniMax M2.7
        独立人格文件
        技能集合
        隔离上下文
      Agent C — GPT-5.4
        独立人格文件
        技能集合
        隔离上下文

  Layer 4 · 消息通道层 (Message Channel)
    飞书 API · Lark API

  Layer 5 · 持久化状态层 (Persistent State)
    JSONL 会话转录本  ·  JSON 会话检查点

RIGHT HALF — DEBATE SCHEMATIC titled:
  「飞书群聊辩论场景示意图 · Lark Chat Debate Schematic (not a real screenshot)」

A stylized chat-window mockup, navy line-art on ivory.
Topic banner at top:
  AI 辩论群 · 辩题：
  智能体驱动的主动情报推送
  是否会削弱用户自主信息需求意识？

Four chat bubbles alternating left-right. Each bubble has a small brick-red dot avatar with the agent name above. Inside each bubble, render the Chinese text on multiple short lines (≤14 chars per line):

  ⓐ Agent A · GLM-5-Turbo (left bubble):
     持续的主动推送
     会使用户从主动寻者
     退化为被动接受者，
     削弱其认知能力。

  ⓑ Agent B · MiniMax M2.7 (right bubble):
     我检索了信息觅食理论
     的相关文献，可以反驳：
     推送降低搜寻成本，
     反而释放用户做
     更高阶认知带宽。

  ⓐ Agent A (left bubble):
     请注意你引用的
     研究情境是 90 年代
     的静态网页，
     不适用于 LLM 时代
     的生成式推送。

  ⓑ Agent B (right bubble):
     同意情境差异，
     让我重新检索
     2023 年后的实证证据……

Caption below the chat (small italic gray, multi-line ≤14 chars per line):
  在限定轮次与辩题边界内，
  两个 Agent 自主将宏观任务拆解为
  「提取对方观点的逻辑漏洞」
  「检索反驳案例」等子目标，
  自主检索，自主论证。人在环上。

═════════════════════════════════════════════════
[BOTTOM BAND] titled (large serif, navy):
  「四维冲击与挑战 · Four Impacts on Information Science」

Four equal-width dark navy cards in a single row, ivory text inside. Each card has:
- A small ① ② ③ ④ in brick-red at the top
- A bilingual title (large)
- A short multi-line description (small, ≤14 chars per line)

  ① 信息行为委托转型 · Behavior Delegation
     [icon: human → robot]
     搜寻主体从人类主动行为 →
     多 Agent 并行持续运转，
     Wilson/Kuhlthau 模型的
     「人类主动搜寻者」预设被松动

  ② 知识生产管线化 · Production Pipelining
     [icon: pipeline gears]
     检索型 Skill → 分析型 Skill →
     校验型 Skill 的 Agent 编排管线；
     OpenAI Deep Research、
     AutoResearch 自改进范式

  ③ 人在环中 → 人在环上 · Loop Repositioning
     [icon: human standing on loop]
     人类角色由执行者
     转向目标设定者
     与最终审查者，
     Harness 工程化驾驭

  ④ 四重风险 · Four-fold Risks
     [icon: shield with crack]
     提示注入与数据泄露；
     信息幻觉（学术引用率
     14.23%–94.93%）；
     信息源失信；
     主体性困境与认知卸载

═════════════════════════════════════════════════
[FOOTER STRIP] — single thin band
LEFT: 智能体应作为独立要素进入情报学的分析视角
CENTER: keyword pills in pill-shaped navy outlines:
  智能体  ·  OpenClaw  ·  情报学  ·  人在环上  ·  Harness
RIGHT: 王树义 ORCID: 0000-0001-5595-4416

═════════════════════════════════════════════════
DIRECTIVES:
- Generous whitespace between sections.
- All schematic line-art, no decorative photos.
- No QR code, no fake logos, no lorem ipsum, no watermark.
- Conference-grade restraint, like JCDL/ASIST/iConference work-style posters.
- Render every Chinese phrase EXACTLY as written above. Do not paraphrase or shorten.
- Multi-line text inside bubbles/cards uses natural line breaks at ≤14 chars per line.
