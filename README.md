# Agent Harness Skills

Reusable skills for turning real software repositories into agent-ready engineering environments.

Agent Harness Skills helps teams build the repo-side control layer that coding agents need: clear entrypoints, explicit boundaries, runnable validation, runtime evidence, and reviewable delivery records.

## What It Is

Agent Harness Skills is a reusable skill library for designing repository harnesses.

A repository harness is the engineering layer around a codebase that tells an agent where to start, which rules matter, what boundaries it must respect, how to prove a change is safe, and what evidence should be left behind for review. It is not a separate product runtime. It is the control layer that makes an existing repository easier for agents and humans to operate together.

Use it when a project has grown beyond "read the README and run the tests" and needs a more explicit way for agents to navigate source-of-truth documents, validation commands, runtime traces, quality gates, and delivery records.

## Why It Exists

Coding agents can edit files quickly, but real repositories need more than fast edits. They need a stable operating surface.

Without a harness, an agent has to infer too much: which document is authoritative, which directories are owned by which subsystem, which checks are meaningful, whether a browser failure maps to a backend error, and what evidence belongs in a PR. That creates drift, repeated rediscovery, weak validation, and delivery summaries that cannot be audited.

Agent Harness Skills turns those expectations into reusable repository practices. The goal is not to add ceremony. The goal is to make the important work discoverable, executable, and reviewable.

## What It Helps Agents Do

- Find the correct entrypoint and source of truth before making changes.
- Understand architecture, ownership, and dependency boundaries.
- Choose the validation surface that actually proves a change.
- Connect visible runtime behavior to logs, traces, request IDs, screenshots, and artifacts.
- Separate code regressions from environment, provider, data, or quota blockers.
- Leave concise delivery records through commits, PR notes, ledgers, and handoffs.
- Improve quality incrementally without turning every task into a broad refactor.

## Included Skills

The skills form a capability map for building and improving an agent-ready repository:

- `repo-harness-assessment`: assess a repository's current agent/harness maturity and identify the smallest useful next slice.
- `agent-entrypoint-design`: design `AGENTS.md`, mirrored agent files, instruction precedence, and source-of-truth navigation.
- `repo-contracts-and-boundaries`: turn architecture and directory boundaries into mechanical checks, baselines, and allowlists.
- `validation-harness-design`: design repo validation entrypoints, test matrix, JSON/JUnit outputs, and CI gates.
- `runtime-evidence-and-tracing`: design run IDs, request IDs, artifact bundles, browser/device/backend traces, and failure evidence.
- `agent-ledger-and-delivery`: design collaboration ledgers and PR/delivery evidence summaries.
- `quality-gardening`: design quality snapshots, structural metrics, debt thresholds, and generated quality reports.
- `design-doc-and-task-board`: coordinate design documents, `tasks.md`, exec plans, status updates, and acceptance criteria.
- `atomic-commit-discipline`: split work into minimal commits, verify diffs, run scoped checks, and keep related evidence together.

## When To Use

Use this repository when you want to:

- Prepare a repository for agent-driven engineering work.
- Turn scattered docs, scripts, and conventions into a navigable harness.
- Design `AGENTS.md` and related entrypoints so agents know where to start.
- Add validation gates that are useful locally and reusable in CI.
- Connect browser, device, backend, and provider evidence into runtime artifact bundles.
- Create durable delivery records for PRs, commits, handoffs, and follow-up work.

It is especially useful when a repository already has product code, tests, and scripts, but agents still lose time rediscovering rules, guessing boundaries, or reporting work without enough evidence.

## What It Is Not

- It is not a product template or business scaffold.
- It is not a private workflow bundle copied from one team or project.
- It is not a replacement for project-specific architecture decisions.
- It is not only a test harness; tests are one part of the validation surface.
- It is not a platform requirement; a small script or document is often the right first layer.

## Usage

Install or point your agent runtime at this repository's `skills/` directory.

Use this repository when you want an agent to answer questions like:

- "What harness pieces is this repo missing?"
- "How should this project structure `AGENTS.md` and validation commands?"
- "How do we connect browser evidence to backend request traces?"
- "Should this requirement live in `tasks.md`, a design doc, or an exec plan?"
- "How should these changes be split into atomic commits?"

## Repository Layout

```text
skills/
  <skill-name>/SKILL.md
docs/
  scenario-tests.md
references/
  harness-patterns.md
scripts/
  check_skill_closure.py
  check_skill_language.py
  validate_skill_quality.py
```

## Validation

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skill_quality.py
python3 scripts/check_skill_language.py
python3 scripts/check_skill_closure.py
```

For substantial skill wording changes, record at least one realistic prompt and observed output in `docs/scenario-tests.md`.
