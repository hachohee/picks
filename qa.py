import asyncio, json, pathlib, os
from playwright.async_api import async_playwright

URL = pathlib.Path('/workspace/work/hotcho-picks/index.html').as_uri()
OUT = pathlib.Path('/workspace/downloads')

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--no-sandbox'])
        ctx = await b.new_context(viewport={'width':390,'height':844}, device_scale_factor=2,
                                  is_mobile=True, has_touch=True, locale='ko-KR',
                                  user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
        page = await ctx.new_page()
        errors, msgs = [], []
        page.on('console', lambda m: (errors if m.type=='error' else msgs).append(m.text))
        page.on('pageerror', lambda e: errors.append('pageerror: '+str(e)))
        await page.goto(URL, wait_until='load')
        await page.wait_for_timeout(1500)
        try: await page.evaluate("document.fonts.ready")
        except Exception: pass
        await page.wait_for_timeout(300)

        info = await page.evaluate("""() => {
          const r = {};
          r.title = document.title;
          r.cards = document.querySelectorAll('.card').length;
          r.tabs = [...document.querySelectorAll('.tab')].map(t => t.textContent.trim());
          r.brand = document.querySelector('#brand')?.textContent;
          r.handle = document.querySelector('#handle')?.textContent;
          r.tagline = document.querySelector('#title')?.textContent;
          r.buy = document.querySelectorAll('.buy').length;
          r.soon = document.querySelectorAll('.soon').length;
          r.docW = document.documentElement.scrollWidth; r.viewW = innerWidth;
          r.overflowers = [...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right > innerWidth+1).map(e=>e.className+'|'+e.textContent.slice(0,20)).slice(0,10);
          r.fonts = [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family).filter((v,i,a)=>a.indexOf(v)===i);
          r.heroH = Math.round(document.querySelector('.hero').getBoundingClientRect().height);
          r.disclosure = document.querySelector('#disclosure').textContent;
          r.firstCardH = Math.round(document.querySelector('.card').getBoundingClientRect().height);
          return r;
        }""")
        print(json.dumps(info, ensure_ascii=False, indent=2))
        await page.screenshot(path=str(OUT/'hotcho_picks_preview.png'), full_page=True)
        await page.screenshot(path=str(OUT/'hotcho_picks_top.png'))
        for cat, expect in [('living',4),('table',8),('care',5),('all',17)]:
            await page.click(f'.tab[data-cat="{cat}"]')
            await page.wait_for_timeout(500)
            n = await page.eval_on_selector_all('.card', 'els => els.length')
            print('filter', cat, '->', n, 'expected', expect, 'OK' if n==expect else 'MISMATCH')
        await page.click('.tab[data-cat="living"]')
        await page.wait_for_timeout(550)
        await page.screenshot(path=str(OUT/'hotcho_picks_filter.png'))
        hrefs = await page.eval_on_selector_all('.buy', 'els => els.map(e=>e.getAttribute("href"))')
        print('buy hrefs:', hrefs)
        print('console errors:', errors)
        print('console other:', msgs[:5])
        await b.close()

asyncio.run(main())
