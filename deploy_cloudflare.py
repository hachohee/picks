#!/usr/bin/env python3
"""Cloudflare Pages 업로드용 zip 만들기.

    python3 deploy_cloudflare.py
    -> _deploy/jibsooni-box.zip  (index.html, items.js, items.json, og.png, assets/*)

만든 zip을 https://dash.cloudflare.com/ → Workers 및 Pages → jibsooni-box
→ 배포 생성 → 파일 끌어서 놓기 에서 올리면 https://jibsooni-box.pages.dev/ 에 반영된다.
"""
import pathlib
import subprocess
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
FILES = ["index.html", "items.js", "items.json", "og.png"]
EXTRA = []  # 필요할 때만 임시 파일 이름을 넣는다 (예: 390px 미리보기 _p390.html)
ASSET_DIR = "assets"
OUT = ROOT / "_deploy" / "jibsooni-box.zip"


def main() -> None:
    missing = [f for f in FILES if not (ROOT / f).exists()]
    if missing:
        raise SystemExit(f"파일이 없습니다: {missing}")
    extra = [f for f in EXTRA if (ROOT / f).exists()]
    assets = sorted(p for p in (ROOT / ASSET_DIR).iterdir() if p.is_file())
    if not assets:
        raise SystemExit("assets/ 폴더가 비어 있습니다.")

    # items.js가 items.json보다 오래됐으면 먼저 다시 만든다.
    if (ROOT / "items.json").stat().st_mtime > (ROOT / "items.js").stat().st_mtime:
        subprocess.run(["python3", "build.py"], cwd=ROOT, check=True)

    OUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for name in FILES:
            z.write(ROOT / name, name)
        for name in extra:
            z.write(ROOT / name, name)
        for p in assets:
            z.write(p, f"{ASSET_DIR}/{p.name}")

    size = OUT.stat().st_size
    print(f"{OUT.relative_to(ROOT.parent)}  ({size:,} bytes, 파일 {len(FILES) + len(extra) + len(assets)}개)")
    print("업로드: Cloudflare 대시보드 → Workers 및 Pages → jibsooni-box → 배포 생성 → 파일 끌어서 놓기")


if __name__ == "__main__":
    main()
