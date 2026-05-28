---
name: validation-harness-design
description: Use when designing repository validation commands, doctor scripts, test matrices, JSON or JUnit outputs, CI gates, smoke checks, or harness command surfaces.
---

# Validation Harness Design

## Overview

English summary: define the smallest repeatable command surface that proves repository changes are safe enough for review.

本 skill 负责把验证路径收口成 agent 能执行、CI 能复用、失败能诊断的命令集合。

## When To Use

- 用户要新增 `check_repo_harness.py`、`doctor.py`、test matrix、CI gate。
- 现有验证命令分散，agent 不知道 docs-only、frontend、backend、runtime 分别跑什么。
- 需要 JSON/JUnit/artifact 输出。

## Inputs Needed

- 技术栈、主要 app、现有测试命令、CI 配置。
- 哪些变更类型需要哪些最小 gate。
- 是否需要浏览器、真机、Docker、provider 或外部服务。

## Execution Order

- First: 盘点现有命令和 CI，确认哪些已经可用。
- Then: 设计分层验证矩阵和统一入口。
- Finally: 输出命令表、报告格式、CI 接入和降级规则。

## Step-by-Step Process

1. 搜索 `package.json`、Makefile、scripts、CI workflow、测试目录和 docs。
2. 把验证分成 repo/docs、contracts、unit/type/lint、runtime/browser/device。
3. 为每类变更指定最小命令和升级条件。
4. 设计统一入口：`check_repo_harness` 或 `doctor` 负责环境和结构；专项命令负责具体行为。
5. 设计报告输出：stdout 给人读，JSON/JUnit 给 CI 和 artifact。
6. 明确 skip/fallback 必须记录原因，不能把降级验证说成完整验证。

## Checks

- 可运行检查：命令是否能在干净 checkout 或 documented setup 下执行。
- 分层检查：docs-only 不应强制跑全量 runtime，runtime 改动不能只跑静态检查。
- 输出检查：失败是否能定位到 case、path、command、artifact。
- CI 检查：本地命令和 CI 逻辑是否一致。
- 成本检查：最小 gate 是否足够快，重 gate 是否只在高风险变更触发。

## Output Format

```markdown
# Validation Harness Design

## Change-Type Matrix
| Change type | Minimum check | Escalation |
| --- | --- | --- |

## Command Surface
-

## Report Outputs
-

## CI Gates
-

## Fallback / Skip Policy
-
```

## Common Mistakes

- 把所有变更都要求跑最重 E2E，导致 agent 实际跳过。
- 只有命令列表，没有变更类型矩阵。
- JSON/JUnit 输出不是稳定 schema，后续无法聚合。
- fallback 没记录，交付说明把 Playwright 当 Chrome DevTools。

## Example Prompts

- "给这个 repo 设计 check_repo_harness.py。"
- "Design validation commands for docs-only, frontend, backend, and runtime changes."
- "把这些测试整理成 CI gate 和 test matrix。"
