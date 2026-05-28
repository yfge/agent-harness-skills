---
name: runtime-evidence-and-tracing
description: Use when connecting browser, device, backend, logs, metrics, request IDs, run IDs, screenshots, traces, or artifacts into a runtime evidence loop.
---

# Runtime Evidence And Tracing

## Overview

Make runtime validation auditable by tying user-visible behavior to backend evidence through stable IDs and artifacts.

Agents should not only say they tested something; they should leave run IDs, request IDs, logs, screenshots, network records, or traces. For shared harness terms, see `../../references/harness-patterns.md`.

## When To Use

- The user mentions browser validation, device validation, request IDs, traces, logs, metrics, or artifacts.
- A production or test-environment issue must be traced from UI behavior to backend evidence.
- AI, provider, media, payment, or notification flows need classification as code failure, provider blocker, environment issue, or data problem.

## Inputs Needed

- Target flow, entry URL/API/device command.
- Existing logging, request wrapper, headers, and observability endpoints.
- Artifact directory and run ID naming preference.

## Execution Order

- First: Find the request entrypoint and existing request/log/trace propagation points.
- Then: Design run IDs, request IDs, artifact bundles, and collection commands.
- Finally: Output the evidence contract and validation path, including fallback and blocker classification.

## Step-by-Step Process

1. Search frontend API wrappers, backend request middleware, logs, metrics, and trace scripts.
2. Confirm whether UI/client code can generate or propagate `X-Request-ID` and `X-Harness-Run-ID`.
3. Design `artifacts/runs/<run_id>/` with manifest, summary, logs, network, screenshots, and trace files.
4. Define the collection order for the target flow: start, authenticate if needed, operate, wait, read artifacts, and attribute the result.
5. Define blocker categories: code regression, environment unavailable, provider quota/billing, data missing, and not evaluable.
6. Explain how PRs or ledgers should reference artifacts without committing large temporary files.

## Checks

- Propagation: request ID and run ID remain searchable across frontend, backend, workers, and provider calls.
- Artifact: the directory includes manifest, summary, and reproducible commands.
- Evidence: screenshots, console, network, logs, and metrics cover the failure boundary.
- Attribution: provider or environment blockers are not reported as product-quality failures.
- Privacy: artifacts do not contain tokens, phone numbers, real secrets, or sensitive payloads.

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

- Keeping only screenshots with no request ID or backend evidence.
- Creating traces only on the backend, leaving browser errors disconnected.
- Treating provider balance or quota issues as product-quality failures.
- Committing large artifacts instead of referencing paths and summaries.

## Example Prompts

- "Connect browser validation to backend request IDs."
- "Design artifacts/runs evidence for this AI generation workflow."
- "How should this failure be classified: code, environment, or provider blocker?"
