import os
import pandas as pd
import json
from openai import OpenAI
from dotenv import load_dotenv

# 1. Setup & Konfiguration
# ------------------------
load_dotenv() # Lädt den API Key aus der .env Datei
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

file_path = "day2/05_captstone_project/"
INPUT_FILE = file_path + "kunden_feedback.xlsx"
OUTPUT_FILE = file_path + "kunden_feedback_analyzed.xlsx"

# 2. Die AI-Funktion (Das "Gehirn")
# ---------------------------------
def analyze_text_with_ai(text):
    """
    Sendet einen Text an die AI und erwartet eine strukturierte Analyse zurück.
    """
    system_prompt = """
    Du bist ein hilfreicher Support-Analyst. 
    Analysiere das Kundenfeedback und extrahiere folgende Informationen im JSON-Format:
    1. "stimmung": (Positiv, Neutral, Negativ)
    2. "kategorie": (Logistik, Support, Buchhaltung, Produktqualität, Sonstiges)
    3. "zusammenfassung": (Eine sehr kurze Zusammenfassung des Problems in max. 5 worten)
    
    Antworte NUR mit dem JSON-Objekt.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Oder "gpt-3.5-turbo" (günstig & schnell)
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Feedback: {text}"}
            ],
            response_format={"type": "json_object"}, # Zwingt die AI zu validem JSON
            temperature=0 # 0 macht die AI deterministischer (weniger kreativ)
        )
        
        # Die Antwort der AI (String) in ein echtes Python-Dictionary umwandeln
        result_content = response.choices[0].message.content
        return json.loads(result_content)

    except Exception as e:
        print(f"⚠️ Fehler bei der AI-Anfrage: {e}")
        # Fallback-Werte, falls die API streikt
        return {"stimmung": "Fehler", "kategorie": "Manuelle Prüfung", "zusammenfassung": "API Error"}

# 3. Hauptprogramm (Der Workflow)
# -------------------------------
def main():
    print(f"📂 Lese Datei: {INPUT_FILE}...")
    
    # Excel laden
    try:
        df = pd.read_excel(INPUT_FILE)
    except FileNotFoundError:
        print("❌ Datei nicht gefunden!")
        return

    print(f"✨ Starte Analyse von {len(df)} Einträgen...\n")

    # Listen für die neuen Spalten vorbereiten
    stimmungen = []
    kategorien = []
    zusammenfassungen = []

    # Iterieren über jede Zeile (mit Index für Fortschrittsanzeige)
    for index, row in df.iterrows():
        feedback_text = row['Feedback']
        kunde = row['Kunde']
        
        print(f"   [{index+1}/{len(df)}] Analysiere Feedback von '{kunde}'...")
        
        # AI aufrufen
        analyse_ergebnis = analyze_text_with_ai(feedback_text)
        
        # Ergebnisse speichern
        stimmungen.append(analyse_ergebnis.get("stimmung"))
        kategorien.append(analyse_ergebnis.get("kategorie"))
        zusammenfassungen.append(analyse_ergebnis.get("zusammenfassung"))

    # 4. Daten zusammenfügen & Speichern
    # ----------------------------------
    df['AI_Stimmung'] = stimmungen
    df['AI_Kategorie'] = kategorien
    df['AI_Zusammenfassung'] = zusammenfassungen

    print(f"\n💾 Speichere Ergebnisse in: {OUTPUT_FILE}")
    df.to_excel(OUTPUT_FILE, index=False)
    
    # Vorschau anzeigen
    print("\n--- Fertiges Ergebnis (Vorschau) ---")
    print(df[['Kunde', 'AI_Kategorie', 'AI_Stimmung']].head(10))
    print("------------------------------------")

# Diese Bedingung überprüft, ob das Skript direkt aufgerufen wird und nicht als Modul importiert wurde. 
# Wenn __name__ den Wert "__main__" hat (was nur der Fall ist, wenn das Skript direkt ausgeführt wird), 
# dann führt sie die in main() definierten Anweisungen aus.
if __name__ == "__main__":
    main()