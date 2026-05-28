# Agent Harness Skills

Reusable skills for turning real software repositories into agent-ready engineering environments.

Agent Harness Skills helps teams build the repo-side control layer that coding agents need: clear entrypoints, explicit boundaries, runnable validation, runtime evidence, and reviewable delivery records.

## Repository

Canonical Git remote:

```bash
git@github.com:yfge/agent-harness-skills.git
```

Use this remote for git-backed installs and for publishing repository updates. A local clone path can still be used anywhere the installation examples accept `<repo-url-or-local-path>`.

## What It Is

Agent Harness Skills is a reusable skill library for designing repository harnesses.

A repository harness is the engineering layer around a codebase that tells an agent where to start, which rules matter, what boundaries it must respect, how to prove a change is safe, and what evidence should be left behind for review. It is not a separate product runtime. It is the control layer that makes an existing repository easier for agents and humans to operate together.

Use it when a project has grown beyond "read the README and run the tests" and needs a more explicit way for agents to navigate source-of-truth documents, validation commands, runtime traces, quality gates, and delivery records.

## Why It Exists

Coding agents can edit files quickly, but real repositories need more than fast edits. They need a stable operating surface.

Without a harness, an agent has to infer too much: which document is authoritative, which directories are owned by which subsystem, which checks are meaningful, whether an observed failure maps to a runtime error, and what evidence belongs in a PR. That creates drift, repeated rediscovery, weak validation, and delivery summaries that cannot be audited.

Agent Harness Skills turns those expectations into reusable repository practices. The goal is not to add ceremony. The goal is to make the important work discoverable, executable, and reviewable.

## What It Helps Agents Do

- Find the correct entrypoint and source of truth before making changes.
- Understand architecture, ownership, and dependency boundaries.
- Choose the validation surface that actually proves a change.
- Connect observed runtime behavior to logs, traces, request IDs, screenshots, and artifacts.
- Separate code regressions from environment, external dependency, data, or quota blockers.
- Leave concise delivery records through commits, PR notes, ledgers, and handoffs.
- Improve quality incrementally without turning every task into a broad refactor.

## Included Skills

The skills form a capability map for building and improving an agent-ready repository:

- `repo-harness-assessment`: assess a repository's current agent/harness maturity and identify the smallest useful next slice.
- `agent-entrypoint-design`: design `AGENTS.md`, mirrored agent files, instruction precedence, and source-of-truth navigation.
- `repo-contracts-and-boundaries`: turn architecture and directory boundaries into mechanical checks, baselines, and allowlists.
- `validation-harness-design`: design repo validation entrypoints, test matrix, JSON/JUnit outputs, and CI gates.
- `runtime-evidence-and-tracing`: design run IDs, request IDs, artifact bundles, runtime traces, and failure evidence.
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
- Connect observed behavior, runtime signals, external dependency results, and logs into artifact bundles.
- Create durable delivery records for PRs, commits, handoffs, and follow-up work.

It is especially useful when a repository already has product code, tests, and scripts, but agents still lose time rediscovering rules, guessing boundaries, or reporting work without enough evidence.

## What It Is Not

- It is not a product template or business scaffold.
- It is not a private workflow bundle copied from one team or project.
- It is not a replacement for project-specific architecture decisions.
- It is not only a test harness; tests are one part of the validation surface.
- It is not a platform requirement; a small script or document is often the right first layer.

## Installation

Installation differs by agent runtime. If you use more than one agent, install Agent Harness Skills separately for each one.

Use one of two patterns:

- Packaged install: use the metadata files in this repo when the agent runtime supports plugins or extensions.
- Skills-path install: point the agent runtime directly at this repository's `skills/` directory.

In the examples below, replace `<repo-url-or-local-path>` with this repository's git URL (`git@github.com:yfge/agent-harness-skills.git`) or an absolute local path to the repository root.

### Generic Skills Directory

Use this fallback for any agent runtime that supports an explicit skills path:

```text
<repo-url-or-local-path>/skills
```

Verify by asking the agent to list or load the `repo-harness-assessment` skill.

### Codex CLI And Codex App

This repository includes `.codex-plugin/plugin.json`, which exposes `./skills/` as a Codex plugin.

- For a packaged or marketplace install, install `agent-harness-skills` through the Codex plugin UI or `/plugins` flow once the repository is published in that channel.
- For local development, register this repository as a local plugin source or through a personal marketplace entry that points to the repository root.
- Verify by asking Codex to use `repo-harness-assessment` on a repository.

### Claude Code

This repository includes `.claude-plugin/plugin.json` for Claude Code plugin packaging.

- Install from the plugin marketplace once published, or use Claude Code's local/plugin-from-repository workflow for this repository.
- Verify by asking Claude Code to load `repo-harness-assessment` or assess a repository's harness maturity.

### Cursor

This repository includes `.cursor-plugin/plugin.json`, with `skills` set to `./skills/`.

- Install from the Cursor plugin marketplace once published, or add this repository through Cursor's plugin flow.
- Verify by asking Cursor to list available skills or load `repo-harness-assessment`.

### Gemini CLI

This repository includes `gemini-extension.json` and `GEMINI.md`.

Install the extension from a git URL or local path:

```bash
gemini extensions install git@github.com:yfge/agent-harness-skills.git
```

Gemini loads `GEMINI.md`, which points it to `INDEX.md` for skill routing. Verify by asking Gemini which Agent Harness Skills are available.

### OpenCode

This repository includes an OpenCode plugin entrypoint at `.opencode/plugins/agent-harness-skills.js`.

For a local clone, add the repository root to the `plugin` array in your global or project-level `opencode.json`:

```json
{
  "plugin": ["/absolute/path/to/agent-harness-skills"]
}
```

For a git-backed install:

```json
{
  "plugin": ["agent-harness-skills@git+ssh://git@github.com/yfge/agent-harness-skills.git"]
}
```

Restart OpenCode, then verify with:

```text
use skill tool to list skills
use skill tool to load repo-harness-assessment
```

See `docs/README.opencode.md` for the longer OpenCode guide.

## Usage

Install through the runtime-specific path above, or point your agent runtime at this repository's `skills/` directory.

Use this repository when you want an agent to answer questions like:

- "What harness pieces is this repo missing?"
- "How should this project structure `AGENTS.md` and validation commands?"
- "How do we connect observed behavior to request traces?"
- "Should this requirement live in `tasks.md`, a design doc, or an exec plan?"
- "How should these changes be split into atomic commits?"

## Repository Layout

```text
.codex-plugin/
  plugin.json
.claude-plugin/
  plugin.json
.cursor-plugin/
  plugin.json
.opencode/
  INSTALL.md
  plugins/agent-harness-skills.js
GEMINI.md
gemini-extension.json
skills/
  <skill-name>/SKILL.md
docs/
  README.opencode.md
  scenario-tests.md
references/
  harness-patterns.md
scripts/
  check_skill_closure.py
  check_skill_language.py
  check_reference_neutrality.py
  validate_skill_quality.py
```

## Validation

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skill_quality.py
python3 scripts/check_skill_language.py
python3 scripts/check_skill_closure.py
python3 scripts/check_reference_neutrality.py
```

For substantial skill wording changes, record at least one realistic prompt and observed output in `docs/scenario-tests.md`.
