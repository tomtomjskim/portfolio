# Backend Engineering Portfolio

## 30-second profile

- **Core:** PHP / MySQL 기반 운영형 백엔드·업무시스템
- **Domains:** 커머스·오픈마켓, 물류·배송, 제조 MES
- **Working method:** 기능 변경 전 AS-IS 코드·DB 상태·권한·관리자·batch/cron·외부 API 영향 확인
- **Verification:** 코드·DB·테스트·운영 흐름을 근거로 변경 범위와 완료 여부 판단

```text
Career case
= 실제 경력에서 확인된 도메인·문제 해결 방식

Public engineering repository
= 현재 공개적으로 확인 가능한 설계·구현·검증 방식
```

두 종류의 evidence를 서로 바꿔 말하지 않습니다.

---

## Case 01 — Commerce / Logistics

### 문제

운영형 커머스·물류 시스템에서는 화면 하나의 증상이 DB 상태, 관리자 처리, batch/cron, 외부 API와 연결될 수 있습니다.

### 판단

증상이 보이는 UI부터 수정하지 않고 이번 변경에 연결된 경계를 먼저 확인합니다.

```text
change request
→ AS-IS code
→ DB structure / state
→ permission
→ admin workflow
→ batch / cron
→ external API
→ bounded modification scope
```

### 확인 가능한 범위

- PHP 기반 커머스·물류 운영 시스템의 기능 개선 경험
- 상품·입고·재고·외부출고·관리자 흐름 등 상태 중심 기능
- file-based 외부 주문 등록에서 upload → preview → confirm과 batch 처리 경계

[Deep dive →](cases/commerce-change-impact.md)

---

## Case 02 — Manufacturing MES

### 문제

현장의 “화면을 바꿔 달라”는 요청은 실제로 입력 순서, 조회 조건, 상태, 통계, 권한, DB 관계의 변경일 수 있습니다.

### 판단

요구 문구를 그대로 구현하지 않고 실제 작업 순서를 시스템 조건으로 분해합니다.

```text
field request
→ actual workflow
→ input / query
→ state rule
→ report / statistics
→ permission
→ screen + DB scope
```

### 확인 가능한 범위

- PHP 기반 MES·업무시스템 개발·유지보수
- 생산·공정·품질·재고 도메인 경험
- 현장 도입·지원 과정에서 application/data와 계정·네트워크·장비 환경 문제를 구분해 접근

[Deep dive →](cases/mes-requirement-modeling.md)

---

## Supporting signal — AI-assisted engineering

LLM 사용량 자체를 경력의 중심으로 두지 않습니다. 요구사항·기존 코드·외부 API 문서를 분석하고 구현·검토·테스트 후보를 만들 때 활용하되, 실제 코드·DB·테스트 결과와 사람이 최종 판단합니다.

[Practical AI case →](cases/practical-ai-automation.md)

---

## Public engineering evidence

### StackForge Atlas

제품 의도, interface, implementation, verification, failure/recovery를 하나의 evidence chain으로 연결합니다.

- Node pilot
- PostgreSQL durability/recovery exercise
- CI validation
- PITR/HA/failover 전체를 증명했다고 주장하지 않음

Repository: <https://github.com/tomtomjskim/stackforge-atlas>

### harness-kit

반복되는 AI coding configuration을 typed module과 deterministic generation으로 관리하는 내부도구 사례입니다.

- dependency audit gate
- typecheck
- tests
- build / CLI smoke
- publication/adoption/productivity claim 없음

Repository: <https://github.com/tomtomjskim/harness-kit>

### Codex Workflow Skills

복잡한 Agent 작업을 intake, 구현, 독립 검토, validation, closeout으로 나누고 pass/skip/not_run/failure를 구분합니다.

Repository: <https://github.com/tomtomjskim/codex-workflow-skills>

---

## Public / private boundary

공개하지 않는 정보:

- private repository와 production source
- 고객·주문·결제·배송·생산 데이터
- 내부 endpoint / hostname / credential
- raw production log와 screenshot
- 검증되지 않은 ownership·metric claim

공개 Case는 실제 문제 해결 방식을 비식별화한 설명이며 production architecture dump가 아닙니다.
