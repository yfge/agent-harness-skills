#!/usr/bin/env python3
"""Check harness profile and template consistency."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import sys
from typing import Any


PROFILE_PATH = Path("references") / "harness-profiles.json"
REQUIRED_ARCHETYPES = {
    "library",
    "service",
    "monorepo",
    "cli-tooling",
    "docs-only",
    "regulated-high-audit",
}


@dataclass(frozen=True)
class ProfileIssue:
    path: Path
    message: str


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json_object(path: Path) -> tuple[dict[str, Any] | None, list[ProfileIssue]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None, [ProfileIssue(path, "missing harness profile")]
    except json.JSONDecodeError as exc:
        return None, [ProfileIssue(path, f"invalid JSON: {exc}")]
    if not isinstance(payload, dict):
        return None, [ProfileIssue(path, "profile must contain a JSON object")]
    return payload, []


def _require_string(
    payload: dict[str, Any],
    key: str,
    path: Path,
    issues: list[ProfileIssue],
    *,
    prefix: str,
) -> str | None:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        issues.append(ProfileIssue(path, f"{prefix}.{key} must be a non-empty string"))
        return None
    return value


def _require_string_list(
    payload: dict[str, Any],
    key: str,
    path: Path,
    issues: list[ProfileIssue],
    *,
    prefix: str,
) -> list[str]:
    value = payload.get(key)
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        issues.append(ProfileIssue(path, f"{prefix}.{key} must be a list of strings"))
        return []
    return value


def _validate_template(
    root: Path,
    role_id: str,
    template_path: str,
    profile_path: Path,
    issues: list[ProfileIssue],
) -> None:
    if Path(template_path).is_absolute():
        issues.append(ProfileIssue(profile_path, f"template path must be relative: {template_path}"))
        return
    resolved = (root / template_path).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError:
        issues.append(ProfileIssue(profile_path, f"template path escapes repository: {template_path}"))
        return
    if not resolved.is_file():
        issues.append(ProfileIssue(profile_path, f"missing template: {template_path}"))
        return
    text = resolved.read_text(encoding="utf-8")
    role_marker = f"Harness role: {role_id}"
    if role_marker not in text:
        issues.append(ProfileIssue(resolved, f"template must include `{role_marker}`"))


def check_repository(root: Path) -> list[ProfileIssue]:
    root = root.resolve()
    profile_path = root / PROFILE_PATH
    profile, issues = load_json_object(profile_path)
    if profile is None:
        return issues

    roles = profile.get("roles")
    if not isinstance(roles, dict) or not roles:
        issues.append(ProfileIssue(profile_path, "roles must be a non-empty object"))
        return issues
    template_directory = profile.get("templateDirectory", "templates")
    if not isinstance(template_directory, str) or not template_directory.strip():
        issues.append(ProfileIssue(profile_path, "templateDirectory must be a non-empty string"))
    elif not (root / template_directory).is_dir():
        issues.append(ProfileIssue(profile_path, f"templateDirectory does not exist: {template_directory}"))
    role_ids = set(roles)
    for role_id, role in roles.items():
        if not isinstance(role, dict):
            issues.append(ProfileIssue(profile_path, f"roles.{role_id} must be an object"))
            continue
        _require_string(role, "description", profile_path, issues, prefix=f"roles.{role_id}")
        _require_string_list(role, "defaultArtifacts", profile_path, issues, prefix=f"roles.{role_id}")
        _require_string_list(role, "aliases", profile_path, issues, prefix=f"roles.{role_id}")

    archetypes = profile.get("archetypes")
    if not isinstance(archetypes, list) or not archetypes:
        issues.append(ProfileIssue(profile_path, "archetypes must be a non-empty array"))
        return issues

    seen_archetypes: set[str] = set()
    for index, archetype in enumerate(archetypes):
        prefix = f"archetypes[{index}]"
        if not isinstance(archetype, dict):
            issues.append(ProfileIssue(profile_path, f"{prefix} must be an object"))
            continue
        archetype_id = _require_string(archetype, "id", profile_path, issues, prefix=prefix)
        if archetype_id:
            seen_archetypes.add(archetype_id)
        _require_string(archetype, "displayName", profile_path, issues, prefix=prefix)
        role_fields = (
            _require_string_list(archetype, "minimumRoles", profile_path, issues, prefix=prefix)
            + _require_string_list(archetype, "optionalRoles", profile_path, issues, prefix=prefix)
            + _require_string_list(archetype, "avoidByDefault", profile_path, issues, prefix=prefix)
        )
        for role_id in role_fields:
            if role_id not in role_ids:
                issues.append(ProfileIssue(profile_path, f"{prefix} references unknown role: {role_id}"))
        minimum_roles = set(archetype.get("minimumRoles", []))
        avoid_by_default = set(archetype.get("avoidByDefault", []))
        overlap = sorted(minimum_roles & avoid_by_default)
        for role_id in overlap:
            issues.append(
                ProfileIssue(
                    profile_path,
                    f"{prefix} cannot require and avoid role by default: {role_id}",
                )
            )

        templates = archetype.get("defaultTemplates", {})
        if not isinstance(templates, dict):
            issues.append(ProfileIssue(profile_path, f"{prefix}.defaultTemplates must be an object"))
            continue
        for role_id, template_path in templates.items():
            if role_id not in role_ids:
                issues.append(ProfileIssue(profile_path, f"{prefix} template uses unknown role: {role_id}"))
                continue
            if not isinstance(template_path, str) or not template_path.strip():
                issues.append(ProfileIssue(profile_path, f"{prefix}.{role_id} template must be a string"))
                continue
            _validate_template(root, role_id, template_path, profile_path, issues)

    missing_archetypes = sorted(REQUIRED_ARCHETYPES - seen_archetypes)
    for archetype_id in missing_archetypes:
        issues.append(ProfileIssue(profile_path, f"missing required archetype: {archetype_id}"))

    engineering_forms = profile.get("engineeringForms", [])
    if not isinstance(engineering_forms, list) or not all(
        isinstance(item, str) and item.strip() for item in engineering_forms
    ):
        issues.append(ProfileIssue(profile_path, "engineeringForms must be a list of strings"))

    return issues


def main() -> int:
    issues = check_repository(repo_root())
    if issues:
        print("Harness profile consistency check FAILED:", file=sys.stderr)
        for issue in issues:
            print(f"  error: {issue.path}: {issue.message}", file=sys.stderr)
        return 1

    print("Harness profile consistency check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
