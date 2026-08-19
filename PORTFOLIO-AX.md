# AI-assisted Engineering / Internal Tools / AX

AI 도구를 많이 사용했다는 사실보다 **어떤 문제에 AI가 필요한지, 어디까지 일반 코드로 처리하고, 어떤 판단을 사람에게 남겼는지**를 보여줍니다.

## Positioning

```text
Backend / business-system experience
→ repeated work or verification problem
→ AI suitability decision
→ deterministic boundary
→ visible failure state
→ human acceptance
```

AI Engineer로 경력을 다시 포장하지 않습니다. 운영형 백엔드 경험을 바탕으로 반복되는 개발·운영 문제를 도구화하고, AI가 들어가는 경계에서도 검증과 회수 가능성을 유지하는 방향입니다.

## Primary cases

| Case | Problem | Decision | Evidence |
|---|---|---|---|
| [Practical AI Automation](cases/practical-ai-automation.md) | 번역·복사·언어팩 반영 반복과 소형 모델의 속도·품질 한계 | 자연어 초안만 Local LLM에 맡기고 PHP/JSON 변환은 일반 코드, 최종 반영은 사람 | 실제 업무 반복 사용 + 비식별화한 Workflow |
| [Developer Internal Tooling](cases/developer-internal-tooling.md) | 프로젝트마다 Skill·Hook·MCP·Agent 설정을 복제하면 drift 발생 | 반복 비용이 생기는 경계만 typed module과 deterministic build로 공통화 | `harness-kit` 공개 코드와 Node 22/24 검증 Workflow |

## Supporting work cases

| Case | Why it matters for AX |
|---|---|
| [Commerce / Logistics Change Impact](cases/commerce-change-impact.md) | 기존 상태·권한·배치·외부 연동을 이해하지 않은 자동화는 운영 위험을 키움 |
| [Manufacturing MES Requirement Modeling](cases/mes-requirement-modeling.md) | 현업의 모호한 요청을 명시적 시스템 규칙으로 바꾸는 과정이 자동화보다 먼저 필요 |

## AI / code / human boundary

| Responsibility | Default owner | Reason |
|---|---|---|
| 비정형 자연어의 번역·분류·요약 초안 | LLM | 복수의 합리적 출력이 존재 |
| key/value 보존, 파일 생성, 상태·금액·권한 규칙 | deterministic code | 규칙이 명확하고 재현 가능해야 함 |
| 업무 맥락, 예외, 최종 반영·배포 판단 | human | 실패 비용과 운영 책임이 존재 |

AI를 넣을 수 있다는 이유만으로 사용하지 않습니다. 검증 비용이 직접 구현보다 크거나 규칙이 이미 명확하면 일반 코드 또는 사람 구현으로 회수합니다.

## Verification contract

```text
Model response != Completion evidence
```

```text
Problem / scope
→ acceptance condition
→ AI-assisted analysis or implementation
→ static check / test / Playwright E2E / execution result
→ independent review when needed
→ human acceptance
```

Agent가 `skip`, `fail`, `not_run`을 충분히 보고하지 않는 경험 이후, 완료 보고와 실제 실행 결과를 분리했습니다.

- 미실행은 성공으로 처리하지 않음
- 환경·외부 의존성 때문에 제외된 항목은 이유를 남김
- 회사 업무의 E2E·수동 검수와 공개 R&D의 CI를 구분
- UI/UX·사용자 동선·운영 영향은 사람이 확인
- PR·CI·test 통과를 배포·외부 채택·생산성으로 확대하지 않음

## Public engineering evidence

| Repository | Shows | Known boundary |
|---|---|---|
| [harness-kit](https://github.com/tomtomjskim/harness-kit) | configuration as code, typed modules, deterministic generation, dependency/test/build gates | npm 미배포, 외부 채택 없음 |
| [codex-workflow-skills](https://github.com/tomtomjskim/codex-workflow-skills) | intake, independent review, failure accounting, validation, closeout | live model 품질·조직 생산성 증거가 아님 |
| [stackforge-atlas](https://github.com/tomtomjskim/stackforge-atlas) | intent, interface, evidence, recovery 연결 | bounded engineering pilot |
| [claude-code-guide](https://github.com/tomtomjskim/claude-code-guide) | Skill·Hook·Agent·Handoff·Failure Recovery 운영 가이드 | 저장소 전체가 회사 프로젝트에 적용됐다는 뜻이 아님 |

전체 상태와 근거 경계: [EVIDENCE.md](EVIDENCE.md)

## Navigate

- General Backend 관점: [PORTFOLIO.md](PORTFOLIO.md)
- Case 목록: [README.md](README.md#selected-case-studies)
- 공개 경계: [docs/PUBLIC-BOUNDARY.md](docs/PUBLIC-BOUNDARY.md)
