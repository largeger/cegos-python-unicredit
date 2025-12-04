import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    page.get_by_role("searchbox", name="Search Wikipedia").click()
    page.get_by_role("searchbox", name="Search Wikipedia").fill("unicredit")
    page.get_by_role("link", name="Unicredit italienische").click()
    page.get_by_role("cell", name="69.722").click()
    page.get_by_role("cell", name="69.722").click()

    # Screenshot machen
    page.screenshot(path="wikipedia.png")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)