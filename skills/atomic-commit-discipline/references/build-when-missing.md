# Build When Missing

Use this when a repository has no commit discipline beyond informal convention. Pattern sources include Conventional Commit policies, exact-path staging rules, task-state coupling, ledger coupling, and validation-before-commit checklists.

## Minimum Files

- Commit policy section in `AGENTS.md` or `CONTRIBUTING.md`.
- Task-state policy section in `tasks.md`, `docs/tasks.md`, or the repository's planning documentation.
- Optional `.github/pull_request_template.md`.
- Optional `docs/commit-checklist.md` if the policy is too long for the entrypoint.
- Optional CI commit-message or ledger-coupling checker.

## Bootstrap Steps

1. State that commits must be atomic: one logical purpose per commit.
2. Require reading `git status`, `git diff`, and `git diff --cached` before staging.
3. Require exact-path staging unless the worktree contains only the current change.
4. State the task coupling rule: when a commit completes, changes, or invalidates a tracked task, include the task-state update in the same logical commit.
5. Define the commit subject format, preferably Conventional Commits.
6. Define minimum validation evidence for docs, tests, implementation, harness, task-state, and ledger changes.

## Validation

- Before commit, confirm staged files match one logical group.
- Confirm task-state updates are included only when related to that logical group.
- Run the minimum validation command for that group.
- After commit, run `git show --stat --oneline HEAD` and `git status --short`.

## Do Not Include

- Permission to use `git add .` by default.
- A rule that every commit must have a task entry unless the repository explicitly requires it.
- Commit messages such as "fix" or "update" without behavioral detail.
- Rules that allow unrelated user changes to be staged silently.
