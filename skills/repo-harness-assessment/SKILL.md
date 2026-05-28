---
name: repo-harness-assessment
description: Use when evaluating an existing repository's agent-readiness, harness maturity, validation surfaces, source-of-truth docs, evidence artifacts, or next smallest harness improvement.
---

# Repo Harness Assessment

## Overview

English summary: assess how well a repository lets an agent understand rules, make safe changes, verify them, and produce reviewable evidence.

本 skill 用来先判断现状，不直接设计大改。目标是找出仓库的 agent/harness 缺口，并给出最小可落地补强切片。

## When To Use

- 用户问“这个 repo 的 harness 缺什么”“为什么是 harness”“怎么补 agent 工程化”。
- 需要对比多个 repo 的 agent 入口、验证命令、运行证据、交付记录。
- 需要决定下一步补 `AGENTS.md`、验证脚本、artifact、ledger 还是质量门禁。

## Inputs Needed

- 仓库根目录。
- 用户关心的变化范围：全仓、某个 app、docs-only、runtime、CI、交付流程。
- 已知参考项目或期望风格。

## Execution Order

- First: 读取仓库入口和事实源，包括 `AGENTS.md`、README、architecture/reliability/docs index、CI 和 scripts。
- Then: 查验证、证据、协作记录、任务/设计文档、提交规范是否已有机械入口。
- Finally: 输出当前成熟度、缺口、最小补强方案和不要过早建设的内容。

## Step-by-Step Process

1. 用 `rg --files` 或 `find` 列出入口文件、docs、scripts、CI、agent ledger 目录。
2. 读取最接近根目录的 agent 指令文件，确认它是否是目录型入口而不是长篇百科。
3. 搜索 `check_repo_harness`、`doctor`、`trace_run`、`quality`、`artifacts/runs`、`agent_chats`、`tasks.md`。
4. 判断仓库是否有稳定验证矩阵：docs、contracts、unit/type/lint、browser/device/runtime、CI。
5. 判断失败证据是否可追溯：run id、request id、日志、截图、JSON/JUnit、PR/commit 记录。
6. 把缺口压缩成最多 3 个下一步，按价值和风险排序。

## Checks

- 文件事实检查：入口文件是否存在，是否互相指向而不是互相复制漂移。
- 结构检查：有没有明确 source of truth、目录边界、禁止新增漂移规则。
- 验证检查：有没有一条本地最小命令和一条 CI 门禁命令。
- evidence 检查：是否能从失败现象定位到日志、trace、截图或运行 artifact。
- 过度建设检查：不要建议上来就做全量脚手架、平台化或跨环境自动发布。

## Output Format

```markdown
# Repo Harness Assessment

## Current State
- Agent entrypoint:
- Source-of-truth docs:
- Validation surface:
- Runtime evidence:
- Delivery/ledger:

## Gaps
1.
2.
3.

## Recommended Minimum Slice
- First:
- Then:
- Finally:

## Do Not Build Yet
-

## Validation Needed
-
```

## Common Mistakes

- 把 harness 简化成“有测试”。
- 只看 README，不看 scripts、CI 和真实 artifact。
- 把某个业务仓库的环境变量、端口、账号复制到另一个仓库。
- 给出一长串愿望清单，而不是最小补强切片。

## Example Prompts

- "检查这个 repo 的 harness 缺什么。"
- "Compare this repository against ai-video-studio style run artifacts."
- "这个项目现在 agent 能不能安全接手？"
