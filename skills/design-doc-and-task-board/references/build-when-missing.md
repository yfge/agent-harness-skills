# Build When Missing

Use this when product intent and execution state live only in conversation. Pattern sources include task boards, design-doc directories, active/completed exec-plan directories, and docs indexes.

## Minimum Files

- `tasks.md` or `docs/tasks.md` for current work state.
- `docs/design/` or `docs/design-docs/` for durable decisions.
- `docs/exec-plans/active/` and `docs/exec-plans/completed/` for complex work.
- `docs/exec-plans/template.md` or an equivalent plan template.

## Bootstrap Steps

1. Create a task board with sections for in progress, backlog, completed, and acceptance criteria.
2. Create a design-doc directory and index if decisions need longer-lived explanation.
3. Create exec-plan directories only when the repository has multi-step or multi-day work.
4. Define update order: design source first, task state second, exec-plan status third.
5. Link planning files from README or `AGENTS.md`.

## Validation

- Confirm every active task has a status and acceptance criteria.
- Confirm design docs and task board do not duplicate the same decision as separate sources of truth.
- Confirm completed exec plans are archived or clearly marked.

## Do Not Include

- Chat logs as task board content.
- Vague tasks such as "improve" without acceptance criteria.
- Large exec-plan machinery for small one-file fixes.
