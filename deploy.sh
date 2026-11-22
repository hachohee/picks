#!/bin/sh
# hachohee/picks 저장소가 생기면 이 스크립트 한 번으로 배포 + Pages 활성화.
set -e
cd "$(dirname "$0")"

REPO=hachohee/picks
if ! gh repo view "$REPO" >/dev/null 2>&1; then
  echo "먼저 https://github.com/new 에서 hachohee/picks (Public) 저장소를 만들어 주세요."
  exit 2
fi

git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/${REPO}.git"
git remote set-url origin "https://github.com/${REPO}.git"

git fetch origin main 2>/dev/null || true
if git rev-parse --verify -q origin/main >/dev/null; then
  COUNT=$(gh api "repos/${REPO}/commits?per_page=5" --jq 'length')
  FIRST=$(gh api "repos/${REPO}/commits?per_page=5" --jq '.[-1].commit.message')
  if [ "$COUNT" = "1" ]; then
    echo "빈 저장소(초기 커밋 1개)라 그대로 덮어씁니다."
    git push -f -u origin HEAD:main
  else
    echo "저장소에 이미 커밋이 있습니다. 강제로 덮지 않습니다: $FIRST"
    exit 3
  fi
else
  git push -u origin HEAD:main
fi

# Pages: main 브랜치 루트에서 서빙
if gh api "repos/${REPO}/pages" >/dev/null 2>&1; then
  echo "Pages 이미 켜져 있음"
else
  gh api -X POST "repos/${REPO}/pages" -f "source[branch]=main" -f "source[path]=/" >/dev/null \
    && echo "Pages 활성화 요청 완료" || echo "Pages API 실패 — GitHub Settings > Pages 에서 main / (root) 선택 필요"
fi

echo "https://hachohee.github.io/picks/ (반영까지 1~2분)"
