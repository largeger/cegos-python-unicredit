import pandas as pd
from rapidfuzz import process, fuzz
import re

# 1. Daten laden (Simulierte Datenframes für das Beispiel)
data1 = {
    'Geschäftsprozess-Name': ['EP: Inland Zahlungsverkehr', 'EP: Inland Zahlungsverkehr', 
                              'EP: SEPA  Zahlungsverkehr', 'EP: SEPA  Zahlungsverkehr', 'EP: SEPA  Zahlungsverkehr'],
    'IT-Anwendung': ['ABC', 'DEF', 'XYZ', 'GHI', 'JKL'],
    'Risikobewertung': ['Niedrig', 'Hoch', 'Mittel', 'Niedrig', 'Niedrig']
}
data2 = {
    'Geschäftsprozess-Name': ['A1.01.09 Inlands-Zahlungsverkehr', 'A1.01.10 SEPA-Zahlungsverkehr'],
    'Process Owner': ['Frau Müller', 'Herr Meier']
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 2. Bereinigungs-Funktion (Preprocessing)
# Ziel: Den "Kern" des Namens freilegen, um den Vergleich zu verbessern
def clean_name(text):
    if not isinstance(text, str): return ""
    text = text.lower()
    # Entfernt "EP:", "A1.23.45" Muster und Sonderzeichen
    text = re.sub(r'ep:', '', text) 
    text = re.sub(r'[a-z]\d+(\.\d+)+', '', text) # Entfernt A1.01.09 etc.
    text = re.sub(r'[^a-zäöüß\s]', '', text) # Nur Buchstaben behalten (keine Bindestriche)
    return text.strip()

# Hilfsspalten für das Matching erstellen
df1['clean_name'] = df1['Geschäftsprozess-Name'].apply(clean_name)
df2['clean_name'] = df2['Geschäftsprozess-Name'].apply(clean_name)

# 3. Fuzzy Matching Logik
# Wir erstellen ein Wörterbuch: {Name_in_Tabelle1 -> Passender_Name_in_Tabelle2}
mapping = {}
unique_names_t1 = df1['clean_name'].unique()
possible_matches = df2['clean_name'].tolist()

for name in unique_names_t1:
    # Findet den besten Match in Tabelle 2
    # score_cutoff=80 bedeutet: Nur Matches mit >80% Ähnlichkeit akzeptieren
    match = process.extractOne(name, possible_matches, scorer=fuzz.token_sort_ratio, score_cutoff=80)
    
    if match:
        matched_clean_name, score, index = match
        # Wir holen uns den ORIGINAL-Namen aus Tabelle 2 zurück
        original_name_t2 = df2.loc[df2['clean_name'] == matched_clean_name, 'Geschäftsprozess-Name'].iloc[0]
        mapping[name] = original_name_t2
    else:
        mapping[name] = None # Kein Match gefunden

# 4. Zusammenführen (Mergen)
# Wir mappen den originalen Namen aus T2 in T1 basierend auf dem Clean-Name
df1['Match_T2'] = df1['clean_name'].map(mapping)

# Jetzt können wir die echten Daten rüberziehen
df_final = pd.merge(df1, df2[['Geschäftsprozess-Name', 'Process Owner']], 
                    left_on='Match_T2', 
                    right_on='Geschäftsprozess-Name', 
                    how='left', 
                    suffixes=('', '_T2_Original'))

# Aufräumen (Hilfsspalten löschen)
df_final = df_final.drop(columns=['clean_name', 'Match_T2', 'Geschäftsprozess-Name_T2_Original'])

print(df_final[['Geschäftsprozess-Name', 'IT-Anwendung', 'Process Owner']])