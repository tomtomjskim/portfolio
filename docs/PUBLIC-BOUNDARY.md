# Public Boundary

## Allowed

- 비식별화한 문제 정의와 업무 맥락
- TOM이 직접 판단·설계·구현·검수한 확인 범위
- AI·일반 코드·사람의 책임 분리
- 테스트·E2E·CI·수동 확인 등 실제 검증 방식
- 확인된 제한사항과 미검증 범위
- 공개 저장소·PR·CI 링크
- synthetic diagram
- public-safe Case와 machine-readable metadata

## Not allowed

- 비공개 저장소명과 내부 경로
- raw AI transcript
- 고객·주문·결제·배송·생산 데이터
- credential·API key·token
- 내부 endpoint·hostname·설정값
- 상세 운영 log·screenshot
- 보호 이력서 원천
- 검증되지 않은 생산성·시간·비용·정확도·SLA 수치
- 이력서·포트폴리오 근거에서 제외한 내부 자산
- 공개 R&D를 이전 회사의 production source로 표현

## Claim precedence

```text
current explicit TOM correction
→ verified current GitHub state
→ current public Claim boundary
→ source lock
→ historical audit / ledger
```

충돌할 때 과거 문서의 강한 상태를 자동 승격하지 않습니다.

## Projection boundary

```text
portfolio source
→ exact commit
→ validated static projection
```

GitHub Pages는 presentation layer입니다. Web 문장과 source가 다르면 `tomtomjskim/portfolio`의 검수된 source commit을 기준으로 되돌립니다.

## Review questions

공개 전 다음을 확인합니다.

1. 이 문장은 실제 업무 Case인가, 공개 R&D인가?
2. TOM의 직접 역할이 source보다 강해졌는가?
3. 측정하지 않은 수치가 추가됐는가?
4. private path·data·endpoint·credential이 노출됐는가?
5. TODO·prototype·CI pass를 완료 운영 성과로 확대했는가?
6. Case와 Evidence의 limitation이 서로 일치하는가?
