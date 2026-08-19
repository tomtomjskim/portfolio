# Backend Engineering Portfolio

## 30-second profile

- **Core:** PHP/MySQL 기반 운영형 백엔드·업무시스템
- **Domains:** 커머스·오픈마켓, 물류·배송, 제조 MES
- **Working method:** 변경 전 AS-IS 코드·DB 상태·권한·관리자·batch/cron·외부 API 영향 확인
- **Completion rule:** 코드 변경뿐 아니라 데이터 상태와 후속 업무 흐름까지 확인

## What I solve

```text
visible symptom or field request
→ actual workflow
→ state and data ownership
→ actor and permission
→ admin / batch / external boundary
→ bounded change
→ verification
```

운영 시스템의 문제는 화면 하나에서 끝나지 않는 경우가 많습니다. 그래서 기술을 먼저 고르기보다 **상태를 누가 만들고, 어떤 데이터와 후속 작업이 연결되며, 어디까지 함께 검증해야 하는지**를 먼저 정합니다.

## Primary cases

| Case | Problem | Decision | Evidence |
|---|---|---|---|
| [Commerce / Logistics Change Impact](cases/commerce-change-impact.md) | 화면 증상과 실제 처리 상태가 DB·관리자·batch·외부 API에 분산 | 상태 변경 주체와 downstream effect를 추적한 뒤 변경 범위 확정 | 비식별화한 커머스·물류 실무 Case |
| [Manufacturing MES Requirement Modeling](cases/mes-requirement-modeling.md) | 현장 요청이 입력·조회·상태·통계·권한·DB 규칙을 한 문장에 숨김 | 실제 작업 순서를 시스템 조건으로 분해 | 비식별화한 MES 개발·도입·지원 Case |

## Engineering decisions shown by the cases

### 1. 상태와 화면을 같은 것으로 보지 않음

사용자 화면, 관리자 처리, batch/cron, 외부 응답이 서로 다른 시점에 상태를 읽고 바꿀 수 있습니다. 화면 조건만 수정하지 않고 read path와 write path를 함께 확인합니다.

### 2. 요구 문장을 바로 구현 항목으로 바꾸지 않음

“버튼을 추가해 달라”, “조회가 이상하다”, “화면을 바꿔 달라”는 표현 뒤에 실제로는 상태 정의, 입력 순서, 조회 조건, 통계 기준, 권한 또는 데이터 관계가 숨어 있을 수 있습니다.

### 3. 전면 교체보다 변경 위험과 반복 비용을 비교

장기 운영 시스템에서는 rewrite가 hidden rule, 데이터 이관, 사용자 교육과 운영 중단 비용을 키울 수 있습니다. 반복 오류와 변경 비용이 실제로 큰 경계부터 분리하고, 기존 동작을 회귀 기준으로 유지합니다.

### 4. 완료를 코드 반영으로만 판단하지 않음

자동화 가능한 경로는 테스트하고, 관리자·사용자 동선과 운영 영향은 수동 시나리오로도 확인합니다. 모든 회사 업무 단계가 CI에서 자동 강제됐다는 의미는 아닙니다.

## Supporting case — AI-assisted engineering

[Practical AI Automation](cases/practical-ai-automation.md)은 LLM 사용량이 아니라 책임 분리를 보여줍니다.

```text
비정형 자연어
→ Local LLM draft

명확한 파일 변환 규칙
→ deterministic program

업무 맥락과 최종 반영
→ human validation
```

AI가 본업을 대체한 사례가 아니라, 반복 업무와 개발 검수의 일부를 안전한 경계 안에서 보조한 경험입니다.

## Public engineering signals

| Repository | What is public | Boundary |
|---|---|---|
| [stackforge-atlas](https://github.com/tomtomjskim/stackforge-atlas) | intent → interface → evidence → recovery 연결 | bounded pilot이며 전체 production HA/PITR 증거가 아님 |
| [harness-kit](https://github.com/tomtomjskim/harness-kit) | typed configuration, build pipeline, dependency audit, tests, CLI smoke | npm 배포·외부 채택·생산성 수치 없음 |
| [codex-workflow-skills](https://github.com/tomtomjskim/codex-workflow-skills) | independent review와 pass/skip/not_run/failure 구분 | test 결과를 모델 품질·조직 채택으로 확대하지 않음 |

전체 Evidence 상태: [EVIDENCE.md](EVIDENCE.md)

## Navigate

- AI-assisted / Internal Tools 관점: [PORTFOLIO-AX.md](PORTFOLIO-AX.md)
- 4개 Case 전체: [README.md](README.md#selected-case-studies)
- 공개 경계: [docs/PUBLIC-BOUNDARY.md](docs/PUBLIC-BOUNDARY.md)
