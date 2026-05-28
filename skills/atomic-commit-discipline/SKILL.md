---
name: atomic-commit-discipline
description: Use when splitting changes into atomic commits, checking git status and diffs, staging exact paths, writing Conventional Commits, or preventing unrelated changes.
---

# Atomic Commit Discipline

## Overview

Turn completed work into small, reviewable commits with scoped validation and no unrelated files.

This skill is not a PR template or ledger template. It focuses on minimal commits, exact staged paths, validation, and commit messages. For shared harness terms, see `../../references/harness-patterns.md`; when commit rules are absent, use `references/build-when-missing.md`.

## When To Use

- The user asks to commit, split commits, stage exact paths, or avoid unrelated changes.
- The worktree has multiple changes and you need to decide which belong in the same logical commit.
- The project requires Conventional Commits or a ledger entry paired with each commit.

## Inputs Needed

- Current `git status`, `git diff`, and `git diff --cached`.
- User goal and completed validation.
- Repository commit rules and whether ledger entries must be committed together.

## Execution Order

- First: Read `git status` and relevant diffs to identify your changes and unrelated changes.
- Then: Split staged paths by one logical behavior per commit, and run the minimum relevant validation.
- Finally: Write a Conventional Commit message, commit, and re-check status and commit contents.

## Step-by-Step Process

1. Run `git status --short --branch` and list all tracked and untracked changes.
2. Read `git diff -- <path>` for every file you intend to commit; do not commit changes you do not understand.
3. If no commit discipline is documented, bootstrap the minimum grouping and validation checklist from `references/build-when-missing.md`.
4. Group by logical boundary: docs, tests, implementation, harness, and ledger should not be mixed unless repository rules require the same commit.
5. Run the smallest validation command that matches each group; fix failures before committing.
6. Use `git add <exact paths>`; avoid `git add .` unless the whole worktree contains only this change.
7. Write a Conventional Commit subject, and use the body for validation, skip reasons, or linked artifacts when needed.
8. After committing, run `git show --stat --oneline HEAD` and `git status --short`.

## Checks

- Scope: each commit has one logical purpose.
- Ownership: no user-owned changes or temporary generated files are included by accident.
- Validation: the commit has matching pre-commit validation.
- Message: the subject describes behavior, not "update files."
- Ledger: if the repository requires `agent_chats` in the same commit, it is staged with the change.

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

- Using `git add .` and bringing unrelated files into the commit.
- Mixing features, formatting, docs, refactors, and temporary fixes in one commit.
- Committing before reading the diff.
- Writing commit messages such as "fix" or "update."
- Committing after validation fails.

## Example Prompts

- "Split these changes into atomic commits."
- "Commit only the harness docs and leave unrelated files unstaged."
- "Check git status and commit by logical group."
