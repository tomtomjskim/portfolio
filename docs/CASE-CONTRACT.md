# Case Authoring Contract

이 문서는 `cases/*.md`의 공통 구조와 공개 Claim 상한을 정의합니다.

## Required case grammar

각 Case는 아래 순서를 유지합니다.

```text
Question
→ At a glance
→ Problem
→ Context / constraints
→ Investigation
→ Decision
→ Trade-off
→ Implementation
→ Verification / actual use
→ Limitations
→ Evidence
→ Interview hooks
```

## 15-second card contract

`At a glance`는 다음 세 항목으로 Case를 15초 안에 파악하게 합니다.

| Field | Question answered |
|---|---|
| Problem | 무엇이 어려웠는가? |
| Decision | 어떤 기준으로 무엇을 선택했는가? |
| Evidence | 무엇으로 확인할 수 있는가? |

카드 원문은 [portfolio-manifest.json](../portfolio-manifest.json)이 소유합니다. Case 파일에는 같은 문장을 사람이 읽기 쉬운 표로 투영하며, validator가 두 위치의 일치를 확인합니다.

## Case classifications

| Classification | Meaning |
|---|---|
| `sanitized-actual-work` | 실제 업무 경험을 공개 가능한 수준으로 비식별화 |
| `sanitized-actual-work-with-public-rnd-support` | 실제 업무 Case와 별도의 공개 R&D 근거를 함께 사용 |
| `public-rnd` | 공개 코드·문서·CI로 확인 가능한 현재 Engineering Artifact |

분류를 변경해 과거 회사의 production source와 공개 R&D를 혼합하지 않습니다.

## Required content rules

### Problem

- 사용자·운영자·개발자가 겪은 실제 문제를 설명
- 기술을 먼저 제시하지 않음
- 검증되지 않은 규모·성과 수치 금지

### Context / constraints

- 기존 환경과 변경 제약
- 공개할 수 없는 범위
- 기술·조직·운영 한계

### Investigation

- 어떤 질문으로 문제 범위를 좁혔는지
- 데이터·상태·권한·외부 시스템을 어떻게 확인했는지
- source가 없는 세부 구현은 후보로 쓰지 않음

### Decision / Trade-off

- 선택한 방식
- 선택하지 않은 대안
- 비용·위험·적용 조건

### Implementation

- TOM이 직접 다룬 범위
- public-safe 구조와 책임
- 내부 table·endpoint·host·credential·raw log 금지

### Verification / actual use

- 코드·DB·테스트·CI·사용자 흐름 중 실제 확인한 범위
- `not_run`, 수동 확인, private evidence를 성공으로 둔갑시키지 않음
- PR·CI·test를 release·deployment·adoption·성과 수치로 확대하지 않음

### Limitations

- 책임·성숙도·공개 범위의 상한
- Case 전체를 무력화하는 방어문이 아니라 해석 경계

### Evidence

- [EVIDENCE.md](../EVIDENCE.md)의 stable Evidence ID 참조
- 공개 repository 또는 public-safe Case link
- private source 이름과 내부 경로 금지

### Interview hooks

- 실제 면접에서 확인될 가능성이 높은 질문
- 새로운 사실을 만들지 않고 Case의 판단·책임·한계를 점검

## No-new-claim rule

Case 수정은 다음을 할 수 없습니다.

- 새로운 Career Fact 생성
- TOM의 역할을 source보다 강화
- 측정하지 않은 성과 수치 생성
- public R&D를 employer production work로 변경
- TODO·계획·prototype을 완료 기능으로 표현

근거가 부족한 세부는 `현재 공개 근거로는 확인되지 않음` 또는 `protected detail needed`로 남깁니다.
