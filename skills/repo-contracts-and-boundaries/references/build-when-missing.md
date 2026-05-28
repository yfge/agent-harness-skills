# Build When Missing

Use this when architecture intent exists only in conversations or conventions. Pattern sources include repositories with `ARCHITECTURE.md`, contract docs, diff/audit checkers, generated baselines, and allowlists.

## Minimum Files

- `ARCHITECTURE.md` or `docs/architecture/index.md`.
- `docs/architecture/contracts.md` or a contract section in the architecture doc.
- `scripts/check_repo_contracts.py` or similarly named standard-library checker.
- Baseline or allowlist file under `docs/generated/`, `scripts/baselines/`, or `scripts/harness-baselines/`.

## Bootstrap Steps

1. Write the architecture map: main surfaces, dependency direction, known choke points, and allowed ownership boundaries.
2. Choose two or three rules that can be checked mechanically before adding more.
3. Create a checker with `--mode diff` for changed files and `--mode audit` for the full repository.
4. Put historical violations in a baseline or allowlist with owner, reason, and repayment note.
5. Make new violations fail while historical debt remains visible.

## Validation

- Run diff mode against changed files.
- Run audit mode and confirm historical findings are reported without blocking unexpectedly.
- Verify failure messages include path, rule, reason, and suggested direction.

## Do Not Include

- Rules that cannot be checked or reviewed consistently.
- A baseline that silently hides all debt without a report.
- Product-specific ports, service names, or private deployment paths from pattern sources.
