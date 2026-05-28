---
name: agent-entrypoint-design
description: Use when designing or refactoring AGENTS.md, CLAUDE.md, GEMINI.md, Cursor rules, GitHub instructions, source-of-truth navigation, or agent onboarding entrypoints.
---

# Agent Entrypoint Design

## Overview

English summary: create a small, stable entrypoint that tells agents where truth lives, what rules apply, and which checks gate changes.

本 skill 用来设计 agent 进入仓库后的第一屏规则。入口文件应该是目录和硬规则，不是把所有工程知识塞成一篇长文。

## When To Use

- 用户要新建或重构 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`.cursorrules`、GitHub instructions。
- 多个 agent 指令文件内容重复、漂移或互相矛盾。
- 新项目需要定义 agent 先读什么、能改什么、改完跑什么。

## Inputs Needed

- 仓库根目录和主要 app/模块边界。
- 现有 agent 指令文件和 docs 入口。
- 是否需要镜像文件、symlink、生成脚本或 CI 检查。

## Execution Order

- First: 读取现有入口文件，确认哪个文件应成为 source of truth。
- Then: 设计根入口、子目录入口、镜像策略和验证命令。
- Finally: 输出入口文件结构和同步/防漂移检查。

## Step-by-Step Process

1. 搜索 `AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`.cursor`、`.github/instructions`。
2. 判断是否存在重复规则、过长规则、过时路径、chat-only 事实。
3. 选定一个主入口，其他 agent-specific 文件只镜像、symlink 或明确引用它。
4. 根入口只保留 scope、source-of-truth docs、do/avoid、commands、tests、相关技能。
5. 如果子目录有特殊规则，为子目录建更近的 `AGENTS.md`，不要把所有细节放根目录。
6. 定义防漂移机制：生成脚本、check 脚本、CI 或人工检查清单。

## Checks

- 入口检查：agent 是否能在 60 秒内知道先读什么、哪里能改、最小验证是什么。
- 一致性检查：镜像文件是否会漂移，是否有生成注释或 symlink 约束。
- 事实源检查：规则是否指向版本化 docs/scripts，而不是聊天记忆。
- 范围检查：根规则是否过细，子目录规则是否缺失。
- 可执行检查：每条关键规则是否有对应命令、文件或明确判断标准。

## Output Format

```markdown
# Agent Entrypoint Design

## Source Of Truth
- Primary entrypoint:
- Mirrors:
- Subtree overrides:

## Root Entrypoint Sections
-

## Sync / Drift Prevention
-

## Minimum Commands
-

## Follow-up Files
-
```

## Common Mistakes

- 在所有 agent 文件里复制大段规则，后续必然漂移。
- 让入口文件变成项目百科，agent 读完仍不知道先做什么。
- 把具体业务需求写进通用 agent 规则。
- 没有说明 instruction precedence。

## Example Prompts

- "给这个项目设计 AGENTS.md 和 CLAUDE/GEMINI 镜像规则。"
- "This repo has multiple agent instruction files. Make them source-of-truth safe."
- "把 agent 入口收缩成高信号导航。"
