import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def test_run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www2.ctt.pt/particulares/index")
    await page.get_by_role("button", name="Definições de cookies").click()
    await page.get_by_role("button", name="Permitir todos").click()
    await page.get_by_role("link", name="").click()
    await page.get_by_role("button", name="Entrar").click()
    await page.get_by_label("Email  *").click()
    await page.get_by_label("Email  *").fill("pedro.m.bento@cttexpresso.pt")
    await page.get_by_label("Password  *").click()
    await page.get_by_label("Password  *").fill("Teste123")
    await page.get_by_role("button", name="Login").click()
    # time.sleep(3)
    #assert page.expect_request(url_or_predicate="https://www2.ctt.pt/particulares/index")
    await expect(page).to_have_url(re.compile("https://www2.ctt.pt/particulares/index"))

    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await test_run(playwright)

asyncio.run(main())
