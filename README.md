# 집순이보물창고 (@jibsooni.box) — 스토어프론트

인스타 프로필에 거는 찐템 모음집. 직접 사서 써 보고 남은 살림·밥상·힐링 **21개**를
**쿠팡 인플루언서 스토어프론트 스타일**(사진 카드 2열 그리드 + 실시간 검색 + 카테고리 탭)로 모았습니다.

**라이브: https://jibsooni-box.pages.dev/** (Cloudflare Pages, 2026-11-22 스토어프론트 개편 + 18~21번 4개 추가 배포) — 배포 방법은 `DEPLOY.md`.

## 파일

- `index.html` — 페이지 (CSS/JS 포함, 외부 라이브러리·웹폰트 없음)
- `items.json` — **여기만 고치면 됩니다.** 상품·후기·가격·링크·카테고리·사진 경로·프로필 문구
- `items.js` — `build.py`가 items.json에서 자동 생성 (직접 고치지 마세요)
- `assets/` — `p01.jpg`~`p21.jpg`(제품 사진 500×500, 18~21번은 492×492) + `profile.png`(프로필 240×240)
- `build.py` — `python3 build.py` 로 items.js 재생성
- `deploy_cloudflare.py` — `python3 deploy_cloudflare.py` → `_deploy/jibsooni-box.zip` (assets 포함)
- `og.html` / `og.png` — 카톡·인스타 공유 미리보기 이미지(1200×630)
- `.nojekyll` — GitHub Pages 예비 주소용

## 화면 구성

- 상단: 프로필(원형) · `집순이보물창고` · `@jibsooni.box` · 한 줄 소개 · `👇 아래에서 번호나 사진 보고 바로 찾아보세요 👇`
- 검색창(상단 고정): `상품 이름이나 번호로 검색해 보세요 (예: 01, 행주)` — 입력 즉시 필터
  - 숫자만 입력하면 **상품 번호로만** 찾습니다 (`01` → 01번, `1` → 01번, `10` → 10번)
- 카테고리 탭: `전체 21` · `살림·정리 4` · `밥상·간식 10` · `힐링·뷰티·꿀템 7`
- 카드: 1:1 제품 사진 + 좌상단 번호 배지 → `01. 루시아이 팬트리 정리함` · 한 줄 후기 · 가격 · `쿠팡 보기 ↗`
  (카드 전체가 쿠팡 파트너스 링크, 새 탭으로 열림)
- 쿠팡 파트너스 대가성 문구: 상단(작은 글씨) · 하단(박스)

## 상품 추가·수정

1. `items.json`의 `items` 배열에 항목 추가(또는 기존 항목 수정)
   - `num`: 01~21 (카드 번호) · `category`: `living` | `table` | `care`
   - `image`: `assets/pNN.jpg` · `link`: `https://link.coupang.com/a/...`
   - `keywords`: 검색에 걸릴 단어(이름에 없는 말도 여기에 넣으면 검색됨)
2. 사진은 500×500 JPEG(30~80KB)로 `assets/`에 저장
3. `python3 build.py` → `python3 deploy_cloudflare.py` → Cloudflare 대시보드에서 zip 업로드(`DEPLOY.md`)
4. (선택) commit & push — GitHub Pages 예비 주소도 함께 갱신

링크만 채울 때: `python3 update_links.py 16 https://link.coupang.com/a/xxxx`

공정위 대가성 문구(`site.disclosure`)는 지우지 마세요.
