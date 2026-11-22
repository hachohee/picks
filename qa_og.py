import asyncio, pathlib
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--no-sandbox'])
        ctx=await b.new_context(viewport={'width':1200,'height':630}, device_scale_factor=1, locale='ko-KR')
        pg=await ctx.new_page()
        await pg.goto(pathlib.Path('/workspace/work/hotcho-picks/og.html').as_uri(), wait_until='load')
        await pg.wait_for_timeout(1200)
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(300)
        await pg.screenshot(path='/workspace/work/hotcho-picks/og.png')
        await b.close()
asyncio.run(main())
