# Scenario Tests

Record realistic prompt tests for substantial skill wording changes. Keep entries repo-neutral, concise, and free of private URLs, credentials, secrets, or environment assumptions.

## 2026-05-28 - Planning Review Routing

- Prompt: "检查这个项目的 skills 的规划是否合理"
- Skills under review: all 9 repository skills plus `INDEX.md` routing.
- Observed output: The review kept the current 9-skill model, found incomplete index routing, missing validator section-order enforcement, and no durable scenario-test record.
- Follow-up: Add full routing notes, validator unit tests, section-order validation, CI test execution, and this scenario-test log.

## 2026-05-28 - English Skill Body Conversion

- Prompt: "commit, then make every SKILL.md English and add needed references and scripts"
- Skills under review: all 9 repository skills plus supporting repository checks.
- Observed output: The change should preserve the 9-skill model, convert skill bodies to English-only text, add a shared harness reference, and add a standard-library language check for `SKILL.md` files.
- Follow-up: Run unit tests, structure validation, language validation, and diff whitespace checks before committing.

## 2026-05-28 - Missing Harness Files Closure

- Prompt: "missing harness files should be constructed, not only searched"
- Skills under review: all 9 repository skills plus per-skill references.
- Observed output: The workflow should discover existing harness files, classify absence, build the minimum viable artifact from a skill-local reference, and validate the result.
- Follow-up: Add `references/build-when-missing.md` for every skill and a closure checker that prevents skills from regressing to search-only guidance.
