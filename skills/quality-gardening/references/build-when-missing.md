# Build When Missing

Use this when quality is discussed but not measured. Pattern sources include `QUALITY_SCORE.md`, generated quality reports, harness baseline files, and scheduled gardening commands.

## Minimum Files

- `QUALITY_SCORE.md` or `docs/quality/QUALITY_SCORE.md`.
- `docs/generated/quality-report.md` or a generated Markdown report path.
- Optional JSON report under `docs/generated/` or `artifacts/`.
- Baseline or threshold file under `scripts/baselines/` or `scripts/harness-baselines/`.

## Bootstrap Steps

1. Choose four to eight automatically collectible metrics tied to structural risk.
2. Separate blocking gates from informational metrics.
3. Create thresholds or baselines so historical debt is visible but new degradation fails.
4. Generate a Markdown report for humans and JSON only if scripts need trend data.
5. Define a gardening cadence that lowers thresholds or removes allowlist entries gradually.

## Validation

- Run the report generator or manual collection command.
- Confirm every finding includes path, metric, current value, threshold, and suggested action.
- Confirm new degradation can be detected without forcing full historical cleanup.

## Do Not Include

- A single aggregate score that hides critical risk.
- Metrics that cannot be collected repeatably.
- One-off refactor plans presented as ongoing quality governance.
