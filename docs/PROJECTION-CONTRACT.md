# Portfolio Projection Contract

## Roles

```text
tomtomjskim/portfolio
= canonical public Case and Evidence source

tomtomjskim/tomtomjskim
= GitHub Profile entrypoint

tomtomjskim/tomtomjskim.github.io
= visual presentation layer
```

Web은 이 저장소의 내용을 보여주는 downstream projection이며 경력 사실·Claim·Case 원문을 새로 소유할 수 없습니다.

## Source selection

GitHub Pages build는 floating `main`을 바로 사용하지 않습니다.

```text
portfolio repository
+ exact source commit SHA
+ site build commit SHA
+ generated-at timestamp
```

사이트 저장소의 source manifest 예시:

```json
{
  "source_repository": "tomtomjskim/portfolio",
  "source_commit": "<40-character commit SHA>",
  "site_commit": "<40-character commit SHA>",
  "generated_at": "<ISO 8601 timestamp>"
}
```

source commit 변경은 별도 PR로 검수합니다.

## Content ownership

| Content | Owner |
|---|---|
| Case order and 15-second card metadata | `portfolio-manifest.json` |
| Full Case prose | `cases/*.md` |
| Backend / AX selection views | `PORTFOLIO.md`, `PORTFOLIO-AX.md` |
| Evidence state and limitations | `EVIDENCE.md` |
| Public/private policy | `docs/PUBLIC-BOUNDARY.md` |
| Visual components, layout, route rendering | user-site repository |

Site repository에서 Case 문장을 수동 복제해 유지하지 않습니다.

## Initial route contract

```text
/
/cases/commerce-change-impact
/cases/mes-requirement-modeling
/cases/practical-ai-automation
/cases/developer-internal-tooling
/about
```

초기 release에서는 public-safe reviewed resume가 없으므로 `/resume`를 만들지 않습니다.

## Build contract

```text
checkout site
→ checkout portfolio at exact commit
→ validate portfolio manifest and Markdown
→ render static pages
→ generate provenance manifest
→ static export
→ deploy GitHub Pages
```

## Required QA

- desktop and mobile rendering
- keyboard navigation and visible focus
- semantic headings
- contrast
- no horizontal overflow
- 404 route
- favicon / OpenGraph / sitemap / robots
- broken-link check
- static export
- visible source provenance
- public/private boundary scan

## Prohibited

- Web에서 새로운 Career Fact·Claim 생성
- `portfolio/main`을 검수 없이 자동 배포
- Case prose의 독립 복사본 유지
- public R&D를 employer production으로 재서술
- private repository·path·customer data·credential 노출
- 검증되지 않은 production metric·adoption·SLA 추가
