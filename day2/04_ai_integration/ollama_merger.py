import pandas as pd
import ollama
import json
import re

# 1. Daten laden (Hier simulieren wir Ihre Excel-Daten)
data1 = {
    'Geschäftsprozess-Name': [
        'EP: Inland Zahlungsverkehr', 
        'EP: Inland Zahlungsverkehr', 
        'EP: SEPA  Zahlungsverkehr', 
        'EP: SEPA  Zahlungsverkehr', 
        'ABC Prozess unbekannt' # Ein Testfall ohne Match
    ],
    'IT-Anwendung': ['ABC', 'DEF', 'XYZ', 'GHI', 'TEST']
}

data2 = {
    'Geschäftsprozess-Name': [
        'A1.01.09 Inlands-Zahlungsverkehr', 
        'A1.01.10 SEPA-Zahlungsverkehr'
    ],
    'Process Owner': ['Frau Müller', 'Herr Meier']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Listen der eindeutigen Namen erstellen
list_t1 = df1['Geschäftsprozess-Name'].unique().tolist()
list_t2 = df2['Geschäftsprozess-Name'].unique().tolist()

print(f"Sende {len(list_t1)} Einträge an Ollama zum Abgleich...")

# 2. Der Prompt für das lokale Modell
# WICHTIG: Lokale Modelle brauchen sehr klare Anweisungen.
prompt = f"""
Du bist ein Daten-Mapping-Assistent. Deine Aufgabe ist es, unscharfe Strings zu matchen.

Ich habe zwei Listen mit Geschäftsprozess-Namen.
Liste 1 enthält 'schmutzige' Daten (Prefixe wie 'EP:', Tippfehler).
Liste 2 enthält die sauberen Stammdaten.

Aufgabe:
Ordne jedem Element aus Liste 1 das passendste Element aus Liste 2 zu.
Ignoriere Codes (wie A1.01) und Prefixe (wie EP:). Achte auf die inhaltliche Bedeutung.

Liste 1 (Input): {json.dumps(list_t1, ensure_ascii=False)}
Liste 2 (Target): {json.dumps(list_t2, ensure_ascii=False)}

Antworte NUR mit einem JSON-Objekt, das die Zuordnung zeigt:
{{
  "Name aus Liste 1": "Name aus Liste 2",
  "Anderer Name aus Liste 1": null
}}
Wenn kein passender Eintrag gefunden wird, setze den Wert auf null.
"""

# 3. Anfrage an Ollama
try:
    response = ollama.chat(
        model='qwen3',  # Oder 'mistral', 'gemma2', etc.
        messages=[{'role': 'user', 'content': prompt}],
        format='json',    # Zwingt das Modell zu JSON-Output (sehr wichtig!)
        options={'temperature': 0} # 0 macht das Modell deterministischer/logischer
    )
    
    response_content = response['message']['content']
    print("Antwort von Ollama erhalten.")

    # 4. Verarbeitung der Antwort
    mapping_dict = json.loads(response_content)
    
    # Mapping auf Tabelle 1 anwenden
    df1['Mapped_Name'] = df1['Geschäftsprozess-Name'].map(mapping_dict)
    
    # Merge durchführen
    df_final = pd.merge(
        df1, 
        df2, 
        left_on='Mapped_Name', 
        right_on='Geschäftsprozess-Name', 
        how='left',
        suffixes=('', '_Master')
    )
    
    # Ergebnis anzeigen
    print("\n--- Ergebnis ---")
    print(df_final[['Geschäftsprozess-Name', 'Mapped_Name', 'Process Owner']])

except json.JSONDecodeError:
    print("Fehler: Das Modell hat kein gültiges JSON zurückgegeben.")
    print("Raw Output:", response_content)
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")