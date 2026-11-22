#!/usr/bin/env python3
"""2~4탄 파트너스 링크가 나오면 카드에 바로 연결하는 도구.

    python3 update_links.py 16 https://link.coupang.com/a/xxxx
    python3 update_links.py 16 https://link.coupang.com/a/xxxx https://blog.naver.com/hachohee/123456

번호(1~17)는 work/coupang_partners_reviews.md의 원래 번호와 같습니다.
링크를 넣으면 '곧 링크 연결 중' 버튼이 '쿠팡에서 보기'로 바뀌고, items.js가 다시 만들어집니다.
"""
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).resolve().parent


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    try:
        no = int(sys.argv[1])
    except ValueError:
        print("첫 번째 인자는 상품 번호(숫자)여야 합니다.")
        return 2
    link = sys.argv[2].strip()
    blog = sys.argv[3].strip() if len(sys.argv) > 3 else None

    path = root / "items.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = next((it for it in data["items"] if it["id"] == no), None)
    if target is None:
        print(f"{no}번 상품이 items.json에 없습니다. 번호를 확인해 주세요.")
        return 1
    if not link.startswith("https://link.coupang.com/"):
        print("경고: 쿠팡 파트너스 단축 링크(https://link.coupang.com/...)가 아닙니다. 그대로 저장합니다.")

    target["link"] = link
    target["opens"] = None
    if blog:
        target["blog"] = blog
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    subprocess.run([sys.executable, str(root / "build.py")], check=True)
    print(f"{no}번 '{target['name']}' 연결 완료")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
