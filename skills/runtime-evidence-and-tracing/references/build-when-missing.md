# Build When Missing

Use this when runtime validation is not auditable. Use generic run artifacts, request IDs, interaction evidence, trace scripts, log queries, and external-blocker classification.

## Minimum Files

- `artifacts/runs/<run_id>/manifest.json` or equivalent manifest.
- `artifacts/runs/<run_id>/summary.md` for human-readable result and classification.
- `scripts/harness/trace_run.py`, `scripts/harness/doctor.py`, or a documented collection command.
- A request/run ID policy in `RELIABILITY.md`, README, or a runbook.

## Bootstrap Steps

1. Define run ID and request ID names; prefer headers such as `X-Harness-Run-ID` and `X-Request-ID` where HTTP is involved.
2. Create a run directory structure with manifest, summary, logs, screenshots, network traces, and metrics slots.
3. Add a minimal collection command that writes manifest and summary even when deeper logs are unavailable.
4. Define failure classification: code regression, environment unavailable, external dependency blocker, data missing, not evaluable.
5. Require PR or ledger summaries to reference artifact path and classification.

## Validation

- Run one smoke collection and confirm manifest plus summary are written.
- Confirm the same run ID appears in available caller, service, worker, or external dependency evidence.
- Confirm artifacts are referenced but not committed when large or sensitive.

## Do Not Include

- Tokens, real user identifiers, contact details, dependency keys, or sensitive payloads.
- Claims of runtime validation without evidence of the actual path used.
- Large binary artifacts in normal source commits unless the repository explicitly allows them.
