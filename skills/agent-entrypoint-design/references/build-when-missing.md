# Build When Missing

Use this when a repository has no usable agent entrypoint. Pattern sources include source-of-truth `AGENTS.md` files, symlink/mirror policies, and subtree overrides in larger repositories.

## Minimum Files

- Root `AGENTS.md`.
- Optional mirrors: `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, or `.github/instructions/*`.
- Optional subtree `AGENTS.md` only where a directory has stricter local rules.

## Bootstrap Steps

1. Create a root `AGENTS.md` that states scope, source-of-truth docs, do/avoid rules, validation commands, and commit policy.
2. Declare instruction precedence: system/developer, user, nearest agent file, linked docs.
3. Add a mirror policy: symlink, exact copy with generation marker, or explicit "read AGENTS.md first" pointer.
4. Add only high-signal navigation; link deeper docs instead of embedding long procedures.
5. Add a drift check if mirrors are generated or exact-copy files.

## Validation

- Confirm an agent can identify first-read docs, edit boundaries, and minimum validation in under one minute.
- Run the mirror/drift checker if present.
- If no checker exists, compare mirror contents or symlink targets manually.

## Do Not Include

- Product secrets, credentials, local machine paths, or private environment assumptions.
- Long project encyclopedia content that belongs in architecture or runbook docs.
- Business-specific requirements that should live in design docs or task boards.
