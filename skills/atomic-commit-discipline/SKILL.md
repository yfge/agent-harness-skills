---
name: atomic-commit-discipline
description: Use when splitting changes into atomic commits, checking git status and diffs, staging exact paths, writing Conventional Commits, or preventing unrelated changes.
---

# Atomic Commit Discipline

## Overview

English summary: turn completed work into small, reviewable commits with scoped validation and no unrelated files.

本 skill 负责做事后落库。它不是 PR 模板，也不是 ledger 模板；它专注于最小提交、精确 staged paths、验证和提交信息。

## When To Use

- 用户说 commit、拆提交、stage exact paths、不要混入无关改动。
- 工作区有多个变更，需要判断哪些属于同一逻辑提交。
- 项目要求 Conventional Commits 或每个 commit 搭配 ledger。

## Inputs Needed

- 当前 `git status`、`git diff`、`git diff --cached`。
- 本次用户目标和已完成验证。
- 仓库提交规则和是否要求 ledger 同提交。

## Execution Order

- First: 读取 `git status` 和相关 diff，识别自己改的文件与无关改动。
- Then: 按一个逻辑行为一个提交拆分 staged paths，并运行最小必要验证。
- Finally: 写 Conventional Commit 信息，提交后复查状态和提交内容。

## Step-by-Step Process

1. 运行 `git status --short --branch`，列出所有 tracked/untracked 变化。
2. 用 `git diff -- <path>` 阅读要提交的每个文件，不提交没读懂的变更。
3. 按逻辑边界分组：docs、tests、implementation、harness、ledger 不要随意混合，除非同一规则要求同提交。
4. 对每组运行最小相关验证；验证失败先修，不要提交“稍后再修”。
5. 使用 `git add <exact paths>` 精确 staged，不用 `git add .` 除非确认全仓只有本次变更。
6. 写 Conventional Commit subject，必要时 body 记录 validation、skip reason、linked artifact。
7. 提交后运行 `git show --stat --oneline HEAD` 和 `git status --short` 复查。

## Checks

- 范围检查：每个提交是否只有一个逻辑目的。
- ownership 检查：是否误提交用户已有改动或生成临时文件。
- 验证检查：提交前是否跑过和本组变更匹配的最小命令。
- message 检查：subject 是否表达行为，而不是“update files”。
- ledger 检查：如果仓库要求 agent_chats 同提交，是否同批 staged。

## Output Format

```markdown
# Atomic Commit Plan

## Worktree State
-

## Commit Groups
1. Subject:
   Paths:
   Validation:

## Excluded Changes
-

## Final Checks
- First:
- Then:
- Finally:
```

## Common Mistakes

- 用 `git add .` 把无关文件带进去。
- 一个提交同时改功能、格式、文档、重构和临时修复。
- 没有读 diff 就提交。
- 提交信息只写“fix”或“update”。
- 验证失败仍然提交。

## Example Prompts

- "帮我把这批改动拆成原子提交。"
- "Commit only the harness docs and leave unrelated files unstaged."
- "检查 git status，按逻辑分组提交。"
