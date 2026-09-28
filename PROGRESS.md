# RL 84 天学习进度追踪

> 与 `PLAN.md` 的逐日规划一一对应。每完成一天把 `[ ]` 改成 `[x]`，
> 并在当天条目后补一行简短记录（遇到的问题 / 收获 / 链接）。

## W1 · 启动 + Bandit + MDP

- [ ] **D1** 装环境；数学自测；建 GitHub 仓库与日志；S&B Ch1
- [ ] **D2** 数学补强：重要性采样、矩阵求导、拉格朗日
- [ ] **D3** Gymnasium 随机 agent，吃透 env API；搭 Anki/笔记模板
- [ ] **D4** Ch2 多臂老虎机：ε-greedy、乐观初始化、UCB、gradient bandit
- [ ] **D5** 代码：10 臂测试台，复现 Fig 2.2 / 2.4
- [ ] **D6** Ch3 MDP：手推 Bellman 期望/最优方程；Silver L1
- [ ] **D7** 周日：费曼讲 Bellman 方程由来；Anki；休息

## W2 · 动态规划 + 蒙特卡洛

- [ ] **D8** Silver L2；Ch3 习题；Bellman 方程的矩阵形式
- [ ] **D9** Ch4 DP：策略评估/改进、策略迭代、值迭代、GPI
- [ ] **D10** 代码：GridWorld 策略迭代/值迭代，复现 Fig 4.1
- [ ] **D11** Ch5 MC：首访/每访、MC 控制、探索起点、异策 IS
- [ ] **D12** Silver L3+L4；代码：Blackjack MC 复现 Fig 5.1–5.3
- [ ] **D13** Ch6 TD：TD(0)、SARSA、Q-learning、Expected SARSA、Double Q
- [ ] **D14** 周日：默写 MC/Q-learning/SARSA 伪代码；休息

## W3 · TD 深入 + 规划

- [ ] **D15** Silver L5；代码：Cliff Walking Fig 6.4 + Windy Gridworld
- [ ] **D16** Ch6 习题；TD vs MC 偏差/方差/bootstrapping 对比笔记
- [ ] **D17** Ch7 n-step TD、n-step SARSA
- [ ] **D18** Ch8 Dyna-Q、优先扫描、MCTS；代码 Dyna Maze Fig 8.2
- [ ] **D19** Silver L6（函数逼近预习）
- [ ] **D20** 小项目：tabular Q-learning 解 Taxi/8×8 FrozenLake + 实验报告
- [ ] **D21** 周日：默写 PI/VI/MC/SARSA/Q-learning/Dyna 全部伪代码；休息

## W4 · 函数逼近 + 策略梯度起步

- [ ] **D22** Ch9.1–9.7：值函数梯度方法、梯度 MC/TD、线性逼近
- [ ] **D23** 代码：线性逼近 1000-state random walk；deadly triad
- [ ] **D24** Ch10：on-policy 控制 with 函数逼近、半梯度 Sarsa
- [ ] **D25** 代码：PyTorch Q-network 朴素解 CartPole（观察不稳定）
- [ ] **D26** Ch13.1–13.4：**策略梯度定理完整推导**、REINFORCE
- [ ] **D27** Silver L7；代码：REINFORCE 解 CartPole，观察高方差
- [ ] **D28** 周日：默写 PG 定理；休息

## W5 · Actor-Critic

- [ ] **D29** QAC/A2C；证明 baseline 降方差但不改变梯度期望
- [ ] **D30** 代码：A2C CartPole/Acrobot，对比 REINFORCE
- [ ] **D31** Ch13.7：高斯策略、连续动作 PG、DPG 引子
- [ ] **D32** 数学日：IS 再推导 + GAE 论文（λ-return、偏差方差）
- [ ] **D33** 小项目：A2C 解 LunarLander，系统调参 + 报告
- [ ] **D34** 阶段复习：默写 REINFORCE/A2C + PG 定理 + GAE
- [ ] **D35** 周日：休息

## W6 · DQN 家族 + TRPO/PPO

- [ ] **D36** DQN Nature 精读：replay、target net、全部 trick；Silver L9
- [ ] **D37** 代码：从零 DQN 解 CartPole，replay/target 消融
- [ ] **D38** Double / Dueling / PER 三篇论文
- [ ] **D39** Rainbow 通读；代码：Double+Dueling
- [ ] **D40** CS285 deep Q-learning 讲座；可选 Atari（SB3 对照）
- [ ] **D41** TRPO 精读：替代目标、KL 约束、共轭梯度
- [ ] **D42** 周日：整理「问题→trick」清单；休息

## W7 · PPO / SAC / Model-based

- [ ] **D43** PPO 论文 + Spinning Up：clip 目标、价值损失、熵 bonus
- [ ] **D44** 代码：PPO 离散解 LunarLander，对照 SB3
- [ ] **D45** 代码：PPO 连续解 Pendulum；log prob、归一化、GAE 细节
- [ ] **D46** DDPG、TD3 论文
- [ ] **D47** SAC 论文（最大熵推导）；代码或精读 CleanRL SAC
- [ ] **D48** CS285 model-based；AlphaZero/MuZero 通读
- [ ] **D49** 周日：休息

## W8 · 大实验 + 探索 + 离线/世界模型

- [ ] **D50** 探索专题：NoisyNet、RND 选 2 篇
- [ ] **D51** 大实验上：PPO/SAC，2–3 环境 × ≥3 种子
- [ ] **D52** 大实验下：置信区间曲线 + 超参/消融分析
- [ ] **D53** Offline RL：分布偏移、CQL 精读
- [ ] **D54** TD3+BC/IQL；D4RL 小数据集实验
- [ ] **D55** PETS、DreamerV2/V3；世界模型与 agent 的联系
- [ ] **D56** 周日：手绘 RL 算法家谱图；休息

## W9 · RLHF + DPO

- [ ] **D57** RLHF 全景；**InstructGPT 精读**
- [ ] **D58** Bradley-Terry、pairwise loss；走读 trl 相关代码
- [ ] **D59** 动手：0.5B–1.5B + LoRA 跑通 toy RLHF pipeline
- [ ] **D60** **DPO 精读**：从 KL 正则目标推导 DPO 损失；IPO/KTO
- [ ] **D61** 动手：DPOTrainer 实验，对比 SFT
- [ ] **D62** MARL（QMIX/MAPPO）或层次化 RL，按兴趣选一
- [ ] **D63** 周日：白板推 DPO 损失；休息

## W10 · GRPO/RLVR + 选题

- [ ] **D64** **GRPO**（DeepSeekMath + R1 报告）：组采样、组内相对优势、去 critic
- [ ] **D65** 动手：Mini-R1 / TRL GRPOTrainer / verl，Qwen2.5-0.5B 跑 RLVR
- [ ] **D66** 前沿扫描：agentic RL、tool-use、long-horizon、PRM；post-training 地图
- [ ] **D67** 选题：1 页 proposal（问题、方法、baseline、指标、算力）
- [ ] **D68** 复现 baseline（上）：数据/环境/评测拉通
- [ ] **D69** 复现 baseline（下）：对齐官方指标
- [ ] **D70** 周日：休息

## W11 · 研究执行

- [ ] **D71** 评测管线：指标、数据版本、配置可复现
- [ ] **D72** rollout/数据管线工程化（最耗时的环节，留足）
- [ ] **D73** 实现改进（上）
- [ ] **D74** 实现改进（下）+ 首轮训练
- [ ] **D75** 消融：逐项验证每个改动
- [ ] **D76** 多种子、失败案例、负面结果
- [ ] **D77** 周日：休息

## W12 · 写作与交付

- [ ] **D78** 技术报告：Intro / Related / Method
- [ ] **D79** 技术报告：Experiments / Analysis / Limitations
- [ ] **D80** 公开博客（费曼级讲清问题与结论）
- [ ] **D81** GitHub 收尾：README、一键复现脚本、日志归档
- [ ] **D82** 重做 Day1 自测对比；写后续 3–6 月研究计划
- [ ] **D83** 缓冲：补欠账
- [ ] **D84** 休息；确认下一程方向（对齐 / agentic / 世界模型 / robotics）
