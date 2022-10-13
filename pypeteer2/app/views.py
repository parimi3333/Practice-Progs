from django.shortcuts import render
import asyncio
from pyppeteer import launch
# Create your views here.

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://duckduckgo.com/")
    await page.screenshot({'path':'C:\Users\Lenovo\Pictures\Camera Roll\scrsp.png'})
    dimensions = await page.evaluate('''() => {
            return {
                width: document.documentElement.clientWidth,
                height: document.documentElement.clientHeight,
                deviceScaleFactor: window.devicePixelRatio,
            }
        }''')
    print(dimensions)
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
