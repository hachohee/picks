# 집순이보물창고 (@jibsooni.box) — 찐템 모음집

인스타 프로필에 거는 링크 모음 페이지. 직접 사서 써 보고 남은 살림·밥상·힐링 찐템 17개와
한 줄 찐후기, 쿠팡 파트너스 링크를 한 장에 모았습니다.

- `index.html` — 페이지 (CSS/JS 포함, 외부 라이브러리 없음)
- `items.json` — **여기만 고치면 됩니다.** 상품·후기·가격·링크·카테고리·프로필 문구
- `items.js` — `build.py`가 items.json에서 자동 생성 (직접 고치지 마세요)
- `build.py` — `python3 build.py` 로 items.js 재생성
- `.nojekyll` — GitHub Pages 그대로 서빙
- `og.html` / `og.png` — 카톡·인스타 공유 미리보기 이미지(1200×630)

## 새 상품 / 파트너스 링크 추가
1. `items.json`의 `items` 배열에 항목 추가(또는 기존 항목의 `link` 채우기)
   - `link`: `https://link.coupang.com/a/...` (있으면 '쿠팡에서 보기' 활성화)
   - `opens`: (선택) 링크가 없을 때 버튼에 붙일 날짜. 비우면 "곧 링크 연결 중"으로 표시
   - `category`: `living` | `table` | `care`
2. `python3 build.py`
3. commit & push → GitHub Pages 자동 반영

링크만 채울 때는 더 간단합니다:
`python3 update_links.py 16 https://link.coupang.com/a/xxxx https://blog.naver.com/hachohee/123`

## 프로필 바꾸기
`items.json`의 `site`에서 `brand`(이름), `account`(핸들), `badge`, `title`, `intro` 수정.

공정위 대가성 문구(`site.disclosure`)는 지우지 마세요.
