from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.google.com")

    # --- Cookie Banner akzeptieren ---
    # Google EU-Cookie Banner: Button "Alle ablehnen" oder "Alle akzeptieren"
    try:
        page.locator("button:has-text('Alle akzeptieren')").click(timeout=3000)
    except:
        try:
            page.locator("button:has-text('Ich stimme zu')").click(timeout=3000)
        except:
            pass  # Banner erscheint nicht immer

    # --- Eingabefeld ausfüllen ---
    page.fill("textarea[name='q']", "Playwright Python Browser Automation")
    page.keyboard.press("Enter")

    # Warten bis Ergebnisse sichtbar
    page.wait_for_selector("#search")

    # Screenshot machen
    page.screenshot(path="google.png")

    browser.close()
