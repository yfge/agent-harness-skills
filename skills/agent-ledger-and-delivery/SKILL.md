---
name: agent-ledger-and-delivery
description: Use when designing agent_chats or agents_chat records, PR evidence, delivery summaries, linked commits, validation notes, risks, or handoff records.
---

# Agent Ledger And Delivery

## Overview

Define how agent work is recorded so reviewers can see prompt, intent, changes, validation, risks, and linked commits.

This skill focuses on delivery evidence and long-term traceability, not commit splitting. For shared harness terms, see `../../references/harness-patterns.md`.

## When To Use

- The user mentions `agent_chats`, `agents_chat`, PR descriptions, delivery records, or linked commits.
- A project requires AI collaboration records for each delivery.
- Validation, risk, next steps, and artifact references need a stable format.

## Inputs Needed

- Existing ledger directory and naming rules.
- User goal, change summary, validation commands, artifacts, PR, or commits.
- Whether the repository requires ledger updates in the same commit.

## Execution Order

- First: Read existing ledger rules and recent examples.
- Then: Design the record schema, naming, required sections, and commit/PR coupling.
- Finally: Output a reusable ledger template and delivery checklist.

## Step-by-Step Process

1. Search for `agent_chats`, `agents_chat`, CI checks, AGENTS rules, and PR templates.
2. Confirm record granularity: per commit, per PR, per session, or per milestone.
3. Define filename, frontmatter, body sections, language, and redaction rules.
4. Define when ledger updates are required, when skip is allowed, and how skip is recorded.
5. Define how PR summaries reference commits, validation, artifacts, risks, and next steps.
6. Keep ledger and atomic commit rules separate: this skill defines records; `atomic-commit-discipline` defines commit splitting.

## Checks

- Completeness: prompt, goals, changes, validation, risks, and linked commits are present.
- Coupling: code changes have a corresponding ledger or explicit skip reason.
- Readability: future agents can resume from the record; it is not just "done."
- Privacy: records do not include tokens, secrets, private chat transcripts, or sensitive logs.
- Duplication: avoid two ledger formats that drift from each other.

## Output Format

```markdown
# Agent Ledger And Delivery

## Ledger Policy
- Directory:
- Filename:
- Required metadata:
- Required sections:

## Delivery Summary Template
-

## Commit / PR Coupling
-

## Validation Evidence
-

## Skip Policy
-
```

## Common Mistakes

- Writing a diary instead of validation and risk evidence.
- Letting the PR summary disagree with actual validation.
- Mixing atomic commit rules into the ledger skill until responsibilities overlap.
- Recording sensitive content.

## Example Prompts

- "Design an agents_chat record policy for this project."
- "Make a PR evidence template for this agent-driven repo."
- "What validation and linked commits should this delivery record include?"
