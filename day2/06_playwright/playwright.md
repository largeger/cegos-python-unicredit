# Einführung in Playwright (Python) 🎭
Playwright ist ein Framework zur Web-Automatisierung und zum End-to-End-Testing, das von Microsoft entwickelt wird. Es ermöglicht die Steuerung von modernen Webbrowsern wie Chromium (Basis von Chrome/Edge), Firefox und WebKit (Safari).

## Warum Playwright?
Im Gegensatz zu älteren Tools (wie Selenium) bietet Playwright entscheidende Vorteile:
- **Auto-Waiting**: Playwright wartet automatisch, bis Elemente sichtbar und klickbar sind, bevor eine Aktion ausgeführt wird. Das eliminiert instabile sleep()-Befehle ("Flakiness").
- **Ein API für alle Browser**: Der gleiche Code funktioniert in Chrome, Firefox und Safari.
- **Headless Mode**: Browser können unsichtbar im Hintergrund laufen (für CI/CD Pipelines) oder sichtbar (zum Debuggen).

## Die Grundstruktur
Playwright organisiert den Browser in drei Hierarchie-Ebenen. Dies ist wichtig für saubere Tests:

1. **Browser**: Die eigentliche Browser-Instanz (z. B. Chromium). Sie wird nur einmal gestartet.

2. **Context**: Ein isolierter Bereich innerhalb des Browsers (vergleichbar mit einem "Inkognito-Fenster"). Cookies und Cache werden nicht zwischen Kontexten geteilt.

3. **Page**: Ein einzelner Tab oder ein Fenster innerhalb eines Kontexts. Hier finden die Aktionen statt.

```python
# Konzeptuelles Beispiel (Sync API)
browser = playwright.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
```

## Navigation und Interaktion
Die API ist sehr sprechend gestaltet und nutzt einfache Verben.
- `page.goto("URL")`: Öffnet eine Webseite.
- `page.click("selector")`: Klickt auf ein Element.
- `page.fill("selector", "text")`: Füllt ein Textfeld aus.
- `page.screenshot(path="bild.png")`: Erstellt einen Screenshot.

## Locators: Elemente finden
Das Herzstück von Playwright sind die Locators. Ein Locator ist eine Regel, um ein Element auf der Seite zu finden. Playwright empfiehlt, Elemente so zu finden, wie ein Benutzer sie sieht (nach Text oder Label), statt nach technischen IDs.

- **Nach Text**: page.locator("text=Login")
- **Nach CSS**: page.locator(".btn-primary")
- **Nach Rolle (Best Practice)**: page.get_by_role("button", name="Senden")

### Strict Mode
Playwright ist standardmäßig strikt. Wenn du page.click("button") ausführst, aber 3 Buttons auf der Seite sind, bricht Playwright mit einem Fehler ab, anstatt "irgendeinen" zu klicken. Du musst deinen Selektor dann präziser machen.

## Playwright Inspector & Codegen
Ein mächtiges Feature ist der Code-Generator. Du kannst durch das Web surfen und Playwright schreibt den Code für dich:

```bash
# Befehl im Terminal (nicht im Notebook)
playwright codegen wikipedia.org
```