import asyncio, pathlib, json
from playwright.async_api import async_playwright
URL = pathlib.Path('/workspace/work/hotcho-picks/index.html').as_uri()
OUT = pathlib.Path('/workspace/downloads')
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--no-sandbox'])
        for w in (320, 360, 390, 430):
            ctx = await b.new_context(viewport={'width':w,'height':844}, device_scale_factor=2, is_mobile=True, has_touch=True, locale='ko-KR')
            page = await ctx.new_page()
            errs=[]; page.on('pageerror', lambda e: errs.append(str(e)))
            await page.goto(URL, wait_until='load'); await page.wait_for_timeout(1000)
            m = await page.evaluate("""() => ({
                doc: document.documentElement.scrollWidth, view: innerWidth,
                over: [...document.querySelectorAll('.card, .meta, .actions, .chip')].filter(e=>e.getBoundingClientRect().right > innerWidth+1 || e.scrollWidth > e.clientWidth+1).length,
                chipRows: new Set([...document.querySelectorAll('.chip')].map(e=>Math.round(e.getBoundingClientRect().top))).size,
                cardH: [...document.querySelectorAll('.card')].map(e=>Math.round(e.getBoundingClientRect().height)).slice(0,6)
            })""")
            print(w, m, 'errors', errs)
            if w == 390:
                # footer + item note area
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await page.wait_for_timeout(300)
                await page.screenshot(path=str(OUT/'hotcho_picks_bottom.png'))
                # #8 card with long note
                await page.evaluate("document.querySelectorAll('.card')[1].scrollIntoView({block:'center'})")
                await page.wait_for_timeout(300)
                await page.screenshot(path=str(OUT/'hotcho_picks_card2.png'))
            await ctx.close()
        await b.close()
asyncio.run(main())
