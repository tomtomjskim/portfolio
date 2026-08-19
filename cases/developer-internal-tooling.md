# Developer Internal Tooling — Configuration as Code

## Problem

여러 프로젝트에서 AI coding 설정, 규칙, Hook, MCP, Agent/Workflow 구성을 반복 복제하면 중복과 drift가 생깁니다.

## Decision

프로젝트 수가 적고 변경이 드물면 직접 편집을 유지합니다. 반복 변경 비용이 실제로 발생하는 경계만 typed module과 deterministic generation으로 공통화합니다.

```text
repeated config
→ typed module
→ validation
→ deterministic generation
→ audit / test / build / smoke
```

## Public evidence

[harness-kit](https://github.com/tomtomjskim/harness-kit)

검증 기록은 공개 repository/CI로 확인할 수 있습니다. npm publication, 외부 채택, 생산성 향상은 별도 근거가 없어 주장하지 않습니다.

## Engineering signal

- abstraction을 목적 자체로 두지 않음
- configuration drift를 검증 가능한 pipeline으로 다룸
- dependency/security gate를 functional green과 분리
- 구현·검증·한계를 같은 페이지에서 설명
