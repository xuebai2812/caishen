<div align="center">

# 裁神.skill

> *「被裁不是失败，是带着一笔钱，喜迎裁神。」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green)](https://agentskills.io)
[![Runtime](https://img.shields.io/badge/Runtime-Claude%20·%20Cursor%20·%20Codex-blueviolet)](#安装)

<br>

**裁神帮你算清能拿多少、教你怎么谈、谈不拢带你维权——别再被 HR 的话术拿捏。**

<sub>基于开放的 [Agent Skills 协议](https://agentskills.io)，可在 Claude 桌面端、Claude Code、Cursor、Codex 等兼容 runtime 中运行。</sub>

<br>

中国大陆每天都有人被「优化」。多数人吃亏，不是因为没有法律保护，<br>
而是不知道自己手里有哪些牌、把牌打错了顺序、在错的文件上签了字。<br>
裁神把这层信息差补平：告诉它你的城市、工龄、工资，它替你算账、定策略、列证据。

[看效果](#效果示例) · [安装](#安装) · [它能帮你什么](#它能帮你什么) · [工作原理](#工作原理) · [免责声明](#免责声明)

</div>

---

## 效果示例

```
你       ❯ 我被裁了，杭州，干满 6 年，税前月薪 4万5，HR 只给 N+1 让我这周签

裁神     ❯ 先别慌——这不是你的失败，是带着一笔钱体面离场的机会。
            我帮你把账算清，再看这刀该怎么接。

            结论：N+1 不是上限，你手里至少有三张牌 👇

            | 名目          | 金额（杭州封顶后） | 含义                    |
            |--------------|----------------|------------------------|
            | N（经济补偿）  | ≈ 18 万         | 协商解除的法律底线        |
            | N+1（现方案）  | ≈ 22.5 万       | 比底线略高，仍有谈判空间   |
            | 2N（违法解除）  | ≈ 36 万         | 若解除违法，这才是你的杠杆  |

            关键一问：HR 凭什么定性这是"协商解除"？
            让他出具写明理由的《解除通知书》——它直接决定
            你拿 18 万还是 36 万。这周，别签。
```

这不是泛泛的普法。裁神会先问清你的城市、工龄、工资，**用真实数字**算出 N / N+1 / 2N / 继续履行各值多少，再告诉你这一刀到底该接哪只手——并把谈判话术、证据清单一并给你。

---

## 安装

裁神基于开放的 [Agent Skills](https://agentskills.io) 协议，可在任何 skills-compatible 的 AI agent 中运行。选一种：

### 1️⃣ 一行话，让你的 agent 自己装（推荐）

打开你在用的 agent（Claude 桌面端 / Claude Code / Cursor / Codex 等），直接说：

```
帮我安装这个 skill：https://github.com/xuebai2812/caishen
```

或用通用安装器（[vercel-labs/skills](https://github.com/vercel-labs/skills)，跨 runtime）：

```bash
npx skills add xuebai2812/caishen
```

### 2️⃣ Claude 桌面端 / Cowork（点一下）

下载本仓库的 **`caishen.skill`** 文件 → 拖进 Claude 对话或双击 → 在卡片上点 **「Save skill / 安装技能」**。

### 3️⃣ 手动放进技能目录

<details>
<summary>展开查看各 runtime 的 skills 目录</summary>

| Runtime | 安装路径 |
|---|---|
| Claude Code | `~/.claude/skills/caishen/` |
| Codex CLI | `~/.codex/skills/caishen/` |
| Cursor | `~/.cursor/skills/caishen/` |
| 其他 runtime | clone 到对应 runtime 的 `skills/` 目录 |

```bash
git clone https://github.com/xuebai2812/caishen <上面对应的路径>
```

</details>

### 4️⃣ 当参考资料直接用

即使你的 agent 不支持自动加载，也可以把 `SKILL.md`（及 `references/` 里的文件）粘进对话——它本质就是一份 Markdown，喂进去照样能用。

---

## 使用

装好后**什么都不用设置**，用大白话描述处境，裁神会自动被唤起。把下面这类话发给它就行 👇

```
> 我被裁了，杭州工作 6 年税前月薪 3 万，公司给 N+1，我该拿多少、怎么谈？
> 公司说我绩效不达标要辞退我，让我签确认书，这字该不该签？
> 跟公司谈崩了想去劳动仲裁，需要准备哪些材料？有没有时间限制？
> 我还在哺乳期，公司要裁我，这样合法吗？
```

信息给得越具体（城市、入职/离职时间、税前月薪、公司方案、解除理由），算得越准、建议越到位。

---

## 它能帮你什么

| 模块 | 内容 |
|---|---|
| **算钱** | N / N+1 / 2N / 继续履行+期间工资，表格呈现，自动处理工龄折算与社平工资 3 倍封顶，配交互式计算脚本 |
| **教你谈** | 抬价话术、延长在职、HR 套路逐条反制，含「主张继续履行回去上班」这种公司最怕的反向筹码 |
| **带你维权** | 劳动仲裁材料清单、1 年时效、流程时间线、举证责任倒置、申请书模板 |
| **帮你避坑** | 哪些字千万别签、「不能胜任」四要件、特殊保护人群、竞业限制等红线 |

完事还能生成一份可下载、可打印的《签字前自查 + 仲裁材料清单》，让你照着一项项过。

---

## 工作原理

被唤起后，裁神按四步走：

**1. 先问清算钱必需信息**——城市、工龄、税前月薪、解除方式、公司方案。残缺就先补问，不凭空开算。

**2. 算账**——用计算脚本得出 N / N+1 / 2N / 继续履行各值多少，并**检索当年**当地社平工资 3 倍封顶基数（这个数每年更新，绝不用旧数）。

**3. 定策略**——区分"法律底线"与"谈判空间"，结合你的诉求（多拿钱 / 延长在职 / 不留 gap）给出话术与节奏。

**4. 兜维权底**——谈不拢时给出仲裁材料、时效、举证要点，并生成可带走的自查清单。

四大模块的完整规则在 `references/` 目录。

---

## 仓库结构

```
caishen/
├── SKILL.md                        # 裁神本体：主流程与四模块入口
├── references/
│   ├── compensation.md             # 补偿金计算详解（N/N+1/2N/继续履行）
│   ├── negotiation.md              # 谈判策略与话术
│   ├── arbitration.md              # 仲裁材料、流程、举证责任
│   ├── red_lines.md                # 避坑红线
│   └── city_wage_caps.md           # 社平工资封顶与当年数据检索指引
├── scripts/
│   └── compensation_calculator.py  # N/N+1/2N 计算器
└── assets/
    └── checklist_template.md       # 可带走的自查清单模板
```

---

## 免责声明

本技能提供的是基于**中国大陆现行劳动法律**的一般性信息，**不构成正式法律意见**，也不适用于其他法域。各地执行口径、个案事实差异都可能影响结果。涉及较大金额或复杂争议（尤其是 2N、工伤、竞业纠纷）时，请咨询当地劳动仲裁机构（**12333** 热线）或专业劳动法律师。

---

## 关于作者

由 **Snow（Shirley）** 创建。<!-- 可在此补充你的公众号 / 小红书 / X 等链接 -->

如果裁神帮到了你，欢迎 Star ⭐ 让更多被裁的人看到。

---

## 许可证

[MIT](LICENSE) —— 随便用，随便改，随便分发，保留版权声明即可。

---

<div align="center">

被裁不是失败，是带着一笔钱体面离场、换一个更好开始的机会。<br>
**把牌打好，喜迎裁神。**

<br>

MIT License © 2026 Snow (Shirley)

</div>

---

## English

> *"Getting laid off isn't failure — it's leaving with a check in hand."*

**Caishen** is an [Agent Skill](https://agentskills.io) that helps employees in mainland China handle layoffs: it calculates exactly how much severance you're owed (N / N+1 / 2N / reinstatement), coaches you through the negotiation with HR, and walks you through labor arbitration if talks break down — complete with an evidence checklist you can take with you.

Most people don't lose out for lack of legal protection — they lose out because they don't know which cards they hold, play them in the wrong order, or sign the wrong document. Caishen closes that information gap.

Runs in Claude Desktop, Claude Code, Cursor, Codex, and any Agent Skills–compatible runtime.

**Install** (cross-runtime, auto-detects your agent): `npx skills add xuebai2812/caishen`

> ⚠️ Provides general information based on current PRC labor law; not formal legal advice. For significant or complex disputes, consult a qualified labor lawyer or the local arbitration authority (hotline 12333).
