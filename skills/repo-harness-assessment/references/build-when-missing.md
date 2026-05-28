# Build When Missing

Use this when a repository has no clear harness inventory. Pattern sources include full harness repositories with root docs and checks, medium harness repositories with generated reports, and thin repositories that only have an entrypoint plus task board.

## Minimum Files

- `AGENTS.md` or equivalent agent entrypoint.
- `ARCHITECTURE.md` or `docs/architecture/index.md`.
- `docs/validation.md` or a validation section in README.
- `docs/harness-assessment.md` for the first inventory if no generated report exists.

## Bootstrap Steps

1. Inventory existing entrypoints, docs, scripts, CI, artifact directories, and ledgers.
2. Classify each harness layer as present, partial, or absent: entrypoint, planning, contracts, validation, runtime evidence, ledger, quality, commit discipline.
3. For absent layers, name the smallest artifact that would make the layer discoverable.
4. Write `docs/harness-assessment.md` with current state, gaps, and the next three slices.
5. Link the assessment from `AGENTS.md` or README so future agents can find it.

## Validation

- Run a docs/structure check if one exists.
- If no checker exists, verify that the assessment links to concrete files or explicitly says "absent".
- Confirm every recommended next slice names a file, command, or directory to create.

## Do Not Include

- Private URLs, credentials, account names, or environment-specific hosts.
- A full platform roadmap before the first minimum slice is justified.
- Product-specific workflow details copied from a pattern source.
