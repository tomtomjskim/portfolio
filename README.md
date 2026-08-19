# 김정식 | 백엔드 개발 포트폴리오

PHP/MySQL 기반 커머스·물류·MES 업무시스템을 개발·운영해 온 백엔드 개발자입니다.

기능을 변경할 때 화면이나 단일 함수부터 고치기보다 **AS-IS 코드, DB 상태, 권한, 관리자 흐름, batch/cron, 외부 API가 실제로 연결되는 범위**를 먼저 확인합니다. LLM과 Agent는 분석·구현·검토를 보조하지만, 완료 여부는 코드·테스트·실행 결과와 사람의 판단으로 확인합니다.

## 시작하기

- **백엔드 개발 관점:** [PORTFOLIO.md](PORTFOLIO.md)
- **AI 활용·내부 도구 관점:** [PORTFOLIO-AX.md](PORTFOLIO-AX.md)
- **공개 근거와 한계:** [EVIDENCE.md](EVIDENCE.md)

## 대표 사례

| 사례 | 문제 | 판단 | 근거 |
|---|---|---|---|
| [커머스·물류 변경 영향 분석](cases/commerce-change-impact.md) | 화면 증상이 DB 상태·관리자·배치·외부 연동까지 이어짐 | 화면 수정 전에 상태 변경 주체와 후속 영향을 추적 | 비식별화한 실무 사례와 프로젝트 검수 범위 |
| [제조 MES 요구사항 모델링](cases/mes-requirement-modeling.md) | “화면 변경” 요청이 상태·조회·통계·권한 규칙을 숨김 | 실제 작업 순서를 시스템 조건으로 분해 | 비식별화한 실무 사례와 현장 도입·지원 범위 |
| [실무형 AI 자동화](cases/practical-ai-automation.md) | 번역·복사·언어팩 반영이 반복되고 소형 모델에 한계가 있음 | 자연어는 로컬 LLM, 파일 변환은 규칙 기반 코드, 최종 판단은 사람 | 실제 반복 사용한 언어팩 작업 흐름과 공개 검증 원칙 |
| [개발자 내부 도구](cases/developer-internal-tooling.md) | 여러 프로젝트의 AI 코딩 도구 설정을 복제하면 중복과 설정 불일치가 발생 | 반복 비용이 생기는 경계만 타입이 정의된 모듈과 규칙 기반 생성으로 공통화 | `harness-kit` 공개 코드와 Node 22/24 검증 흐름 |

## 이 저장소 읽는 법

```text
실무 사례
= 실제 경력에서 확인된 문제·판단·업무 범위를 공개 가능한 수준으로 비식별화

공개 개발 자료
= 공개 코드와 CI로 확인할 수 있는 설계·구현·검증 방식
```

두 종류의 근거를 서로 바꿔 말하지 않습니다. 사례 원문은 `cases/`, 공개 근거의 상태와 한계는 [EVIDENCE.md](EVIDENCE.md)에서 확인할 수 있습니다.

## 공개 개발 자료

- [stackforge-atlas](https://github.com/tomtomjskim/stackforge-atlas) — 제품 의도·인터페이스·검증 근거·복구 경계를 연결하는 개발 기준 모음
- [harness-kit](https://github.com/tomtomjskim/harness-kit) — AI 코딩 도구 설정을 모듈과 규칙 기반 빌드로 관리하는 내부 도구
- [codex-workflow-skills](https://github.com/tomtomjskim/codex-workflow-skills) — 작업 접수·독립 검토·실패 상태·완료 검증을 분리한 작업 규칙
- [claude-code-guide](https://github.com/tomtomjskim/claude-code-guide) — Skill·Hook·Agent 규칙과 인수인계·실패 복구 방식을 정리한 가이드와 템플릿

## 원문과 웹사이트 반영

이 저장소가 공개 사례의 원문입니다. 향후 GitHub Pages는 이 저장소의 `main` 내용을 빌드할 때 읽어 화면으로 보여주며, 별도의 경력 사실이나 사례 문장을 따로 관리하지 않습니다.

- 화면 구성용 목록: [portfolio-manifest.json](portfolio-manifest.json)
- 사례 작성 기준: [docs/CASE-CONTRACT.md](docs/CASE-CONTRACT.md)
- 웹사이트 반영 기준: [docs/PROJECTION-CONTRACT.md](docs/PROJECTION-CONTRACT.md)
- 공개 범위: [docs/PUBLIC-BOUNDARY.md](docs/PUBLIC-BOUNDARY.md)

GitHub 프로필: <https://github.com/tomtomjskim>
