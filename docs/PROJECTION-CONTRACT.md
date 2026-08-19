# 웹사이트 반영 기준

## 저장소 역할

```text
tomtomjskim/portfolio
= 공개 사례와 근거의 원문

tomtomjskim/tomtomjskim
= GitHub 프로필 진입점

tomtomjskim/tomtomjskim.github.io
= 화면 구성과 정적 웹사이트
```

GitHub Pages는 이 저장소의 내용을 읽어 보여주는 화면 계층입니다. 새로운 경력 사실이나 사례 문장을 따로 관리하지 않습니다.

## 단순한 반영 원칙

```text
portfolio/main
→ 내용 검증
→ 정적 사이트 빌드
→ GitHub Pages 배포
```

별도의 commit SHA 고정 파일이나 이중 이력 관리는 사용하지 않습니다. 변경 내역과 되돌리기는 각 저장소의 Git 이력과 PR로 관리합니다.

## 내용 관리 위치

| 내용 | 관리 위치 |
|---|---|
| 사례 순서와 요약 문장 | `portfolio-manifest.json` |
| 전체 사례 원문 | `cases/*.md` |
| 백엔드·AI 활용 관점별 선택 | `PORTFOLIO.md`, `PORTFOLIO-AX.md` |
| 근거 상태와 한계 | `EVIDENCE.md` |
| 공개·비공개 기준 | `docs/PUBLIC-BOUNDARY.md` |
| 화면 구성·스타일·경로 | GitHub Pages 저장소 |

웹사이트 저장소에서 전체 사례 문장을 복사해 별도로 유지하지 않습니다.

## 초기 경로

```text
/
/cases/commerce-change-impact
/cases/mes-requirement-modeling
/cases/practical-ai-automation
/cases/developer-internal-tooling
/about
```

공개 가능한 검토 완료 이력서가 없으므로 초기 버전에는 `/resume`을 만들지 않습니다.

## 빌드 흐름

```text
사이트 저장소 받기
→ portfolio/main 내용 받기
→ manifest와 Markdown 검증
→ 정적 페이지 생성
→ GitHub Pages 배포
```

## 필수 점검

- 데스크톱·모바일 화면
- 키보드 이동과 포커스 표시
- 제목 구조
- 글자 대비
- 가로 넘침 없음
- 404 화면
- 파비콘·공유 미리보기·사이트맵·robots
- 링크 확인
- 정적 빌드
- 공개 범위 검사

## 금지 사항

- 웹사이트에서 새로운 경력 사실·주장 생성
- 사례 원문의 독립 복사본 유지
- 공개 연구·개발 자료를 이전 회사의 운영 업무로 재서술
- 비공개 저장소·경로·고객 데이터·credential 노출
- 검증되지 않은 운영 수치·외부 채택·SLA 추가
