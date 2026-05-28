# Build When Missing

Use this when agent work has no durable delivery record. Pattern sources include `agent_chats/` and `agents_chat/` directories with date-based records, validation sections, linked tasks, and linked commits.

## Minimum Files

- `agent_chats/` or `agents_chat/` directory.
- `.gitkeep` if the directory would otherwise be empty.
- `docs/agent-ledger-template.md` or a template section in `AGENTS.md`.
- Optional CI checker only after the policy is stable.

## Bootstrap Steps

1. Choose one ledger directory name and document that no parallel format should be created.
2. Define filename format such as `YYYY/MM/DD/YYYY-MM-DDTHH-MM-SSZ-topic.md`.
3. Define required sections: user prompt, goals, changes, validation, risks or next steps, linked tasks, and linked commits.
4. Define coupling: per commit, per review, per session, or per milestone.
5. Add skip policy for trivial or emergency changes, including how to record the skip reason.

## Validation

- Create or inspect one sample record and confirm all required sections exist.
- Confirm validation commands and artifact paths in the record match what actually ran.
- Confirm the ledger references task state without replacing the authoritative task surface.
- If CI exists, confirm code changes that require ledgers are detected.

## Do Not Include

- Raw private chat transcripts, secrets, credentials, or sensitive logs.
- Two competing ledger directory names unless one is explicitly deprecated.
- Task-status ownership that belongs in `tasks.md`, an issue tracker, or another work-state surface.
- Commit-splitting rules that belong in atomic commit discipline.
