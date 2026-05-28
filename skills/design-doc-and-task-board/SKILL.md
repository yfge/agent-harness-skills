---
name: design-doc-and-task-board
description: Use when deciding how requirements should be captured in design docs, tasks.md, exec plans, acceptance criteria, status updates, or planning source-of-truth files.
---

# Design Doc And Task Board

## Overview

Decide where intent, design, execution tasks, and acceptance criteria should live so they do not drift.

Design docs explain why and how; `tasks.md` tracks current work and state; exec plans describe how to execute a complex batch of changes. For shared harness terms, see `../../references/harness-patterns.md`; when planning files are absent, use `references/build-when-missing.md`.

## When To Use

- The user asks whether a requirement belongs in a design doc, `tasks.md`, or an exec plan.
- README, design docs, tasks, and exec plans start to duplicate or drift.
- Requirements need to become tasks, statuses, acceptance criteria, and change records.

## Inputs Needed

- Current requirement or change goal.
- Existing `tasks.md`, design docs, exec plans, README, and docs index.
- Change size, cross-module scope, and whether long-term tracking is needed.

## Execution Order

- First: Read existing planning sources of truth and identify how this project expresses intent and status.
- Then: Decide whether this requirement belongs in a design doc, task board, exec plan, or combination.
- Finally: Output the doc/task sync strategy, acceptance criteria, and update order.

## Step-by-Step Process

1. Search for `tasks.md`, `PLANS.md`, `docs/design*`, `docs/exec-plans`, and README.
2. Identify each file's actual responsibility; do not infer solely from names.
3. If no planning surface exists, bootstrap the minimum design/task/exec-plan set from `references/build-when-missing.md`.
4. Classify by complexity: small fixes update tasks only; architecture or cross-module changes start with a design doc; multi-day batches use an exec plan.
5. Write task entries with owner, status, acceptance criteria, and linked paths; do not put chat notes into `tasks.md`.
6. When design changes, update the design source of truth first, then sync task state and acceptance criteria.
7. Output drift checks: one conclusion has one source of truth, and other files reference it.

## Checks

- Responsibility: design doc, task board, and exec plan each have a clear role.
- Sync: task status matches current code and design decisions.
- Acceptance: every task has executable acceptance criteria.
- Granularity: tasks are small enough to verify and large enough to express user value.
- Pollution: `tasks.md` does not become a chat log or unordered TODO list.

## Output Format

```markdown
# Design Doc And Task Board Decision

## Where This Belongs
- Design doc:
- tasks.md:
- Exec plan:

## Update Order
- First:
- Then:
- Finally:

## Task Entries
-

## Acceptance Criteria
-

## Drift Checks
-
```

## Common Mistakes

- Putting task status into a design doc where it cannot be maintained.
- Updating only `tasks.md` while leaving the design source of truth stale.
- Opening a large exec plan for every small requirement.
- Writing tasks with no acceptance criteria, such as "improve" or "optimize."

## Example Prompts

- "Should this requirement live in a design doc or tasks.md?"
- "Turn this design into a task board and acceptance criteria."
- "Our tasks.md and design docs have drifted; how should we converge them?"
