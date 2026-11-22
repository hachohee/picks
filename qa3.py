import asyncio, pathlib
from playwright.async_api import async_playwright
URL=pathlib.Path('/workspace/work/hotcho-picks/index.html').as_uri()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--no-sandbox'])
        ctx=await b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True,locale='ko-KR')
        pg=await ctx.new_page(); await pg.goto(URL,wait_until='load'); await pg.wait_for_timeout(1200)
        await pg.evaluate("document.querySelectorAll('.card')[4].scrollIntoView({block:'start'})")
        await pg.wait_for_timeout(400)
        await pg.screenshot(path='/workspace/downloads/hotcho_picks_soon_card.png')
        txt=await pg.eval_on_selector_all('.soon','e=>e.map(x=>x.textContent)')
        print(len(txt), set(txt))
        await b.close()
asyncio.run(main())
