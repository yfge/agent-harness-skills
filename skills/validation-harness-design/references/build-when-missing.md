# Build When Missing

Use this when a repository has tests but no clear command surface. Pattern sources include repositories with `check_repo_harness.py`, `doctor.py`, validation pipelines, JSON reports, JUnit output, and CI gates.

## Minimum Files

- `scripts/check_repo_harness.py` or `scripts/doctor.py`.
- `docs/validation.md`, `docs/runbooks/validation.md`, or README validation section.
- CI workflow step that runs the minimum checker.
- Optional JSON/JUnit output directory under `artifacts/` for runtime or device checks.

## Bootstrap Steps

1. Inventory existing commands from manifests, Makefiles, scripts, and CI.
2. Create a change-type matrix: docs, contracts, unit/type/lint, runtime/browser/device.
3. Implement a minimum checker that validates required docs, command availability, and known generated artifacts.
4. Add stdout output for humans and stable JSON/JUnit only when automation will consume it.
5. Wire the minimum checker into CI before adding heavier runtime gates.

## Validation

- Run the minimum checker from a clean checkout or documented setup.
- Confirm docs-only changes do not require heavy runtime checks.
- Confirm runtime-sensitive changes have an escalation path beyond static checks.

## Do Not Include

- A single heavyweight command for every change type.
- Skip/fallback behavior that is not recorded.
- Provider credentials, account names, or machine-specific setup hidden in the checker.
