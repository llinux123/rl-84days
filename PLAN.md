# 强化学习84天学习规划

## 用户提问

你是如何学习 rl 的，告诉我你精确到天的规划和总规划，采用的学习法和步骤

## 豆包回答

我先快速确认一下 2025–2026 年最新的课程与 RL-for-LLM 实践资源，再给你一份可以直接执行的逐日规划。资源已确认（CS285 2026 版仍在更新并加入了 LLM RL；GRPO/RLVR 的最佳上手路径是 Mini-R1 + TRL/verl）。我现在把完整规划写成一份 Obsidian 友好的逐日清单文件。先说明一点：我没有人类意义上"按天学习"的经历——RL 知识来自训练数据，不存在我的学习日程。但我可以给你一份"如果我以你的目标（顶尖 PhD → OpenAI Research）从零学 RL，会怎么排"的最优路径。以下是完整内容，可勾选的 Obsidian 版文件在最后。

---

## 一、总规划（12 周 / 84 天）

**前提假设**：数学（微积分/线代/概率）合格、Python+PyTorch 能写训练循环、懂基本 ML；每天 6 小时有效投入，每周 6 天（每天 3 小时则翻倍为 24 周）。

| 阶段 | 周次 | 目标 | 主线材料 |
|---|---|---|---|
| P0 启动 | W1 前 3 天 | 环境、数学诊断、反馈系统 | S&B Ch1–3 |
| P1 Tabular 基础 | W1–W3 | 手推+手写全部表格型算法 | S&B Ch1–8、Silver L1–6 |
| P2 函数逼近+策略梯度 | W4–W5 | PG 定理、REINFORCE、A2C、GAE | S&B Ch9–10/13、Silver L7 |
| P3 现代深度 RL | W6–W8 | DQN/PPO/SAC/Model-based + 实验规范 | Spinning Up、CS285、原始论文 |
| P4 LLM 时代 RL | W9–W10 前半 | RLHF、DPO、GRPO/RLVR | InstructGPT、DPO、R1、trl/verl |
| P5 研究冲刺 | W10 后半–W12 | 复现+微创新+报告+博客 | 自选题目 |

**核心设计原则**：理论:代码 = 1:1；经典部分快速压缩（5 周），尽早抵达前沿；后 1/3 只做论文、复现和实验，不再刷课。

## 二、学习法（10 条）

1. **白纸推导（费曼）**：合上书从头推，能给人讲清楚才算过
2. **代码三级阶梯**：跟着敲 → 看伪代码独立写 → 空白复写；Q-learning/DQN/REINFORCE/A2C/PPO 必须到第三级
3. **Anki 间隔重复**：定理、伪代码填空卡、算法对比表，每天 20 分钟
4. **论文三遍法**：5 分钟扫图表结论 → 1 小时细读 → 批判性复现（换我会怎么做、漏洞在哪）
5. **实验科学规范**：结论性实验 ≥3 个随机种子、均值±置信区间、控制变量、消融、wandb 日志
6. **卡点日志**：每个 bug 记「症状→根因→教训」，周日回看
7. **公开输出**：GitHub + 每阶段一篇博客，以教为学
8. **固定周节奏**：周一到周六推进，周日上午默写自测，下午彻底休息
9. **主动回忆优先**：先做题先写代码，卡住再查，不做划线式阅读
10. **待在能力边界**：只练"似会不会"的，不刷已掌握内容

**标准一天（6h）**：理论精读 1.5h → 视频课 1h（1.25–1.5 倍速、暂停做题）→ 代码实验 2h → 笔记+Anki+日志 0.5h →（可选）晚间读论文 1h。

## 三、逐日规划（每天一行）

**W1 启动 + Bandit + MDP**

| 天 | 任务 |
|---|---|
| D1 | 装环境；数学自测；建 GitHub 仓库与日志；S&B Ch1 |
| D2 | 数学补强：重要性采样、矩阵求导、拉格朗日 |
| D3 | Gymnasium 随机 agent，吃透 env API；搭 Anki/笔记模板 |
| D4 | Ch2 多臂老虎机：ε-greedy、乐观初始化、UCB、gradient bandit |
| D5 | 代码：10 臂测试台，复现 Fig 2.2 / 2.4 |
| D6 | Ch3 MDP：手推 Bellman 期望/最优方程；Silver L1 |
| D7 | 周日：费曼讲 Bellman 方程由来；Anki；休息 |

**W2 动态规划 + 蒙特卡洛**

| 天 | 任务 |
|---|---|
| D8 | Silver L2；Ch3 习题；Bellman 方程的矩阵形式 |
| D9 | Ch4 DP：策略评估/改进、策略迭代、值迭代、GPI |
| D10 | 代码：GridWorld 策略迭代/值迭代，复现 Fig 4.1 |
| D11 | Ch5 MC：首访/每访、MC 控制、探索起点、异策 IS |
| D12 | Silver L3+L4；代码：Blackjack MC 复现 Fig 5.1–5.3 |
| D13 | Ch6 TD：TD(0)、SARSA、Q-learning、Expected SARSA、Double Q |
| D14 | 周日：默写 MC/Q-learning/SARSA 伪代码；休息 |

**W3 TD 深入 + 规划**

| 天 | 任务 |
|---|---|
| D15 | Silver L5；代码：Cliff Walking Fig 6.4 + Windy Gridworld |
| D16 | Ch6 习题；TD vs MC 偏差/方差/bootstrapping 对比笔记 |
| D17 | Ch7 n-step TD、n-step SARSA |
| D18 | Ch8 Dyna-Q、优先扫描、MCTS；代码 Dyna Maze Fig 8.2 |
| D19 | Silver L6（函数逼近预习） |
| D20 | 小项目：tabular Q-learning 解 Taxi/8×8 FrozenLake + 实验报告 |
| D21 | 周日：默写 PI/VI/MC/SARSA/Q-learning/Dyna 全部伪代码；休息 |

**W4 函数逼近 + 策略梯度起步**

| 天 | 任务 |
|---|---|
| D22 | Ch9.1–9.7：值函数梯度方法、梯度 MC/TD、线性逼近 |
| D23 | 代码：线性逼近 1000-state random walk；deadly triad |
| D24 | Ch10：on-policy 控制 with 函数逼近、半梯度 Sarsa |
| D25 | 代码：PyTorch Q-network 朴素解 CartPole（观察不稳定） |
| D26 | Ch13.1–13.4：**策略梯度定理完整推导**、REINFORCE |
| D27 | Silver L7；代码：REINFORCE 解 CartPole，观察高方差 |
| D28 | 周日：默写 PG 定理；休息 |

**W5 Actor-Critic**

| 天 | 任务 |
|---|---|
| D29 | QAC/A2C；证明 baseline 降方差但不改变梯度期望 |
| D30 | 代码：A2C CartPole/Acrobot，对比 REINFORCE |
| D31 | Ch13.7：高斯策略、连续动作 PG、DPG 引子 |
| D32 | 数学日：IS 再推导 + GAE 论文（λ-return、偏差方差） |
| D33 | 小项目：A2C 解 LunarLander，系统调参 + 报告 |
| D34 | 阶段复习：默写 REINFORCE/A2C + PG 定理 + GAE |
| D35 | 周日：休息 |

**W6 DQN 家族 + TRPO/PPO**

| 天 | 任务 |
|---|---|
| D36 | DQN Nature 精读：replay、target net、全部 trick；Silver L9 |
| D37 | 代码：从零 DQN 解 CartPole，replay/target 消融 |
| D38 | Double / Dueling / PER 三篇论文 |
| D39 | Rainbow 通读；代码：Double+Dueling |
| D40 | CS285 deep Q-learning 讲座；可选 Atari（SB3 对照） |
| D41 | TRPO 精读：替代目标、KL 约束、共轭梯度 |
| D42 | 周日：整理「问题→trick」清单；休息 |

**W7 PPO / SAC / Model-based**

| 天 | 任务 |
|---|---|
| D43 | PPO 论文 + Spinning Up：clip 目标、价值损失、熵 bonus |
| D44 | 代码：PPO 离散解 LunarLander，对照 SB3 |
| D45 | 代码：PPO 连续解 Pendulum；log prob、归一化、GAE 细节 |
| D46 | DDPG、TD3 论文 |
| D47 | SAC 论文（最大熵推导）；代码或精读 CleanRL SAC |
| D48 | CS285 model-based；AlphaZero/MuZero 通读 |
| D49 | 周日：休息 |

**W8 大实验 + 探索 + 离线/世界模型**

| 天 | 任务 |
|---|---|
| D50 | 探索专题：NoisyNet、RND 选 2 篇 |
| D51 | 大实验上：PPO/SAC，2–3 环境 × ≥3 种子 |
| D52 | 大实验下：置信区间曲线 + 超参/消融分析 |
| D53 | Offline RL：分布偏移、CQL 精读 |
| D54 | TD3+BC/IQL；D4RL 小数据集实验 |
| D55 | PETS、DreamerV2/V3；世界模型与 agent 的联系 |
| D56 | 周日：手绘 RL 算法家谱图；休息 |

**W9 RLHF + DPO**

| 天 | 任务 |
|---|---|
| D57 | RLHF 全景；**InstructGPT 精读** |
| D58 | Bradley-Terry、pairwise loss；走读 trl 相关代码 |
| D59 | 动手：0.5B–1.5B + LoRA 跑通 toy RLHF pipeline |
| D60 | **DPO 精读**：从 KL 正则目标推导 DPO 损失；IPO/KTO |
| D61 | 动手：DPOTrainer 实验，对比 SFT |
| D62 | MARL（QMIX/MAPPO）或层次化 RL，按兴趣选一 |
| D63 | 周日：白板推 DPO 损失；休息 |

**W10 GRPO/RLVR + 选题**

| 天 | 任务 |
|---|---|
| D64 | **GRPO**（DeepSeekMath + R1 报告）：组采样、组内相对优势、去 critic |
| D65 | 动手：Mini-R1 / TRL GRPOTrainer / verl，Qwen2.5-0.5B 跑 RLVR |
| D66 | 前沿扫描：agentic RL、tool-use、long-horizon、PRM；post-training 地图 |
| D67 | 选题：1 页 proposal（问题、方法、baseline、指标、算力） |
| D68 | 复现 baseline（上）：数据/环境/评测拉通 |
| D69 | 复现 baseline（下）：对齐官方指标 |
| D70 | 周日：休息 |

**W11 研究执行**

| 天 | 任务 |
|---|---|
| D71 | 评测管线：指标、数据版本、配置可复现 |
| D72 | rollout/数据管线工程化（最耗时的环节，留足） |
| D73 | 实现改进（上） |
| D74 | 实现改进（下）+ 首轮训练 |
| D75 | 消融：逐项验证每个改动 |
| D76 | 多种子、失败案例、负面结果 |
| D77 | 周日：休息 |

**W12 写作与交付**

| 天 | 任务 |
|---|---|
| D78 | 技术报告：Intro / Related / Method |
| D79 | 技术报告：Experiments / Analysis / Limitations |
| D80 | 公开博客（费曼级讲清问题与结论） |
| D81 | GitHub 收尾：README、一键复现脚本、日志归档 |
| D82 | 重做 Day1 自测对比；写后续 3–6 月研究计划 |
| D83 | 缓冲：补欠账 |
| D84 | 休息；确认下一程方向（对齐 / agentic / 世界模型 / robotics） |

## 四、毕业验收（D84 自检）

- **白板推导**：Bellman 方程、PG 定理+baseline 证明、GAE、PPO clip、DPO 损失、GRPO vs PPO
- **空白手写**：Q-learning/SARSA、DQN、REINFORCE、A2C、PPO；跑通过一次 DPO/RLHF 和一次 GRPO/RLVR
- **研究成果**：一个带多种子与消融的完整项目 + 技术报告 + 公开仓库，能讲清每个算法"解决了前任的什么问题"

资源要点：理论跟 S&B + Silver，深度部分跟 **CS285（2026 春仍在更新，已含 LLM RL）**；LLM-RL 动手走 Mini-R1、TRL、verl。

下面是可直接放进 Obsidian 的逐日勾选版。规划已交付。如果你告诉我当前的数学/PyTorch 基础和每天实际可投入的小时数，我可以把这份 84 天计划按比例校准（比如在读状态改成 24 周版，或基础好时把前三周压缩到 10 天）。