import asyncio, pathlib
from playwright.async_api import async_playwright
URL=pathlib.Path('/workspace/work/hotcho-picks/index.html').as_uri()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--no-sandbox'])
        for w,name in ((320,'hotcho_picks_320.png'),(390,'hotcho_picks_preview.png')):
            ctx=await b.new_context(viewport={'width':w,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True,locale='ko-KR')
            pg=await ctx.new_page(); errs=[]
            pg.on('pageerror',lambda e: errs.append(str(e)))
            pg.on('console',lambda m: errs.append('console:'+m.text) if m.type=='error' else None)
            await pg.goto(URL,wait_until='load'); await pg.wait_for_timeout(1200)
            if w==320:
                await pg.screenshot(path='/workspace/downloads/'+name)
            else:
                await pg.screenshot(path='/workspace/downloads/'+name, full_page=True)
                await pg.screenshot(path='/workspace/downloads/hotcho_picks_top.png')
            print(w,'errors',errs,'doc',await pg.evaluate("document.documentElement.scrollWidth"))
            await ctx.close()
        await b.close()
asyncio.run(main())
