# 공개 근거 목록

이 문서는 공개 포트폴리오가 연결하는 근거의 **종류, 확인 가능한 범위, 해석 상한**을 관리합니다.

```text
비식별화한 실무 사례
= 실제 경력의 문제·판단·사용 범위를 공개 가능한 수준으로 설명

공개 개발 자료
= 공개 코드·문서·CI로 현재 확인 가능한 구현과 검증 방식
```

공개 연구·개발 자료를 이전 회사의 운영 코드나 실무 성과로 표현하지 않습니다.

## 실무 사례

<a id="ev-career-commerce"></a>
### EV-CAREER-COMMERCE — 커머스·물류

- **구분:** 비식별화한 실무 사례
- **보여주는 내용:** PHP/MySQL 커머스·물류 운영 시스템의 상태·권한·관리자·batch/cron·외부 API 변경 영향 분석
- **공개 표현:** [커머스·물류 변경 영향 분석](cases/commerce-change-impact.md)
- **근거 강도:** 실제 경력 원천은 비공개이며, 이 공개 저장소만으로 독립 검증할 수 없음
- **비공개 범위:** 경력 원천과 내부 프로젝트 자료
- **증명하지 않는 것:** 전체 커머스 구조 책임, 운영 SLA·트래픽·매출 수치, 모든 트랜잭션·멱등성·정산 대사 구현

<a id="ev-career-mes"></a>
### EV-CAREER-MES — 제조 MES

- **구분:** 비식별화한 실무 사례
- **보여주는 내용:** 현장 요구를 입력·조회·상태·통계·권한·DB 조건으로 분해하고 도입·지원에서 문제 계층을 구분한 경험
- **공개 표현:** [제조 MES 요구사항 모델링](cases/mes-requirement-modeling.md)
- **근거 강도:** 실제 경력 원천은 비공개이며, 이 공개 저장소만으로 독립 검증할 수 없음
- **비공개 범위:** 고객사·공장·생산 데이터와 내부 제품 구조
- **증명하지 않는 것:** 전체 MES 제품 책임, 모든 고객사 단독 구축, 클라우드 SaaS·SLA 성과

<a id="ev-local-i18n"></a>
### EV-LOCAL-I18N — 로컬 LLM 언어팩 작업

- **구분:** 비식별화한 실제 사용 사례
- **보여주는 내용:** Python + Ollama/Gemma 3 번역 초안, 별도 PHP 언어팩 생성·JSON 변환, 사람 검수의 책임 분리
- **실제 사용:** 프론트 개발자가 반복 언어팩 작업에 사용
- **공개 표현:** [실무형 AI 자동화](cases/practical-ai-automation.md)
- **근거 강도:** 실제 사용 진술은 확인된 범위로 제한하며 구현 소스는 공개하지 않음
- **비공개 범위:** 번역 서버 소스와 내부 경로
- **증명하지 않는 것:** 번역 정확도·생산성·비용 절감률, GPU 추론 서버 운영, 완전 자동 번역

## 공개 개발 자료

<a id="ev-harness-kit"></a>
### EV-HARNESS-KIT — harness-kit

- **구분:** 공개 연구·개발 / 내부 도구
- **보여주는 내용:** 지침·Hook·MCP·권한·Agent·작업 흐름·Skill 설정의 모듈화와 규칙 기반 생성
- **구현 근거:** 설정 해석, 불러오기, 검증, 병합, 출력 생성, 파일 기록 흐름
- **검증:** Node 22/24, `high` 기준 의존성 보안 점검, TypeScript 검사, 테스트, 빌드, CLI 기본 실행 확인
- **저장소:** <https://github.com/tomtomjskim/harness-kit>
- **증명하지 않는 것:** npm 배포, 외부 채택, 조직 전체 사용, 생산성 향상

<a id="ev-codex-workflow"></a>
### EV-CODEX-WORKFLOW — codex-workflow-skills

- **구분:** 공개 연구·개발 / 작업 규칙
- **보여주는 내용:** 작업 접수, 구현, 독립 검토, 실패 상태 기록, 검증, 마무리
- **검증 범위:** 공개 검증에서 `pass`와 외부 의존성에 따른 `skip`·`not_run`을 분리
- **저장소:** <https://github.com/tomtomjskim/codex-workflow-skills>
- **증명하지 않는 것:** 실제 모델 품질, 배포, 외부 채택, 조직 생산성

<a id="ev-stackforge"></a>
### EV-STACKFORGE — stackforge-atlas

- **구분:** 공개 연구·개발 / 개발 기준 모음
- **보여주는 내용:** 제품 의도 → 인터페이스 → 구현 → 근거 → 실패·복구 연결
- **검증 범위:** 공개 코드, CI, 제한된 PostgreSQL 내구성·복구 실험
- **저장소:** <https://github.com/tomtomjskim/stackforge-atlas>
- **증명하지 않는 것:** 전체 운영 환경의 PITR·고가용성·복제·장애 전환 책임

<a id="ev-claude-guide"></a>
### EV-CLAUDE-GUIDE — claude-code-guide

- **구분:** 선택형 보조 가이드
- **보여주는 내용:** Skill·Hook·Agent 규칙과 인수인계·실패 복구 방식의 공개 가이드·템플릿
- **저장소:** <https://github.com/tomtomjskim/claude-code-guide>
- **증명하지 않는 것:** 저장소 전체 기능의 회사 프로젝트 적용, 조직 도입, 성과 수치

## 근거 사용 원칙

- PR·CI·테스트 통과는 배포·운영 반영·외부 채택이 아닙니다.
- 공개 연구·개발 자료는 이전 회사의 운영 소스가 아닙니다.
- 실제 업무 사례와 현재 공개 개발 자료를 분리합니다.
- 측정하지 않은 생산성·시간·비용·정확도 수치를 사용하지 않습니다.
- 비공개 저장소·내부 경로·고객 데이터·endpoint·credential·원본 로그를 공개하지 않습니다.
- 공개 근거가 바뀌면 사례보다 먼저 이 문서와 [portfolio-manifest.json](portfolio-manifest.json)의 참조를 갱신합니다.
