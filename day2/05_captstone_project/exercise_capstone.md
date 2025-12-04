# 🚀 Capstone Projekt: Der "Auto-Analyst"

Willkommen zum finalen Projekt des Tages! Jetzt setzen wir alle Bausteine zusammen: **Excel, Python und Künstliche Intelligenz.**

---

### 📖 Das Szenario
Dein Teamleiter im Customer Support ertrinkt in Arbeit. Jeden Tag kommen hunderte Feedback-Einträge von Kunden rein. Manche sind wütend, manche glücklich, manche haben technische Probleme.

Bis jetzt muss jemand diese Liste **manuell** lesen und in eine Excel-Tabelle eintragen:
* Ist das positiv oder negativ?
* Geht es um Logistik oder das Produkt?
* Was ist die Kurzfassung?

**Deine Mission:** Baue einen Bot, der diese Arbeit in Sekunden erledigt!

---

### 🎯 Das Ziel
Schreibe ein Python-Skript, das:
1.  Die Datei `kunden_feedback.xlsx` einliest.
2.  Jeden Feedback-Text an die **OpenAI API** sendet.
3.  Die Antwort der AI analysiert (Sentiment & Kategorie).
4.  Eine **neue Excel-Datei** speichert, die um die Analyse-Spalten erweitert wurde.

---

### 🛠️ Schritt-für-Schritt Anleitung

#### 1. Setup & Imports 📦
Erstelle ein neues Skript (z.B. `auto_analyst.py`).
Lade deinen API Key sicher aus der `.env` Datei.
* **Benötigte Module:** `pandas`, `openai`, `os`, `json`, `dotenv`

#### 2. Daten laden 📄
Lese die Datei `kunden_feedback.xlsx` in einen Pandas DataFrame.
* *Check:* Lass dir die ersten 5 Zeilen mit `print(df.head())` ausgeben, um sicherzugehen, dass es geklappt hat.

#### 3. Das "Gehirn" bauen (Die AI-Funktion) 🧠
Schreibe eine Funktion `analyze_text(text)`, die den Text an GPT-4o-mini (oder gpt-3.5-turbo) sendet.
**Wichtig:** Der System-Prompt muss der AI genau sagen, wie sie antworten soll.

> **Der Prompt-Befehl:**
> "Du bist ein Analyst. Extrahiere aus dem Text folgende Daten als JSON:
> - `stimmung` (Positiv, Neutral, Negativ)
> - `kategorie` (Logistik, Support, Produkt, Sonstiges)
> - `zusammenfassung` (Max 5 Wörter)"

💡 **Pro-Tipp:** Nutze im API-Call den Parameter `response_format={"type": "json_object"}`, damit die AI garantiert valides JSON zurückgibt!

#### 4. Die Automatisierung (Der Loop) 🔄
* Erstelle leere Listen für `stimmungen`, `kategorien` und `zusammenfassungen`.
* Iteriere durch den DataFrame (nutze `df.iterrows()`).
* Sende in jedem Durchlauf das Feedback an deine AI-Funktion.
* Speichere die Ergebnisse in den Listen.

#### 5. Speichern & Feierabend 💾
Füge die Listen als neue Spalten zum DataFrame hinzu:
```python
df['AI_Stimmung'] = stimmungen
# ... usw
```
Speichere das Ergebnis als `kunden_feedback_analyzed.xlsx`.

---

### 💡 Tipps & Tricks
- **JSON Parsing**: Die AI antwortet mit einem String, der aussieht wie JSON. Nutze import json und data = json.loads(antwort_string), um daraus ein echtes Python-Dictionary zu machen.
- **Kosten sparen**: Zum Testen reicht es, wenn du den Loop nach 2-3 Durchläufen abbrichst (mit break), damit du nicht bei jedem Testlauf alle Zeilen verarbeitest.
- **Error Handling**: Was passiert, wenn die API mal nicht antwortet? Ein try-except Block rettet dein Programm vor dem Absturz!

---

### 🏆 Bonus-Challenge (für die Schnellen)
Die Excel-Datei ist fertig? Super! Versuche nun, basierend auf der Spalte `AI_Stimmung`, eine bedingte Formatierung einzubauen oder eine Statistik auszugeben:

- Wie viel Prozent der Kunden sind negativ eingestellt?
- Welche Kategorie verursacht die meisten Probleme?