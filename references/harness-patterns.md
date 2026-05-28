# Harness Patterns Reference

This reference keeps shared vocabulary out of individual skills. Use it when a skill needs neutral names for common harness concepts without copying product-specific workflow.

## Core Layers

- Entrypoint: the first file an agent reads, usually `AGENTS.md` or an equivalent mirror.
- Source of truth: the versioned document or script that owns a decision.
- Contract: a rule that can be checked by script or review, usually with diff and audit modes.
- Validation surface: the commands that prove a change is safe enough for review.
- Runtime evidence: artifacts that connect visible behavior to backend, logs, traces, or provider calls.
- Ledger: a durable record of agent intent, changes, validation, risks, and linked commits.
- Quality garden: a small set of generated metrics and baselines used to freeze new degradation and reduce old debt.

## Neutral Artifact Names

- `AGENTS.md` for agent entrypoint rules.
- `docs/design/` for longer design decisions.
- `docs/exec-plans/` for multi-step implementation plans.
- `tasks.md` or `docs/tasks.md` for current work state.
- `artifacts/runs/<run_id>/` for runtime evidence bundles.
- `agent_chats/` or `agents_chat/` for collaboration ledgers.
- `scripts/check_*` or `scripts/doctor*` for local repository checks.

## Cross-Repo Pattern Matrix

These names come from pattern sources only. Do not require a target repository to copy every file.

| Shape | Pattern sources | Useful signals | Bootstrap bias |
| --- | --- | --- | --- |
| Full harness | ai-shifu, ai-video-studio | root entrypoint, architecture docs, validation scripts, runtime artifacts, ledgers, quality reports, CI gates | Add only the missing layer; avoid re-scaffolding the whole repo. |
| Medium harness | elab | docs split by architecture/runbooks/quality, generated reports, validation pipelines, baselines | Normalize indexes and commands before adding new layers. |
| Thin harness bootstrap | orion, elab-system | root entrypoint, task board, basic docs, partial scripts or deployment helpers | Create the smallest discoverable artifact and link it from the entrypoint. |

## Missing-File Construction Rule

If a skill asks an agent to search for a harness surface and that surface is absent, the agent must not stop at "missing." It must propose or create the minimum artifact described by the skill-local `references/build-when-missing.md`.

## Design Bias

- Start with the smallest useful slice.
- Freeze new drift before paying down historical debt.
- Prefer a clear script over a platform until the script stops being enough.
- Keep private URLs, credentials, account names, and environment assumptions out of reusable skills.
