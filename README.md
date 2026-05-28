# Agent Harness Skills

Reusable skills for designing agent-first repository harnesses: entrypoints, repo contracts, validation commands, runtime evidence, agent ledgers, quality gardening, task boards, design docs, and atomic commits.

## Included Skills

- `repo-harness-assessment`: assess a repository's current agent/harness maturity and identify the smallest useful next slice.
- `agent-entrypoint-design`: design `AGENTS.md`, mirrored agent files, instruction precedence, and source-of-truth navigation.
- `repo-contracts-and-boundaries`: turn architecture and directory boundaries into mechanical checks, baselines, and allowlists.
- `validation-harness-design`: design repo validation entrypoints, test matrix, JSON/JUnit outputs, and CI gates.
- `runtime-evidence-and-tracing`: design run IDs, request IDs, artifact bundles, browser/device/backend traces, and failure evidence.
- `agent-ledger-and-delivery`: design collaboration ledgers and PR/delivery evidence summaries.
- `quality-gardening`: design quality snapshots, structural metrics, debt thresholds, and generated quality reports.
- `design-doc-and-task-board`: coordinate design documents, `tasks.md`, exec plans, status updates, and acceptance criteria.
- `atomic-commit-discipline`: split work into minimal commits, verify diffs, run scoped checks, and keep related evidence together.

## Repository Layout

```text
skills/
  <skill-name>/SKILL.md
scripts/
  validate_skill_quality.py
```

## Validation

```bash
python3 scripts/validate_skill_quality.py
```

## Usage

Install or point your agent runtime at this repository's `skills/` directory. These skills are designed to compose with broader development workflows such as brainstorming, planning, debugging, TDD, and verification.

Use this repository when you want an agent to answer questions like:

- "What harness pieces is this repo missing?"
- "How should this project structure AGENTS.md and validation commands?"
- "How do we connect browser evidence to backend request traces?"
- "Should this requirement live in tasks.md, a design doc, or an exec plan?"
- "How should these changes be split into atomic commits?"
