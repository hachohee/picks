#!/usr/bin/env python3
"""items.json -> items.js

고칠 내용은 items.json 한 곳만 고치고 이 스크립트를 실행하면 items.js가 다시 만들어집니다.
(새 상품/새 파트너스 링크는 items.json에만 추가하면 됩니다. index.html은 items.js를 읽습니다.)
    python3 build.py
"""
import json
import pathlib

root = pathlib.Path(__file__).resolve().parent
data = json.loads((root / "items.json").read_text(encoding="utf-8"))

# 사람이 읽기 좋은 형태로 떨어뜨린다(자동 업데이트 스크립트가 문자열만 바꿔도 깨지지 않게).
body = json.dumps(data, ensure_ascii=False, indent=2)
(root / "items.js").write_text(
    "/* build.py가 items.json에서 자동 생성합니다. 직접 고치지 마세요. */\n"
    f"window.PICKS_DATA = {body};\n",
    encoding="utf-8",
)

cats = {}
for it in data["items"]:
    cats[it["category"]] = cats.get(it["category"], 0) + 1
live = sum(1 for it in data["items"] if it.get("link"))
print(f"items: {len(data['items'])} | 바로 구매 {live} | 순차 공개 {len(data['items']) - live}")
print("categories:", cats)
