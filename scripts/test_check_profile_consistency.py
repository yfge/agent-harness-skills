#!/usr/bin/env python3
"""Tests for harness profile and template consistency checks."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT_DIR = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "check_profile_consistency", SCRIPT_DIR / "check_profile_consistency.py"
)
assert SPEC is not None
assert SPEC.loader is not None
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def valid_profile() -> dict:
    roles = {
        "entrypoint": {
            "description": "First-read repository guidance.",
            "defaultArtifacts": ["AGENTS.md"],
            "aliases": ["CLAUDE.md"],
        },
        "work-state": {
            "description": "Current tasks and acceptance criteria.",
            "defaultArtifacts": ["tasks.md"],
            "aliases": ["GitHub Issues"],
        },
        "ledger": {
            "description": "Delivery evidence records.",
            "defaultArtifacts": ["agent_chats/"],
            "aliases": ["PR descriptions"],
        },
        "validation": {
            "description": "Commands proving changes are safe.",
            "defaultArtifacts": ["docs/validation.md"],
            "aliases": ["Makefile targets"],
        },
        "runtime-evidence": {
            "description": "Artifacts tying observed behavior to traces.",
            "defaultArtifacts": ["artifacts/runs/<run_id>/"],
            "aliases": ["trace exports"],
        },
        "quality": {
            "description": "Metrics and baselines for quality movement.",
            "defaultArtifacts": ["QUALITY_SCORE.md"],
            "aliases": ["generated quality report"],
        },
    }
    archetypes = [
        {
            "id": "library",
            "displayName": "Library",
            "minimumRoles": ["entrypoint", "validation"],
            "optionalRoles": ["work-state", "ledger", "quality"],
            "defaultTemplates": {"entrypoint": "templates/AGENTS.md"},
            "avoidByDefault": ["runtime-evidence"],
        },
        {
            "id": "service",
            "displayName": "Service",
            "minimumRoles": ["entrypoint", "validation", "runtime-evidence"],
            "optionalRoles": ["work-state", "ledger", "quality"],
            "defaultTemplates": {"runtime-evidence": "templates/runtime-evidence-summary.md"},
            "avoidByDefault": [],
        },
        {
            "id": "monorepo",
            "displayName": "Monorepo",
            "minimumRoles": ["entrypoint", "validation", "work-state"],
            "optionalRoles": ["ledger", "runtime-evidence", "quality"],
            "defaultTemplates": {"validation": "templates/validation-matrix.md"},
            "avoidByDefault": [],
        },
        {
            "id": "cli-tooling",
            "displayName": "CLI Tooling",
            "minimumRoles": ["entrypoint", "validation"],
            "optionalRoles": ["work-state", "ledger", "quality"],
            "defaultTemplates": {"validation": "templates/validation-matrix.md"},
            "avoidByDefault": ["runtime-evidence"],
        },
        {
            "id": "docs-only",
            "displayName": "Docs Only",
            "minimumRoles": ["entrypoint", "validation"],
            "optionalRoles": ["work-state", "ledger"],
            "defaultTemplates": {"entrypoint": "templates/AGENTS.md"},
            "avoidByDefault": ["runtime-evidence", "quality"],
        },
        {
            "id": "regulated-high-audit",
            "displayName": "Regulated High Audit",
            "minimumRoles": ["entrypoint", "work-state", "ledger", "validation"],
            "optionalRoles": ["runtime-evidence", "quality"],
            "defaultTemplates": {"ledger": "templates/delivery-record.md"},
            "avoidByDefault": [],
        },
    ]
    return {
        "version": 1,
        "templateDirectory": "templates",
        "roles": roles,
        "archetypes": archetypes,
        "engineeringForms": ["library", "service", "monorepo", "backend", "frontend"],
    }


class CheckProfileConsistencyTest(unittest.TestCase):
    def test_valid_profile_and_templates_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_json(root / "references" / "harness-profiles.json", valid_profile())
            for template, role_id in (
                ("AGENTS.md", "entrypoint"),
                ("runtime-evidence-summary.md", "runtime-evidence"),
                ("validation-matrix.md", "validation"),
                ("delivery-record.md", "ledger"),
            ):
                write_text(
                    root / "templates" / template,
                    f"# Template\n\nHarness role: {role_id}\n",
                )

            issues = checker.check_repository(root)

            self.assertEqual([], issues)

    def test_unknown_role_in_archetype_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            profile = valid_profile()
            profile["archetypes"][0]["minimumRoles"].append("unknown-role")
            write_json(root / "references" / "harness-profiles.json", profile)
            write_text(root / "templates" / "AGENTS.md", "Harness role: entrypoint\n")

            issues = checker.check_repository(root)

            self.assertTrue(any("unknown role" in issue.message for issue in issues), issues)

    def test_missing_template_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_json(root / "references" / "harness-profiles.json", valid_profile())

            issues = checker.check_repository(root)

            self.assertTrue(any("missing template" in issue.message for issue in issues), issues)

    def test_avoid_by_default_role_cannot_be_required(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            profile = valid_profile()
            profile["archetypes"][0]["minimumRoles"].append("runtime-evidence")
            write_json(root / "references" / "harness-profiles.json", profile)
            write_text(root / "templates" / "AGENTS.md", "Harness role: entrypoint\n")

            issues = checker.check_repository(root)

            self.assertTrue(
                any("cannot require and avoid role by default" in issue.message for issue in issues),
                issues,
            )


if __name__ == "__main__":
    unittest.main()
