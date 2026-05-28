---
name: design-doc-and-task-board
description: Use when deciding how requirements should be captured in design docs, tasks.md, exec plans, acceptance criteria, status updates, or planning source-of-truth files.
---

# Design Doc And Task Board

## Overview

English summary: decide where intent, design, execution tasks, and acceptance criteria should live so they do not drift.

本 skill 负责做事前和做事中的计划事实源：设计文档讲“为什么和怎么设计”，`tasks.md` 讲“当前做什么和状态”，exec plan 讲“如何执行一批复杂改动”。

## When To Use

- 用户问“这个需求应该写 design doc 还是 tasks.md”。
- 项目同时有 README、design docs、tasks、exec plans，内容开始漂移。
- 需要把需求拆成任务、状态、验收标准和变更记录。

## Inputs Needed

- 当前需求或变更目标。
- 现有 `tasks.md`、设计文档、exec plans、README/docs index。
- 需求规模、跨模块范围和是否需要长期追踪。

## Execution Order

- First: 读取现有计划事实源，确认当前项目使用哪些文件表达 intent 和状态。
- Then: 判断本需求应该落在 design doc、task board、exec plan 还是组合。
- Finally: 输出文档/任务同步方案、验收标准和更新顺序。

## Step-by-Step Process

1. 搜索 `tasks.md`、`PLANS.md`、`docs/design*`、`docs/exec-plans`、README。
2. 识别每类文件的实际职责，不按名字臆测。
3. 按复杂度分类：小修只更新 task；架构/跨模块先 design doc；多日多步骤用 exec plan。
4. 为任务写清 owner/status/acceptance/linked paths，不把聊天备忘录塞进 `tasks.md`。
5. 当设计变化时，先改设计事实源，再同步任务状态和验收标准。
6. 输出防漂移检查：同一结论只能有一个 source of truth，其他文件引用它。

## Checks

- 职责检查：design doc、task board、exec plan 是否各司其职。
- 同步检查：任务状态是否匹配当前代码和设计结论。
- 验收检查：每个任务是否有可执行 acceptance criteria。
- 粒度检查：任务是否小到可以验证，大到足以表达用户价值。
- 防污染检查：`tasks.md` 不应变成聊天日志或无序 TODO。

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

- 把任务状态写进设计文档，后续无法维护。
- 只改 `tasks.md`，不改已经过时的设计事实源。
- 每个需求都开大型 exec plan，拖慢小改动。
- 任务没有验收标准，只写“优化”“完善”。

## Example Prompts

- "这个需求应该写 design doc 还是 tasks.md？"
- "把这个设计拆成任务板和验收标准。"
- "我们的 tasks.md 和设计文档漂移了，怎么收敛？"
