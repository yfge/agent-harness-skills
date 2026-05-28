## Summary

<!-- What changed, and why? -->

## Type Of Change

- [ ] Skill wording or workflow
- [ ] Validation script or tests
- [ ] Installation or packaging
- [ ] Documentation only
- [ ] Other

## Repository Neutrality

- [ ] Examples are repo-neutral.
- [ ] No private URLs, credentials, account names, or environment assumptions were added.
- [ ] Product-specific details were generalized into reusable patterns.

## Validation

Run the relevant commands and paste results:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/validate_skill_quality.py
python3 scripts/check_skill_language.py
python3 scripts/check_skill_closure.py
python3 scripts/check_reference_neutrality.py
```

For plugin or extension metadata changes:

```bash
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
python3 -m json.tool .cursor-plugin/plugin.json >/dev/null
python3 -m json.tool gemini-extension.json >/dev/null
python3 -m json.tool package.json >/dev/null
node --check .opencode/plugins/agent-harness-skills.js
```

## Scenario Test

<!-- For substantial skill wording or workflow changes, include at least one realistic prompt and observed output. Use docs/scenario-tests.md when the result should be durable. -->

## Notes For Reviewers

<!-- Anything reviewers should pay special attention to? -->
