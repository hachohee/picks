# 배포 방법 — https://jibsooni-box.pages.dev/ (Cloudflare Pages)

집순이보물창고의 **정식 주소는 Cloudflare Pages**입니다. 주소에 `hachohee`가 들어가지 않습니다.

- 라이브: **https://jibsooni-box.pages.dev/**
- Cloudflare 프로젝트명: `jibsooni-box` (계정 hachohee@gmail.com, Direct Upload = Git 연결 없음)
- 배포 기록
  - 2026-11-22 09:52(KST) 첫 배포
  - 2026-11-22 10:13(KST) **스토어프론트 개편** — 17개 실제 제품 사진 카드(2열 그리드) + 실시간 검색 + 카테고리 탭

## 내용 고칠 때 (상품·링크·사진)

1. `items.json`만 고친다 → `python3 build.py` (items.js 재생성)
2. `python3 deploy_cloudflare.py` → `_deploy/jibsooni-box.zip` 생성
3. Cloudflare 대시보드에 업로드:
   1. https://dash.cloudflare.com/ → Workers 및 Pages → `jibsooni-box`
   2. **배포 생성** → 파일 끌어서 놓기(**전체 내용** = zip 선택) → `_deploy/jibsooni-box.zip`
   3. **저장 및 배포** → 30초 뒤 같은 주소에 반영
4. 확인: https://jibsooni-box.pages.dev/ 를 열어 카드 17장·사진·검색·탭을 훑는다.

올리는 파일(22개): `index.html`, `items.js`, `items.json`, `og.png` + `assets/`(p01~p17.jpg, profile.png)

## 제품 사진 규격

- `assets/p01.jpg` ~ `assets/p17.jpg` = **01~17번 상품 사진** (500×500 JPEG, 품질 86, 15~80KB)
- 원본은 `work/coupang_ep1~4/` (ep1 = 01~04, ep2 = 05~09, ep3/ep4 = 10~17)
- 사진을 바꿀 때는 같은 이름으로 덮어쓰면 된다. `items.json`의 `"image"` 경로와 번호만 맞추면 됨.
- 프로필은 `assets/profile.png` (240×240, 원형으로 잘려 보임)

## 예전 GitHub Pages 주소

`https://hachohee.github.io/picks/` 도 같은 소스가 그대로 올라가 있다(예비 주소).
링크를 공유할 때는 **Cloudflare 주소만** 쓴다. (og:url도 Cloudflare 주소로 맞춰 두었다.)
