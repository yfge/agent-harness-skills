# Agent Harness Skills For OpenCode

Use this guide when installing Agent Harness Skills in OpenCode.

## What The OpenCode Plugin Does

The OpenCode plugin registers this repository's `skills/` directory through OpenCode's config hook. It does not inject extra workflow instructions, run commands, or change project files.

## Installation

Use a local clone:

```json
{
  "plugin": ["/absolute/path/to/agent-harness-skills"]
}
```

Or use a git-backed plugin entry:

```json
{
  "plugin": ["agent-harness-skills@git+ssh://git@github.com/yfge/agent-harness-skills.git"]
}
```

Restart OpenCode after changing `opencode.json`.

## Usage

List available skills:

```text
use skill tool to list skills
```

Load a skill:

```text
use skill tool to load repo-harness-assessment
```

Start with `repo-harness-assessment` for an existing repository, then use `INDEX.md` for routing across the other harness skills.

## Troubleshooting

- If no skills appear, confirm the plugin path points to the repository root.
- If the plugin does not load, confirm `package.json` points to `.opencode/plugins/agent-harness-skills.js`.
- If a skill fails to load, run the repository validation commands from the root README.
