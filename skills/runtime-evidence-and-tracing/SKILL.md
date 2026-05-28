---
name: runtime-evidence-and-tracing
description: Use when connecting browser, device, backend, logs, metrics, request IDs, run IDs, screenshots, traces, or artifacts into a runtime evidence loop.
---

# Runtime Evidence And Tracing

## Overview

English summary: make runtime validation auditable by tying user-visible behavior to backend evidence through stable IDs and artifacts.

本 skill 负责运行态证据闭环。它要求 agent 不能只说“我测了”，而要能交出 run id、request id、日志、截图、网络或 trace。

## When To Use

- 用户提到浏览器验证、真机验证、request id、trace、logs、metrics、artifact。
- 线上/测试环境问题需要从 UI 行为追到后端证据。
- AI/provider/media/支付/通知等流程需要判定是业务失败、provider blocker 还是环境问题。

## Inputs Needed

- 目标流程、入口 URL/API/device command。
- 现有日志、请求封装、headers、observability endpoints。
- artifact 存放目录和 run id 命名偏好。

## Execution Order

- First: 找到请求入口和现有 request/log/trace 传播点。
- Then: 设计 run id、request id、artifact bundle 和采集命令。
- Finally: 输出证据契约和验证路径，明确 fallback 与 blocker 分类。

## Step-by-Step Process

1. 搜索 frontend API wrapper、backend request middleware、logs、metrics、trace scripts。
2. 确认 UI/client 是否能生成或透传 `X-Request-ID`、`X-Harness-Run-ID`。
3. 设计 `artifacts/runs/<run_id>/` 结构：manifest、summary、logs、network、screenshots、trace。
4. 为目标流程定义采集顺序：启动/登录/操作/等待/读取 artifact/归因。
5. 定义 blocker 分类：code regression、environment unavailable、provider quota/billing、data missing、not evaluable。
6. 输出如何在 PR 或 ledger 中引用 artifact，而不是提交大型临时文件。

## Checks

- 传播检查：request id/run id 是否跨 frontend、backend、worker、provider call 保持可查。
- artifact 检查：目录是否包含 manifest 和 summary，是否能复现命令。
- 证据检查：截图、console、network、logs、metrics 是否覆盖失败边界。
- 归因检查：provider/环境 blocker 不能写成质量失败。
- 隐私检查：artifact 不应包含 token、手机号、真实密钥或敏感 payload。

## Output Format

```markdown
# Runtime Evidence And Tracing

## ID Contract
- Run ID:
- Request ID:
- Header propagation:

## Artifact Bundle
-

## Collection Flow
1.
2.
3.

## Failure Classification
-

## PR / Ledger Reference
-
```

## Common Mistakes

- 只有截图，没有 request id 或 backend evidence。
- trace 只在后端存在，浏览器错误无法带回同一条链。
- 把 provider 余额/配额问题归为产品质量问题。
- 提交大体积 artifact 到仓库，而不是引用路径和摘要。

## Example Prompts

- "把浏览器验证和后端 request id 串起来。"
- "Design artifacts/runs evidence for this AI generation workflow."
- "这个失败应该怎么分类：代码、环境还是 provider blocker？"
