# 김정식 | Backend Engineering Portfolio

PHP/MySQL 기반 커머스·물류·MES 업무시스템을 개발·운영해 온 백엔드 개발자입니다.

기능을 변경할 때 화면이나 단일 함수부터 고치기보다 **AS-IS 코드, DB 상태, 권한, 관리자 흐름, batch/cron, 외부 API가 실제로 연결되는 범위**를 먼저 확인합니다. LLM과 Agent는 분석·구현·검토를 보조하지만, 완료 여부는 코드·테스트·실행 결과와 사람의 판단으로 확인합니다.

## Start here

- **General Backend:** [PORTFOLIO.md](PORTFOLIO.md)
- **AI-assisted / Internal Tools:** [PORTFOLIO-AX.md](PORTFOLIO-AX.md)
- **Evidence status:** [EVIDENCE.md](EVIDENCE.md)

## Selected case studies

| Case | Problem | Decision | Evidence |
|---|---|---|---|
| [Commerce / Logistics Change Impact](cases/commerce-change-impact.md) | 화면 증상이 DB 상태·관리자·배치·외부 연동까지 이어짐 | UI 수정 전에 상태 변경 주체와 후속 영향을 추적 | 비식별화한 실무 Case와 프로젝트 검수 범위 |
| [Manufacturing MES Requirement Modeling](cases/mes-requirement-modeling.md) | “화면 변경” 요청이 상태·조회·통계·권한 규칙을 숨김 | 실제 작업 순서를 시스템 조건으로 분해 | 비식별화한 실무 Case와 현장 도입·지원 범위 |
| [Practical AI Automation](cases/practical-ai-automation.md) | 번역·복사·언어팩 반영이 반복되고 소형 모델에 한계가 있음 | 자연어는 Local LLM, 파일 변환은 일반 코드, 최종 판단은 사람 | 실제 반복 사용한 언어팩 Workflow와 공개 검증 원칙 |
| [Developer Internal Tooling](cases/developer-internal-tooling.md) | 여러 프로젝트의 AI coding 설정을 복제하면 중복과 drift가 발생 | 반복 비용이 생기는 경계만 typed module과 deterministic build로 공통화 | `harness-kit` 공개 코드와 Node 22/24 검증 Workflow |

## How to read this repository

```text
Career case
= 실제 경력에서 확인된 문제·판단·업무 범위를 공개 가능한 수준으로 비식별화

Public engineering artifact
= 현재 공개 코드와 CI로 확인할 수 있는 설계·구현·검증 방식
```

두 종류의 근거를 서로 바꿔 말하지 않습니다. Case 원문은 `cases/`, 공개 근거의 상태와 한계는 [EVIDENCE.md](EVIDENCE.md)에서 확인할 수 있습니다.

## Selected public engineering

- [stackforge-atlas](https://github.com/tomtomjskim/stackforge-atlas) — intent, interface, evidence, recovery를 연결하는 engineering atlas
- [harness-kit](https://github.com/tomtomjskim/harness-kit) — AI coding configuration을 모듈과 deterministic build로 관리하는 internal tool
- [codex-workflow-skills](https://github.com/tomtomjskim/codex-workflow-skills) — intake, independent review, failure accounting, validation을 분리한 Workflow Skills
- [claude-code-guide](https://github.com/tomtomjskim/claude-code-guide) — Skill·Hook·Agent·Handoff·Failure Recovery 운영 가이드와 템플릿

## Source and projection

이 저장소가 공개 Case의 원문입니다. 향후 `tomtomjskim.github.io`는 이 저장소의 **정확한 commit SHA**를 읽어 정적 화면으로 투영하며, 별도의 경력 사실이나 Case 문장을 소유하지 않습니다.

- Machine-readable source: [portfolio-manifest.json](portfolio-manifest.json)
- Case authoring contract: [docs/CASE-CONTRACT.md](docs/CASE-CONTRACT.md)
- Projection contract: [docs/PROJECTION-CONTRACT.md](docs/PROJECTION-CONTRACT.md)
- Public boundary: [docs/PUBLIC-BOUNDARY.md](docs/PUBLIC-BOUNDARY.md)

GitHub profile: <https://github.com/tomtomjskim>
