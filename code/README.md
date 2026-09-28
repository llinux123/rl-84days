# code/ 命名约定

- 一天一个目录：`d<NN>_<slug>/`，NN = PLAN.md 的 D 编号，补零两位
- 示例：`d05_bandit_testbed/`、`d10_gridworld_dp/`
- 每个目录：可独立运行的脚本 + 运行命令 + 结果说明
- 跨天复用的工具（seed、plot 等）放 `code/lib/`
