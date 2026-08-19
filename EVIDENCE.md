# Public Evidence Index

이 문서는 공개 포트폴리오에서 사용할 수 있는 대표 evidence의 상태를 관리합니다. 과거 원장보다 **현재 사용자 정정과 최신 public claim boundary**를 우선합니다.

## Primary

### harness-kit

- Status: **primary**
- Shows: developer internal tooling, typed configuration, deterministic generation, validation/CI
- Boundary: production adoption, npm publication, productivity metric 미주장
- Repository: <https://github.com/tomtomjskim/harness-kit>

### codex-workflow-skills

- Status: **primary**
- Shows: intake, independent review, failure receipt/accounting, validation, closeout
- Public test evidence: forward-test에서 pass와 external skip/not_run을 분리
- Boundary: test count가 model quality·생산성·조직 채택을 증명하지 않음
- Repository: <https://github.com/tomtomjskim/codex-workflow-skills>

### stackforge-atlas

- Status: **primary**
- Shows: intent → interface → evidence → recovery, DB durability/recovery exercise
- Boundary: full production PITR/HA/replication/failover proof 아님
- Repository: <https://github.com/tomtomjskim/stackforge-atlas>

### Local LLM i18n workflow

- Status: **primary sanitized work case**
- Shows: 실제 반복 언어팩 업무에 Local LLM 적용, deterministic conversion과 human validation 책임 분리
- Boundary: private translation-server source/address 미공개, productivity/accuracy/cost metric 미주장
- Case: [cases/practical-ai-automation.md](cases/practical-ai-automation.md)

## Selective / Supporting

### claude-code-guide

- Status: **selective supporting**
- Use: Skill/Hook/Handoff/Failure Recovery의 학습·일반화 사례
- Metric caveat: 단일 A/B 실험 값을 일반적인 생산성 향상으로 확대하지 않음
- Repository: <https://github.com/tomtomjskim/claude-code-guide>

## Hold

### aiwright

- Status: **hold as representative portfolio case**
- Verified: PR #1 merged; 795/795 tests, typecheck, ESM/CJS/CLI distribution check, production dependency audit
- Hold reason: package release·외부 채택·실제 사용자 성과 미검증이며, 현재 대표 이직 사례로는 목적·실사용 설명력이 Primary 세트보다 약함
- Repository: <https://github.com/tomtomjskim/aiwright>

### db-mcp

- Status: **supporting-hold**
- Verified draft: 74/74 tests, build, lint exit 0, production audit
- Hold reason: PR #3 미병합, lint warning debt와 large formatting diff 존재
- Repository: <https://github.com/tomtomjskim/db-mcp>

## Excluded

- `dna_project`: career evidence에서 영구 제외
- `image-translator`: 현재 이력서·AX 포트폴리오 대표 근거에서 제외
- prototype / upstream-curation 자산은 별도 검증 전 대표 사례로 승격하지 않음

## Evidence rules

- PR/CI/test pass != release/deployment/adoption
- 공개 R&D != employer production source
- 측정하지 않은 생산성·시간·비용·정확도 수치 금지
- private repo/path/customer data/endpoint/credential/raw log 공개 금지
