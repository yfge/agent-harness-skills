# Build When Missing

Use this when a repository has no commit discipline beyond informal convention. Pattern sources include Conventional Commit policies, exact-path staging rules, ledger coupling, and validation-before-commit checklists.

## Minimum Files

- Commit policy section in `AGENTS.md` or `CONTRIBUTING.md`.
- Optional `.github/pull_request_template.md`.
- Optional `docs/commit-checklist.md` if the policy is too long for the entrypoint.
- Optional CI commit-message or ledger-coupling checker.

## Bootstrap Steps

1. State that commits must be atomic: one logical purpose per commit.
2. Require reading `git status`, `git diff`, and `git diff --cached` before staging.
3. Require exact-path staging unless the worktree contains only the current change.
4. Define the commit subject format, preferably Conventional Commits.
5. Define minimum validation evidence for docs, tests, implementation, harness, and ledger changes.

## Validation

- Before commit, confirm staged files match one logical group.
- Run the minimum validation command for that group.
- After commit, run `git show --stat --oneline HEAD` and `git status --short`.

## Do Not Include

- Permission to use `git add .` by default.
- Commit messages such as "fix" or "update" without behavioral detail.
- Rules that allow unrelated user changes to be staged silently.
