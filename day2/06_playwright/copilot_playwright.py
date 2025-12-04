import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://copilot.microsoft.com/")
    page.get_by_test_id("cookie-banner-reject-button").click()
    page.get_by_test_id("composer-input").click()
    page.get_by_test_id("composer-input").fill("Generiere mir eine Übersicht über die Anzahl der Angestellten und der Höhe des Umsatzes für alle großen deutschen Banken")
    page.wait_for_timeout(10000)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
