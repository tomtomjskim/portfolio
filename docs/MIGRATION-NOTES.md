# Migration Notes

Target repository: `tomtomjskim/portfolio`

Purpose: 개인 이직용 public portfolio. `jsnetworkcorp-*` / `jsnwcorp-*` 사업 namespace와 분리한다.

## Selected from previous work

- general backend positioning
- Commerce / Logistics sanitized case
- Manufacturing MES sanitized case
- Practical Local LLM / verification case
- Developer Internal Tooling case
- public evidence links and limitation boundaries

## Intentionally not migrated

- Next.js/web application source
- website routes, screenshots, deployment artifacts
- resume variants and applicant-specific text
- jsnetworkcorp branding / business namespace
- claim-generation machinery and private registry
- internal source paths / protected evidence
- obsolete or hold evidence as primary case

## Known source conflicts resolved for this migration

1. `aiwright`
   - historical ledger: portfolio-ready
   - current public claim boundary: hold
   - migration decision: **hold**

2. Local LLM i18n
   - older G0 review: evidence absent → hold
   - later explicit user correction and subsequent sanitized case review: actual internal use confirmed; i18n output structure verified; private translation-server source remains unavailable publicly
   - migration decision: **sanitized primary work case with explicit limitations**

3. `db-mcp`
   - PR #3 remains draft/mergeable with warning and formatting debt
   - migration decision: **supporting-hold; not a primary case**

4. Personal Wiki resume v4 PR #19
   - open / draft / non-mergeable
   - migration decision: **do not use branch-only protected text as public authority**
