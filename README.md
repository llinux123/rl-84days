# 强化学习 84 天学习中枢

> 核心内容来自豆包对话《强化学习84天学习规划》（2026-09 分享）。
> 目标：12 周（84 天）从零到能独立做 RL-for-LLM 研究，路线 = CS285 + Sutton & Barto + verl 实战。

## 文件

| 文件 | 用途 |
|---|---|
| [`PLAN.md`](PLAN.md) | 完整规划原文：总规划、10 条学习法、W1–W12 逐日任务表、D84 毕业自检 |
| [`PROGRESS.md`](PROGRESS.md) | 逐日勾选追踪（D1–D84），每天做完打勾并补一行记录 |

## 目录结构

```
rl/
├── PLAN.md / PROGRESS.md / README.md   # 规划与追踪（本文件）
├── code/            # 按天编号代码：d<NN>_<slug>/，约定见 code/README.md
├── notes/           # 理论笔记
│   ├── glossary.md  # 术语表（Codex 维护，阅读中随时加词）
│   ├── daily/       # 每日读书笔记与推导
│   └── weekly/      # 每周费曼复述
├── logs/stuck.md    # 卡点日志：症状 → 根因 → 教训
├── experiments/     # W8 起大实验（多种子/消融/置信区间，规范见内）
├── reports/         # D78 起技术报告
├── blog/            # D80 公开博客草稿
└── raw/             # 原始存档：豆包分享 JSON、modern-rl 路线图 HTML
```

## 三个关键档期的验收线（来自 PLAN.md）

- **D28**：理论空白手写——Bellman 两个方程、Q-learning/SARSA、DQN、REINFORCE、A2C、PPO
- **D56**：代码空白默写——DQN 损失、GRPO vs PPO；跑通过一次 DPO/RLHF 和一次 GRPO/RLVR
- **D84**：一个带多种子与消融的完整项目 + 技术报告 + 公开仓库

## 使用约定

1. 每天学习前先打开 `PROGRESS.md`，当天条目打勾
2. 卡住超过 40 分钟：重跑实验 → 查书/课 → 带报错和猜测去问 AI 助手
3. 每周日复盘（W1–W11 每天都安排了周日费曼复述 + Anki + 休整）
4. 起点校准：如果数学/PyTorch 基础好，可把 W1–W3 压缩到 10 天；如果在读时间少，整体放大到 24 周版

## 相关资源

- 课程：CS285（2026 春版，含 LLM RL）、Silver 公开课、Sutton & Barto
- 实战：Mini-R1、TRL、verl
- 已 clone 的补充教材：`~/codebase/github/hands-on-modern-rl`（配套 6 阶段路线图见 `raw/modern-rl-study-roadmap.html`）
- 长线关联：`~/learn/plans/vla-worldmodel-learning/`（VLA+世界模型，本规划是其 RL 地基的强化版）

---
*提取来源：https://www.doubao.com/thread/xDl4DAIUHws6q1Tfk （分享名：强化学习84天学习规划）*
