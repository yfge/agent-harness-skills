# Skill Index

## Recommended Composition

1. `repo-harness-assessment` - start here for an existing repo; map existing artifacts to roles before recommending new files.
2. `agent-entrypoint-design` - define how agents discover rules and source-of-truth docs.
3. `design-doc-and-task-board` - decide how product/design intent becomes tracked work state.
4. `repo-contracts-and-boundaries` - encode structural limits and drift prevention.
5. `validation-harness-design` - define command surfaces and CI gates.
6. `runtime-evidence-and-tracing` - connect runtime failures to evidence artifacts.
7. `agent-ledger-and-delivery` - record collaboration evidence and delivery summaries without replacing task state.
8. `quality-gardening` - track quality as generated metrics and debt movement.
9. `atomic-commit-discipline` - finish work in minimal, reviewable commits with related task-state updates.

## Routing Notes

- Use `repo-harness-assessment` when the user asks what a repo is missing.
- Use `references/harness-profiles.json` to choose the lightest appropriate role set for the repository archetype.
- Include `Detected Mapping` in skill outputs so existing issue trackers, review templates, validation commands, reports, or artifact systems can stand in for default file names.
- Use `agent-entrypoint-design` when the user mentions `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Cursor rules, GitHub instructions, or source-of-truth navigation.
- Use `design-doc-and-task-board` when the user asks where requirements, design docs, `tasks.md`, external task systems, or exec plans should live.
- Use `repo-contracts-and-boundaries` when the user asks to protect architecture, layering, dependency direction, ownership, baselines, or allowlists.
- Use `validation-harness-design` when the user asks for validation commands, doctor scripts, test matrices, CI gates, smoke checks, JSON, or JUnit outputs.
- Use `runtime-evidence-and-tracing` when the user mentions runtime evidence, request IDs, run IDs, logs, traces, screenshots, external dependency evidence, or artifacts.
- Use `agent-ledger-and-delivery` when the user asks for agent work records, review evidence, delivery summaries, linked tasks or commits, validation notes, or handoff records.
- Use `quality-gardening` when the user asks for quality snapshots, generated reports, structural metrics, debt thresholds, regression budgets, or cleanup loops.
- Use `atomic-commit-discipline` when the user asks to commit, split changes, stage paths, include task-state updates, or avoid unrelated work.
