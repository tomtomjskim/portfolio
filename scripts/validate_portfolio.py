#!/usr/bin/env python3
"""공개 포트폴리오의 문서 구조, 링크, 공개 범위를 검사한다."""

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
    "## 핵심 질문",
    "## 한눈에 보기",
    "## 문제",
    "## 업무 환경과 제약",
    "## 확인 과정",
    "## 판단",
    "## 선택 기준과 대안",
    "## 구현",
    "## 검증과 실제 사용",
    "## 한계",
    "## 근거",
]

FORBIDDEN_CASE_SECTIONS = {
    "## 면접 예상 질문",
    "## 인터뷰 예상 질문",
    "## Interview Hooks",
    "## 면접 대응",
    "## 리허설",
}

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
    if not errors:
        return
    print("포트폴리오 검증 실패:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)


def load_manifest(errors: list[str]) -> dict[str, Any]:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append("portfolio-manifest.json 파일이 없음")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(f"portfolio-manifest.json JSON 오류: {exc}")
        return {}

    if not isinstance(data, dict):
        errors.append("portfolio-manifest.json 최상위 값은 객체여야 함")
        return {}
    return data


def validate_required_files(errors: list[str]) -> None:
    for rel in sorted(REQUIRED_FILES):
        if not (ROOT / rel).is_file():
            errors.append(f"필수 파일 없음: {rel}")


def validate_manifest(data: dict[str, Any], errors: list[str]) -> None:
    if data.get("schema_version") != "1.0":
        errors.append("schema_version은 1.0이어야 함")
    if data.get("content_role") != "canonical-public-portfolio-source":
        errors.append("content_role 값이 올바르지 않음")
    if data.get("source_repository") != "tomtomjskim/portfolio":
        errors.append("source_repository 값이 올바르지 않음")

    policy = data.get("projection_policy")
    if not isinstance(policy, dict):
        errors.append("projection_policy는 객체여야 함")
    else:
        if policy.get("source_branch") != "main":
            errors.append("projection_policy.source_branch는 main이어야 함")
        if policy.get("allows_duplicate_full_case_prose") is not False:
            errors.append("전체 사례 문장 중복 관리는 허용하지 않음")

    view_case_refs: list[tuple[str, str, str]] = []
    views = data.get("views")
    if not isinstance(views, list) or not views:
        errors.append("views는 비어 있지 않은 목록이어야 함")
    else:
        view_ids: set[str] = set()
        for index, view in enumerate(views):
            prefix = f"views[{index}]"
            if not isinstance(view, dict):
                errors.append(f"{prefix}는 객체여야 함")
                continue

            view_id = view.get("id")
            if not isinstance(view_id, str) or not view_id:
                errors.append(f"{prefix}.id가 필요함")
                view_id = prefix
            elif view_id in view_ids:
                errors.append(f"중복 view id: {view_id}")
            else:
                view_ids.add(view_id)

            file_name = view.get("file")
            if not isinstance(file_name, str) or not (ROOT / file_name).is_file():
                errors.append(f"view 파일 없음: {file_name!r}")

            for field in ("primary_cases", "supporting_cases"):
                values = view.get(field)
                if not isinstance(values, list):
                    errors.append(f"{prefix}.{field}는 목록이어야 함")
                    continue
                for value in values:
                    if not isinstance(value, str) or not value:
                        errors.append(f"{prefix}.{field}에 잘못된 case id가 있음")
                    else:
                        view_case_refs.append((str(view_id), field, value))

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("cases는 비어 있지 않은 목록이어야 함")
        return

    ids: set[str] = set()
    slugs: set[str] = set()
    orders: set[int] = set()
    evidence_text = (ROOT / "EVIDENCE.md").read_text(encoding="utf-8")

    for index, case in enumerate(cases):
        prefix = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix}는 객체여야 함")
            continue

        case_id = case.get("id")
        slug = case.get("slug")
        order = case.get("order")
        case_file = case.get("file")
        classification = case.get("classification")
        card = case.get("card")
        evidence_refs = case.get("evidence_refs")

        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{prefix}.id가 필요함")
        elif case_id in ids:
            errors.append(f"중복 case id: {case_id}")
        else:
            ids.add(case_id)

        if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            errors.append(f"{prefix}.slug는 kebab-case여야 함")
        elif slug in slugs:
            errors.append(f"중복 case slug: {slug}")
        else:
            slugs.add(slug)

        if not isinstance(order, int) or order < 1:
            errors.append(f"{prefix}.order는 양의 정수여야 함")
        elif order in orders:
            errors.append(f"중복 case order: {order}")
        else:
            orders.add(order)

        if classification not in ALLOWED_CLASSIFICATIONS:
            errors.append(f"{prefix}.classification 값이 올바르지 않음: {classification!r}")

        if not isinstance(case_file, str):
            errors.append(f"{prefix}.file이 필요함")
            continue

        path = ROOT / case_file
        if not path.is_file():
            errors.append(f"case 파일 없음: {case_file}")
            continue
        if path.parent != ROOT / "cases":
            errors.append(f"case 파일은 cases/ 아래에 있어야 함: {case_file}")

        text = path.read_text(encoding="utf-8")
        for forbidden in sorted(FORBIDDEN_CASE_SECTIONS):
            if forbidden in text:
                errors.append(f"{case_file}: 공개 사례에 내부 면접 자료가 포함됨: {forbidden}")

        last_position = -1
        for heading in REQUIRED_CASE_HEADINGS:
            position = text.find(heading)
            if position == -1:
                errors.append(f"{case_file}: 필수 제목 없음: {heading}")
            elif position <= last_position:
                errors.append(f"{case_file}: 제목 순서 오류: {heading}")
            else:
                last_position = position

        question = case.get("question")
        if not isinstance(question, str) or question not in text:
            errors.append(f"{case_file}: manifest 질문이 문서와 일치하지 않음")

        if not isinstance(card, dict):
            errors.append(f"{prefix}.card는 객체여야 함")
        else:
            for field in ("problem", "decision", "evidence"):
                value = card.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{prefix}.card.{field}가 필요함")
                elif value not in text:
                    errors.append(f"{case_file}: card.{field}가 문서와 일치하지 않음")

        if not isinstance(evidence_refs, list) or not evidence_refs:
            errors.append(f"{prefix}.evidence_refs는 비어 있지 않은 목록이어야 함")
        else:
            for evidence_id in evidence_refs:
                if not isinstance(evidence_id, str) or evidence_id not in evidence_text:
                    errors.append(f"{case_file}: EVIDENCE.md에 없는 근거 ID: {evidence_id!r}")

    if orders and orders != set(range(1, len(cases) + 1)):
        errors.append("case order는 1부터 연속이어야 함")

    for view_id, field, case_id in view_case_refs:
        if case_id not in ids:
            errors.append(f"view {view_id}.{field}가 존재하지 않는 case를 참조함: {case_id}")


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
                errors.append(f"{rel}: 저장소 밖으로 나가는 링크: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{rel}: 깨진 상대 링크: {target}")


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
                errors.append(f"{rel}: 공개 금지 문자열 발견: {literal}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{rel}: credential 의심 패턴 발견: {pattern.pattern}")


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
    print(f"확인 완료: 포트폴리오 문서 구조와 공개 범위 통과 ({len(cases)}개 사례)")


if __name__ == "__main__":
    main()
