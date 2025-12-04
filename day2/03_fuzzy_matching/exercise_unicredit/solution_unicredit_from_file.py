import pandas as pd
from rapidfuzz import process, fuzz

file_path = "day2/03_fuzzy_matching/exercise_unicredit/"

# 1. Excel-Dateien einlesen
df1 = pd.read_excel(file_path + "Tabelle_1.xlsx")
df2 = pd.read_excel(file_path + "Tabelle_2.xlsx")

# 2. Fuzzy-Matching Funktion
def fuzzy_match(row, choices, scorer=fuzz.token_set_ratio, threshold=70):
    match, score, _ = process.extractOne(row, choices, scorer=scorer)
    if score >= threshold:
        # print(f"Match gefunden: '{row}' -> '{match}' (Score: {score})")
        return match
    return None

# 3. Neue Spalte in df1 mit dem besten Match aus df2
df1['Matched_Process_Name'] = df1['Geschäftsprozess-Name'].apply(
    lambda x: fuzzy_match(x, df2['Geschäftsprozess-Name'])
)

# 4. Inner Join nur für erfolgreiche Matches
df_joined = pd.merge(
    df1,
    df2,
    left_on='Matched_Process_Name',
    right_on='Geschäftsprozess-Name',
    how='inner',
    suffixes=('_T1', '_T2')
)

# 5. Ergebnis DataFrame erstellen
result = df_joined[[
    'Geschäftsprozess-Name_T1',
    'Zugehörige IT-Anwendung',
    'Risikobewertung der IT-Anwendung',
    'Process Owner des Geschäftsprozesses'
]]

# 6. Ergebnis speichern
result.to_excel("Fuzzy_Join_Ergebnis.xlsx", index=False)

print("Fuzzy-Join erfolgreich! Ergebnis gespeichert als 'Fuzzy_Join_Ergebnis.xlsx'.")
print(result)
