# AI 활용·내부 도구

운영형 백엔드 업무에서 실제 사용한 AI 자동화 사례와 공개 개발 자료를 분리해 정리합니다.

## 실제 사용 사례

### 실무형 AI 자동화

다국어 UI 언어팩 작업에서 로컬 LLM은 번역 초안을 만들고, 별도 프로그램은 PHP 언어팩 생성과 JSON 변환을 담당했습니다. 번역 맥락과 최종 반영은 사람이 확인했습니다.

[문서 보기](cases/practical-ai-automation.md)

## 공개 개발 자료

### 개발자 내부 도구

프로젝트마다 복제되던 Skill·Hook·MCP·Agent 설정을 모듈과 규칙 기반 생성으로 관리한 공개 개발 사례입니다.

[문서 보기](cases/developer-internal-tooling.md) · [harness-kit](https://github.com/tomtomjskim/harness-kit)

### 관련 저장소

| 저장소 | 확인 가능한 내용 |
|---|---|
| [codex-workflow-skills](https://github.com/tomtomjskim/codex-workflow-skills) | 작업 접수·독립 검토·실패 상태·완료 검증을 분리한 작업 규칙 |
| [stackforge-atlas](https://github.com/tomtomjskim/stackforge-atlas) | 제품 의도·인터페이스·근거·복구 경계를 연결한 개발 기준 모음 |
| [claude-code-guide](https://github.com/tomtomjskim/claude-code-guide) | Skill·Hook·Agent 규칙과 인수인계·실패 복구 방식을 정리한 가이드와 템플릿 |

## 관련 업무 사례

- [커머스·물류 변경 영향 분석](cases/commerce-change-impact.md)
- [제조 MES 요구사항 모델링](cases/mes-requirement-modeling.md)

AI 활용 자료는 위 업무 사례를 대체하지 않습니다. 공개 코드와 회사 실무의 역할도 서로 바꿔 표현하지 않습니다.

근거의 종류와 확인 범위는 [EVIDENCE.md](EVIDENCE.md)에서 확인할 수 있습니다.

## 관련 문서

- 전체 목록: [README.md](README.md)
- 백엔드 경력 관점: [PORTFOLIO.md](PORTFOLIO.md)
- 공개 범위: [docs/PUBLIC-BOUNDARY.md](docs/PUBLIC-BOUNDARY.md)
