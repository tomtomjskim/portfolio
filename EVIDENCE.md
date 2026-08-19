# Public Evidence Index

이 문서는 포트폴리오에서 실제로 연결하는 **대표 공개 evidence와 검증 경계**만 정리합니다. 내부 후보군·보류 자산·private source registry는 공개하지 않습니다.

## Primary

### harness-kit

- Shows: developer internal tooling, typed configuration, deterministic generation, validation/CI
- Verification boundary: dependency audit, typecheck, tests, build, CLI smoke
- Limitation: production adoption, npm publication, productivity metric은 주장하지 않음
- Repository: <https://github.com/tomtomjskim/harness-kit>

### codex-workflow-skills

- Shows: intake, independent review, failure accounting, validation, closeout
- Verification boundary: forward-test에서 pass와 external skip/not_run을 분리
- Limitation: test count가 live model 품질·생산성·조직 채택을 증명하지 않음
- Repository: <https://github.com/tomtomjskim/codex-workflow-skills>

### stackforge-atlas

- Shows: intent → interface → evidence → recovery, DB durability/recovery exercise
- Verification boundary: public code와 CI, bounded recovery exercise
- Limitation: full production PITR/HA/replication/failover proof가 아님
- Repository: <https://github.com/tomtomjskim/stackforge-atlas>

### Local LLM i18n workflow

- Shows: 실제 반복 언어팩 업무에 Local LLM을 적용하고 deterministic conversion과 human validation을 분리한 사례
- Verification boundary: public에는 sanitized workflow와 responsibility boundary만 사용
- Limitation: private translation-server source/address, productivity/accuracy/cost metric은 공개·주장하지 않음
- Case: [cases/practical-ai-automation.md](cases/practical-ai-automation.md)

## Selective supporting

### claude-code-guide

- Use: Skill, Hook, Handoff, Failure Recovery의 학습·일반화 근거
- Limitation: 저장소 전체 기능을 모든 회사 프로젝트에서 사용했다고 주장하지 않음
- Repository: <https://github.com/tomtomjskim/claude-code-guide>

## Evidence rules

- PR/CI/test pass != release/deployment/adoption
- 공개 R&D != employer production source
- 실제 업무 case와 현재 공개 engineering artifact를 구분
- 측정하지 않은 생산성·시간·비용·정확도 수치 금지
- private repo/path/customer data/endpoint/credential/raw log 공개 금지
