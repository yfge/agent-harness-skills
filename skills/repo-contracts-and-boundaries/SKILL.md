---
name: repo-contracts-and-boundaries
description: Use when turning architecture, layering, directory ownership, dependency direction, file-size limits, choke points, baselines, or allowlists into repository checks.
---

# Repo Contracts And Boundaries

## Overview

English summary: convert architectural intent into checks that prevent new drift instead of relying on repeated prose warnings.

本 skill 用来把“不要新增漂移”机械化。它不负责重构全部历史债务，而是先冻结新增问题，再逐步收敛 baseline。

## When To Use

- 用户提到架构边界、目录边界、choke point、allowlist、baseline、contracts。
- 仓库已有层级规则，但 agent 仍会新增旁路调用或错误依赖。
- 需要区分 diff 模式和 audit 模式。

## Inputs Needed

- 架构文档或期望分层。
- 当前目录结构和历史债务位置。
- 需要保护的规则：导入方向、文件大小、API 入口、DB 访问、UI 边界等。

## Execution Order

- First: 读取架构文档和现有代码，找出真实边界与已知债务。
- Then: 设计 diff 检查、audit 检查、baseline 和 allowlist。
- Finally: 输出可执行 contract 规则和逐步收敛策略。

## Step-by-Step Process

1. 搜索 `ARCHITECTURE.md`、contracts docs、lint scripts、baseline/allowlist 文件。
2. 列出应该保护的规则，每条规则必须能被脚本或评审检查。
3. 区分新增漂移和历史债务：新增漂移应 fail，历史债务应进 baseline。
4. 设计 `--mode diff` 检查 changed files，`--mode audit` 扫全仓并生成报告。
5. 为每个 violation 输出 path、rule、why、suggested direction。
6. 明确什么时候允许修改 allowlist，以及必须附带什么偿还说明。

## Checks

- 机械性检查：规则是否能通过 AST、regex、import graph、路径扫描或报告脚本验证。
- baseline 检查：历史债务是否显式记录，是否避免“一次性清空”造成假绿。
- diff 检查：新改动是否能被低成本拦截。
- 例外检查：allowlist 是否有 owner、reason、收敛计划。
- 过度建设检查：不要用复杂平台替代一个清晰脚本能解决的问题。

## Output Format

```markdown
# Repo Contracts And Boundaries

## Protected Boundaries
-

## Diff Checks
-

## Audit Checks
-

## Baseline / Allowlist Policy
-

## Failure Message Shape
-

## Rollout Plan
-
```

## Common Mistakes

- 没有 baseline，导致历史债务让检查永远红。
- 只有 audit 没有 diff，agent 仍能继续引入新漂移。
- 错把架构建议当规则，规则却无法机械验证。
- fail message 不告诉 agent 应该怎么改。

## Example Prompts

- "把这个项目的 architecture boundary 做成检查。"
- "Design a diff/audit contract checker for this repo."
- "这些历史 choke point 怎么冻结新增依赖？"
