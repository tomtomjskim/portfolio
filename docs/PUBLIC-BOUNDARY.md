# Public Boundary

## Allowed

- sanitized problem definition
- TOM의 역할과 판단
- AI의 보조 범위
- 테스트·CI·검증 방식
- 확인된 제한사항
- 공개 저장소·PR·CI 링크
- synthetic diagram

## Not allowed

- 비공개 저장소명과 내부 경로
- raw AI transcript
- 고객·주문·결제·배송·생산 데이터
- credential / API key / token
- 내부 endpoint / hostname / 설정값
- 상세 운영 로그
- 보호 이력서 원천
- 검증되지 않은 생산성·시간·비용·정확도 수치
- `dna_project` 관련 career evidence

## Claim precedence

```text
current explicit user correction
→ verified current GitHub state
→ current public claim boundary
→ source lock
→ historical audit / ledger
```

충돌이 있을 때 과거 원장의 강한 상태를 자동 승격하지 않습니다.
