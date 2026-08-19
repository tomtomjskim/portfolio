# Public Evidence Index

이 문서는 공개 Portfolio가 연결하는 근거의 **종류, 확인 가능한 범위, 해석 상한**을 관리합니다.

```text
Sanitized actual-work case
= 실제 경력의 문제·판단·사용 범위를 공개 가능한 수준으로 설명

Public engineering artifact
= 공개 코드·문서·CI로 현재 확인 가능한 구현과 검증 방식
```

공개 R&D를 이전 회사의 production source로 표현하지 않습니다.

## Actual-work cases

<a id="ev-career-commerce"></a>
### EV-CAREER-COMMERCE — Commerce / Logistics

- **Type:** sanitized actual-work case
- **Shows:** PHP/MySQL 커머스·물류 운영 시스템의 상태·권한·관리자·batch/cron·외부 API 변경 영향 분석
- **Public verification:** [Commerce / Logistics Change Impact](cases/commerce-change-impact.md)
- **Protected evidence boundary:** 경력 원천과 내부 프로젝트 자료는 비공개
- **Does not prove:** 전체 commerce architecture ownership, production SLA·트래픽·매출 수치, 모든 transaction/idempotency/reconciliation 구현

<a id="ev-career-mes"></a>
### EV-CAREER-MES — Manufacturing MES

- **Type:** sanitized actual-work case
- **Shows:** 현장 요구를 입력·조회·상태·통계·권한·DB 조건으로 분해하고 도입·지원에서 문제 계층을 구분한 경험
- **Public verification:** [Manufacturing MES Requirement Modeling](cases/mes-requirement-modeling.md)
- **Protected evidence boundary:** 고객사·공장·생산 데이터와 내부 제품 구조는 비공개
- **Does not prove:** 전체 MES 제품 ownership, 모든 고객사 단독 구축, cloud-native SaaS·SLA 성과

<a id="ev-local-i18n"></a>
### EV-LOCAL-I18N — Local LLM i18n Workflow

- **Type:** sanitized actual-use case
- **Shows:** Python + Ollama/Gemma 3 번역 초안, 별도 PHP 언어팩 생성·JSON 변환, 사람 검수의 책임 분리
- **Actual use:** 프론트 개발자가 반복 언어팩 작업에 사용
- **Public verification:** [Practical AI Automation](cases/practical-ai-automation.md)
- **Protected evidence boundary:** 번역 서버 source와 내부 경로는 비공개
- **Does not prove:** 번역 정확도·생산성·비용 절감률, GPU/model-serving 운영, 완전 자동 번역

## Public engineering artifacts

<a id="ev-harness-kit"></a>
### EV-HARNESS-KIT — harness-kit

- **Type:** public R&D / internal-tooling artifact
- **Shows:** instruction·hook·MCP·permission·agent·workflow·skill 설정의 모듈화와 deterministic generation
- **Implementation evidence:** resolver, loader, validator, merger, renderer, writer pipeline
- **Verification:** Node 22/24, dependency audit at `high`, TypeScript check, tests, build, CLI smoke
- **Repository:** <https://github.com/tomtomjskim/harness-kit>
- **Does not prove:** npm publication, external adoption, organization-wide use, productivity improvement

<a id="ev-codex-workflow"></a>
### EV-CODEX-WORKFLOW — codex-workflow-skills

- **Type:** public R&D / Workflow Skills
- **Shows:** intake, implementation, independent review, failure accounting, validation, closeout
- **Verification boundary:** public forward-test separates pass from external `skip` / `not_run`
- **Repository:** <https://github.com/tomtomjskim/codex-workflow-skills>
- **Does not prove:** live model quality, release, external adoption, organization productivity

<a id="ev-stackforge"></a>
### EV-STACKFORGE — stackforge-atlas

- **Type:** public R&D / engineering atlas
- **Shows:** product intent → interface → implementation → evidence → failure/recovery 연결
- **Verification boundary:** public code, CI, bounded PostgreSQL durability/recovery exercise
- **Repository:** <https://github.com/tomtomjskim/stackforge-atlas>
- **Does not prove:** full production PITR, high availability, replication, failover ownership

<a id="ev-claude-guide"></a>
### EV-CLAUDE-GUIDE — claude-code-guide

- **Type:** selective supporting guide
- **Shows:** Skill·Hook·Agent·Handoff·Failure Recovery와 project rule 운영의 공개 가이드·템플릿
- **Repository:** <https://github.com/tomtomjskim/claude-code-guide>
- **Does not prove:** 저장소 전체 기능의 회사 프로젝트 적용, 조직 도입, 성과 수치

## Evidence rules

- PR·CI·test pass는 release·deployment·external adoption이 아닙니다.
- 공개 R&D는 employer production source가 아닙니다.
- 실제 업무 Case와 현재 공개 engineering artifact를 분리합니다.
- 측정하지 않은 생산성·시간·비용·정확도 수치를 사용하지 않습니다.
- private repository·내부 경로·고객 데이터·endpoint·credential·raw log를 공개하지 않습니다.
- 공개 근거가 바뀌면 Case보다 먼저 이 문서와 [portfolio-manifest.json](portfolio-manifest.json)의 참조를 갱신합니다.
