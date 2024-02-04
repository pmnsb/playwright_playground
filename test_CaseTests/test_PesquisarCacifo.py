import asyncio
import time
from playwright.async_api import Playwright, async_playwright, expect

async def test_run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://appserver.ctt.pt/CustomerArea/LockersMap?cacifosbutton=")
    await page.get_by_role("button", name="Accept All Cookies").click()
    await page.get_by_placeholder("Cidade, código postal ou ID").click()
    time.sleep(3)
    await page.get_by_placeholder("Cidade, código postal ou ID").press_sequentially('Alverca')
    # await page.get_by_placeholder("Cidade, código postal ou ID").fill("Alverca")
    await page.get_by_text("Alverca do Ribatejo").click()
    await page.locator("div:nth-child(24)").click()
    await page.get_by_text("Ver detalhe").click()
    await page.get_by_role("button", name="Faça login para adicionar").click()
    expected_url = 'https://www.ctt.pt/fecas/login?service=https%3A%2F%2Fwww.ctt.pt%2Ffecas%2Foauth20%2FcallbackAuthorize'
    await expect(page).to_have_url(expected_url)
    await context.close()
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await test_run(playwright)

asyncio.run(main())