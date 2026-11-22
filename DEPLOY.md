# 배포 방법 — https://jibsooni-box.pages.dev/ (Cloudflare Pages)

집순이보물창고의 **정식 주소는 Cloudflare Pages**입니다. 주소에 `hachohee`가 들어가지 않습니다.

- 라이브: **https://jibsooni-box.pages.dev/**
- Cloudflare 프로젝트명: `jibsooni-box` (계정 hachohee@gmail.com, Direct Upload = Git 연결 없음)
- 배포 기록: 2026-11-22 09:52(KST) 첫 배포 · 배포 ID `741d4f8b` (https://741d4f8b.jibsooni-box.pages.dev)

## 내용 고칠 때 (상품·링크 추가)

1. `items.json`만 고친다 → `python3 build.py` (items.js 재생성)
2. 오늘 날짜의 og:url/og:image는 `https://jibsooni-box.pages.dev/` 그대로 두면 된다.
3. `python3 deploy_cloudflare.py` → `_deploy/jibsooni-box.zip` 생성
4. Cloudflare 대시보드에 업로드:
   1. https://dash.cloudflare.com/ → Workers 및 Pages → `jibsooni-box`
   2. **배포 생성** → 파일 끌어서 놓기(**전체 내용** = zip 선택) → `_deploy/jibsooni-box.zip`
   3. **사이트 배포** → 30초 뒤 같은 주소에 반영
5. 확인: https://jibsooni-box.pages.dev/ 를 열어 카드 개수·쿠팡 링크를 훑는다.

올리는 파일은 4개뿐이다: `index.html`, `items.js`, `items.json`, `og.png`.

## 예전 GitHub Pages 주소

`https://hachohee.github.io/picks/` 도 저장소(`hachohee/picks`)에 그대로 살아 있다.
링크를 공유할 때는 **Cloudflare 주소만** 쓴다. (og:url도 Cloudflare 주소로 맞춰 두었다.)
GitHub 쪽이 필요 없어지면 저장소 Settings → Pages에서 끄면 된다.
