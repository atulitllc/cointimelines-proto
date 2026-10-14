import sys,asyncio
from playwright.async_api import async_playwright
BASE=sys.argv[1]; OUT=sys.argv[2]
PAGES=[("home",""),("btc-timeline","bitcoin/history/"),("xrp-event","xrp/events/2020-sec-lawsuit/"),("compare","compare/xrp-vs-solana-for-payments/"),("guide","guides/how-blockchains-work/"),("year","bitcoin/history/2017/")]
async def main():
    import os; os.makedirs(OUT,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for dev,vp in [("desktop",dict(width=1366,height=900)),("mobile",dict(width=390,height=844))]:
            for th in ["light","dark"]:
                ctx=await b.new_context(viewport=vp,device_scale_factor=1 if dev=="desktop" else 2,is_mobile=dev=="mobile")
                await ctx.add_init_script(f"localStorage.setItem('ct-theme','{th}')")
                pg=await ctx.new_page(); errs=[]
                pg.on("pageerror",lambda e:errs.append(str(e)))
                for name,path in PAGES:
                    r=await pg.goto(BASE+path,wait_until="networkidle")
                    await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
                    ch=await pg.query_selector(".chart")
                    if ch: await ch.scroll_into_view_if_needed(); await pg.wait_for_timeout(2800)
                    n=await pg.evaluate("document.querySelectorAll('.chart svg path.line').length")
                    mk=await pg.evaluate("document.querySelectorAll('.chart .mk').length")
                    await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(300)
                    await pg.screenshot(path=f"{OUT}/{name}-{dev}-{th}.png",full_page=(name in("home","btc-timeline")))
                    print(dev,th,name,r.status,"charts",n,"markers",mk,errs)
                await ctx.close()
        await b.close()
asyncio.run(main())
