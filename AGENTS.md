# Agent Harness Skills - Repository Instructions

## Purpose

This repository contains reusable skills for building agent-first harnesses across software projects. Keep the skills general-purpose: they should help an agent assess, design, validate, and deliver repo harness work without copying any single product's private workflow.

## Rules

- Keep each skill in `skills/<skill-name>/SKILL.md`.
- Skill folder names and frontmatter `name` values must be lowercase kebab-case.
- Frontmatter `description` must start with `Use when` and describe triggering conditions only.
- Every skill must keep these sections in order: `Overview`, `When To Use`, `Inputs Needed`, `Execution Order`, `Step-by-Step Process`, `Checks`, `Output Format`, `Common Mistakes`, `Example Prompts`.
- Use bilingual documentation: README files are split by language; skill bodies are Chinese-first with short English summaries and examples.
- Keep examples repo-neutral. Mention ai-shifu, ai-video-studio, elab, or TalkReplay only as pattern sources, not as required targets.
- Do not add project-specific secrets, URLs, credentials, or private environment assumptions.

## Validation

- Run `python3 scripts/validate_skill_quality.py` before committing.
- For substantial wording changes, test the skill with at least one realistic prompt and record the observed output manually in the commit or PR notes.

## Commit Discipline

- Use Conventional Commits.
- Keep commits atomic: one logical skill/content change per commit.
- Do not mix unrelated skill edits, validation script edits, and formatting churn unless the change is intentionally repository-wide.
