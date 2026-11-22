# 배포 방법 (hachohee/picks → https://hachohee.github.io/picks/)

## 왜 아직 안 올라갔나
픽클의 GitHub 연결에 **저장소 생성 권한이 없어서** `gh repo create`가 403으로 막혔습니다.
(기존 `church`·`quiz`·`studywithfriends`는 권한이 있지만 새 저장소 만들기만 안 됩니다.)

## 1) 저장소만 만들어 주면 (권장, 1분)
1. https://github.com/new 접속
2. **Repository name**: `picks`
3. **Public** 선택
4. README 등 아무것도 체크하지 않고 **Create repository**
5. 픽클에게 "picks 만들었어"라고 알려 주기

→ 그러면 픽클이 이 폴더를 그대로 push하고, Settings → Pages를 켜서
`https://hachohee.github.io/picks/` 라이브까지 확인합니다.

## 2) 직접 올리는 방법 (픽클 없이)
1. 위처럼 `picks` 저장소를 만든 뒤 **uploading an existing file** 클릭
2. 아래 4개 파일을 끌어다 놓고 Commit
   - `index.html` (필수)
   - `items.js` (필수 — 상품 목록)
   - `items.json` (나중에 고칠 원본)
   - `og.png` (공유 미리보기)
3. **Settings → Pages → Build and deployment**
   - Source: `Deploy from a branch`
   - Branch: `main` / `/ (root)` → **Save**
4. 1~2분 뒤 `https://hachohee.github.io/picks/` 열림

## 3) 앱 권한으로 열기
https://github.com/apps/pickle/installations/new 에서 저장소 생성(Administration) 권한을 허용하면
앞으로 이런 페이지를 픽클이 알아서 만들 수 있습니다.

## 나중에 상품·링크 추가할 때
`items.json`만 고치고 `python3 build.py` → push. (README 참고)
