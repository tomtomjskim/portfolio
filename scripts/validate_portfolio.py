#!/usr/bin/env python3
"""Validate the public portfolio source contract with the Python standard library."""

from __future__ import annotations

import json
import pathlib
import re
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "portfolio-manifest.json"

REQUIRED_FILES = {
    "README.md",
    "PORTFOLIO.md",
    "PORTFOLIO-AX.md",
    "EVIDENCE.md",
    "portfolio-manifest.json",
    "docs/CASE-CONTRACT.md",
    "docs/PROJECTION-CONTRACT.md",
    "docs/PUBLIC-BOUNDARY.md",
}

REQUIRED_CASE_HEADINGS = [
    "## Question",
    "## At a glance",
    "## Problem",
    "## Context / constraints",
    "## Investigation",
    "## Decision",
    "## Trade-off",
    "## Implementation",
    "## Verification / actual use",
    "## Limitations",
    "## Evidence",
    "## Interview hooks",
]

ALLOWED_CLASSIFICATIONS = {
    "sanitized-actual-work",
    "sanitized-actual-work-with-public-rnd-support",
    "public-rnd",
}

FORBIDDEN_LITERALS = {
    "jsnetworkcorp-portfolio",
    "dna_project",
    "/Users/",
    "/home/",
    "/mnt/data",
    "sandbox:",
}

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)(?:api[_-]?key|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{20,}"),
]

MARKDOWN_LINK_RE = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")


def fail(errors: list[str]) -> None:
    if errors:
        print("Portfolio validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def load_manifest(errors: list[str]) -> dict[str, Any]:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append("portfolio-manifest.json is missing")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"portfolio-manifest.json is invalid JSON: {exc}")
        return {}

    if not isinstance(data, dict):
        errors.append("portfolio-manifest.json must be an object")
        return {}
    return data


def validate_required_files(errors: list[str]) -> None:
    for rel in sorted(REQUIRED_FILES):
        if not (ROOT / rel).is_file():
            errors.append(f"required file missing: {rel}")


def validate_manifest(data: dict[str, Any], errors: list[str]) -> None:
    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if data.get("content_role") != "canonical-public-portfolio-source":
        errors.append("content_role must be canonical-public-portfolio-source")
    if data.get("source_repository") != "tomtomjskim/portfolio":
        errors.append("source_repository must be tomtomjskim/portfolio")

    projection = data.get("projection_policy")
    if not isinstance(projection, dict):
        errors.append("projection_policy must be an object")
    else:
        if projection.get("requires_exact_source_commit") is not True:
            errors.append("projection_policy.requires_exact_source_commit must be true")
        if projection.get("allows_floating_main") is not False:
            errors.append("projection_policy.allows_floating_main must be false")
        if projection.get("allows_duplicate_full_case_prose") is not False:
            errors.append("projection_policy.allows_duplicate_full_case_prose must be false")

    views = data.get("views")
    view_case_refs: list[tuple[str, str, str]] = []
    if not isinstance(views, list) or not views:
        errors.append("views must be a non-empty list")
    else:
        view_ids: set[str] = set()
        for index, view in enumerate(views):
            prefix = f"views[{index}]"
            if not isinstance(view, dict):
                errors.append(f"{prefix} must be an object")
                continue

            view_id = view.get("id")
            if not isinstance(view_id, str) or not view_id:
                errors.append(f"{prefix}.id is required")
                view_id = prefix
            elif view_id in view_ids:
                errors.append(f"duplicate view id: {view_id}")
            else:
                view_ids.add(view_id)

            file_name = view.get("file")
            if not isinstance(file_name, str) or not (ROOT / file_name).is_file():
                errors.append(f"view file missing: {file_name!r}")

            for field in ("primary_cases", "supporting_cases"):
                values = view.get(field)
                if not isinstance(values, list):
                    errors.append(f"{prefix}.{field} must be a list")
                    continue
                for value in values:
                    if not isinstance(value, str) or not value:
                        errors.append(f"{prefix}.{field} contains an invalid case id")
                    else:
                        view_case_refs.append((str(view_id), field, value))

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("cases must be a non-empty list")
        return

    ids: set[str] = set()
    slugs: set[str] = set()
    orders: set[int] = set()
    evidence_text = (ROOT / "EVIDENCE.md").read_text(encoding="utf-8")

    for index, case in enumerate(cases):
        prefix = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be an object")
            continue

        case_id = case.get("id")
        slug = case.get("slug")
        order = case.get("order")
        case_file = case.get("file")
        classification = case.get("classification")
        card = case.get("card")
        evidence_refs = case.get("evidence_refs")

        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{prefix}.id is required")
        elif case_id in ids:
            errors.append(f"duplicate case id: {case_id}")
        else:
            ids.add(case_id)

        if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            errors.append(f"{prefix}.slug must be kebab-case")
        elif slug in slugs:
            errors.append(f"duplicate case slug: {slug}")
        else:
            slugs.add(slug)

        if not isinstance(order, int) or order < 1:
            errors.append(f"{prefix}.order must be a positive integer")
        elif order in orders:
            errors.append(f"duplicate case order: {order}")
        else:
            orders.add(order)

        if classification not in ALLOWED_CLASSIFICATIONS:
            errors.append(f"{prefix}.classification is invalid: {classification!r}")

        if not isinstance(case_file, str):
            errors.append(f"{prefix}.file is required")
            continue

        path = ROOT / case_file
        if not path.is_file():
            errors.append(f"case file missing: {case_file}")
            continue
        if path.parent != ROOT / "cases":
            errors.append(f"case file must be under cases/: {case_file}")

        text = path.read_text(encoding="utf-8")
        last_position = -1
        for heading in REQUIRED_CASE_HEADINGS:
            position = text.find(heading)
            if position == -1:
                errors.append(f"{case_file}: required heading missing: {heading}")
            elif position <= last_position:
                errors.append(f"{case_file}: heading order invalid at {heading}")
            else:
                last_position = position

        question = case.get("question")
        if not isinstance(question, str) or question not in text:
            errors.append(f"{case_file}: manifest question is not mirrored in the case file")

        if not isinstance(card, dict):
            errors.append(f"{prefix}.card must be an object")
        else:
            for field in ("problem", "decision", "evidence"):
                value = card.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{prefix}.card.{field} is required")
                elif value not in text:
                    errors.append(f"{case_file}: card.{field} does not match manifest")

        if not isinstance(evidence_refs, list) or not evidence_refs:
            errors.append(f"{prefix}.evidence_refs must be a non-empty list")
        else:
            for evidence_id in evidence_refs:
                if not isinstance(evidence_id, str) or evidence_id not in evidence_text:
                    errors.append(f"{case_file}: evidence ref not found in EVIDENCE.md: {evidence_id!r}")

    if orders and orders != set(range(1, len(cases) + 1)):
        errors.append("case orders must be contiguous from 1")

    for view_id, field, case_id in view_case_refs:
        if case_id not in ids:
            errors.append(f"view {view_id}.{field} references unknown case id: {case_id}")


def normalize_link_target(raw: str) -> str:
    target = raw.strip().strip("'\"")
    if " " in target:
        target = target.split(" ", 1)[0]
    return target.split("#", 1)[0]


def validate_markdown_links(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = normalize_link_target(match.group(1))
            if not target or target.startswith(("#", "mailto:")) or "://" in target:
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"{rel}: link escapes repository: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{rel}: broken relative link: {target}")


def validate_public_boundary(errors: list[str]) -> None:
    files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".py", ".yml", ".yaml"}
    ]
    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if rel == pathlib.Path("scripts/validate_portfolio.py"):
            continue
        for literal in FORBIDDEN_LITERALS:
            if literal in text:
                errors.append(f"{rel}: forbidden public literal found: {literal}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{rel}: possible secret pattern found: {pattern.pattern}")


def main() -> None:
    errors: list[str] = []
    validate_required_files(errors)
    data = load_manifest(errors)
    if data:
        validate_manifest(data, errors)
    validate_markdown_links(errors)
    validate_public_boundary(errors)
    fail(errors)

    cases = data.get("cases", []) if isinstance(data, dict) else []
    print(f"ok: portfolio source contract passed ({len(cases)} cases)")


if __name__ == "__main__":
    main()
