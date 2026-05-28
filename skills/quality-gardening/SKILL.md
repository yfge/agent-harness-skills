---
name: quality-gardening
description: Use when designing quality snapshots, generated quality reports, structural metrics, debt thresholds, regression budgets, quality gates, or gradual cleanup loops.
---

# Quality Gardening

## Overview

English summary: track quality as concrete metrics and debt movement, not as a vague single score.

本 skill 用来做质量治理：先冻结新增劣化，再用可生成的指标表达质量状态和收敛方向。

## When To Use

- 用户提到 `QUALITY_SCORE.md`、quality report、质量快照、债务收敛、红线。
- 仓库需要结构质量指标而不是只靠 lint/test。
- 需要定期 garden，不想一次性大重构。

## Inputs Needed

- 当前质量痛点：大文件、散点事件、直接 API 调用、重复入口、缺测试等。
- 可扫描的源码路径和应排除路径。
- CI 或定期运行方式。

## Execution Order

- First: 找到现有质量文档、生成报告、lint 和 baseline。
- Then: 选少量可追踪指标和阈值，不做虚假总分。
- Finally: 输出质量报告结构、门禁策略和收敛节奏。

## Step-by-Step Process

1. 搜索 `QUALITY_SCORE.md`、quality scripts、baseline、CI gardening workflow。
2. 选择 4 到 8 个指标，每个指标必须能自动采集。
3. 区分 blocking gate 和 informational report。
4. 为历史问题设置阈值或 baseline，新增劣化应 fail。
5. 生成 Markdown 给人读，JSON 给脚本和趋势使用。
6. 设计 garden 节奏：每次小幅降低阈值或关闭一个 allowlist。

## Checks

- 指标检查：是否可重复生成，是否真的反映结构风险。
- 阈值检查：是否冻结新增劣化，而不是要求一次性还清旧债。
- 报告检查：是否列出 path、metric、current、threshold、suggested action。
- CI 检查：哪些指标 fail build，哪些只生成报告。
- 反激励检查：不要用单一分数掩盖关键风险。

## Output Format

```markdown
# Quality Gardening

## Metrics
| Metric | Source | Threshold | Gate |
| --- | --- | --- | --- |

## Generated Reports
-

## Baseline Policy
-

## Garden Loop
-

## Non-Goals
-
```

## Common Mistakes

- 发明一个好看的总分，却无法指导修复。
- 指标太多，没人看也没人修。
- 没有 baseline，导致质量门禁从第一天就不可用。
- 把一次性重构当成质量治理。

## Example Prompts

- "给这个 repo 设计 QUALITY_SCORE.md 和 quality-report。"
- "How should we track structural debt without inventing a fake score?"
- "把这些历史大文件和散点调用纳入 quality garden。"
