---
name: agent-ledger-and-delivery
description: Use when designing agent_chats or agents_chat records, PR evidence, delivery summaries, linked commits, validation notes, risks, or handoff records.
---

# Agent Ledger And Delivery

## Overview

English summary: define how agent work is recorded so reviewers can see prompt, intent, changes, validation, risks, and linked commits.

本 skill 负责交付层记录，不负责拆 commit。本 skill 的重点是 PR/交付证据汇总和长期可追溯。

## When To Use

- 用户提到 `agent_chats`、`agents_chat`、PR 描述、交付记录、linked commits。
- 项目要求每次 AI 协作留下记录。
- 需要把 validation、risk、next steps 和 artifact 引用写成稳定格式。

## Inputs Needed

- 仓库现有 ledger 目录和命名规则。
- 本次用户目标、变更摘要、验证命令、artifact/PR/commit。
- 是否要求同 commit 绑定 ledger。

## Execution Order

- First: 读取现有 ledger 规则和最近样例。
- Then: 设计记录 schema、命名、必填 sections、commit/PR 绑定方式。
- Finally: 输出可复制的 ledger 模板和 delivery checklist。

## Step-by-Step Process

1. 搜索 `agent_chats`、`agents_chat`、CI 检查、AGENTS 规则、PR template。
2. 确认记录粒度：每 commit、每 PR、每会话、每里程碑。
3. 定义文件命名、frontmatter、正文 sections、语言、脱敏要求。
4. 定义何时必须更新 ledger，何时允许 skip，以及 skip 如何记录。
5. 定义 PR summary 如何引用 commits、validation、artifacts、risks、next steps。
6. 保持 ledger 和 atomic commit 规则解耦：本 skill 写记录格式，提交拆分由 `atomic-commit-discipline` 处理。

## Checks

- 完整性检查：prompt/goals/changes/validation/risks/linked commits 是否齐全。
- 绑定检查：代码变更是否有对应 ledger 或明确 skip 理由。
- 可读性检查：记录是否能让未来 agent 接续，而不是只写“完成了”。
- 隐私检查：不写 token、密钥、私人聊天原文或敏感日志。
- 防重复检查：不要同时维护两个互相漂移的 ledger 格式。

## Output Format

```markdown
# Agent Ledger And Delivery

## Ledger Policy
- Directory:
- Filename:
- Required metadata:
- Required sections:

## Delivery Summary Template
-

## Commit / PR Coupling
-

## Validation Evidence
-

## Skip Policy
-
```

## Common Mistakes

- ledger 只写流水账，不写验证和风险。
- PR summary 与实际 validation 不一致。
- 把 atomic commit 规则混进 ledger skill，导致职责重叠。
- 记录包含敏感内容。

## Example Prompts

- "给这个项目设计 agents_chat 记录规范。"
- "Make a PR evidence template for this agent-driven repo."
- "这个交付记录应该包含哪些 validation 和 linked commits？"
