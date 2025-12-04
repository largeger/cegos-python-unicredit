import pandas as pd
from rapidfuzz import process, fuzz

file_path = "day2/03_fuzzy_matching/exercise_feedback/"
# 1. Dateien laden
feedbacks = pd.read_csv(file_path + 'feedbacks.csv')
kategorien = pd.read_csv(file_path + 'kategorien.csv')

# 2. Preprocessing: Alles in Kleinschreibung umwandeln und Satzzeichen entfernen
feedbacks['feedback_text'] = feedbacks['feedback_text'].str.lower().str.replace('[^\w\s]', '', regex=True).str.strip()
kategorien['beispielbegriffe'] = kategorien['beispielbegriffe'].str.lower().str.replace('[^\w\s|]', '', regex=True).str.strip()

#print(feedbacks)
#print(kategorien)

# 3. RapidFuzz anwenden
results = []
for idx, row in feedbacks.iterrows():
    best_match = None
    best_score = -1
    
    for _, kategorie_row in kategorien.iterrows():
        begriffe_liste = kategorie_row['beispielbegriffe'].split('|')
        for begriff in begriffe_liste:
            score = fuzz.partial_ratio(row['feedback_text'], begriff)
            if score > best_score:
                # print(f"Score zwischen '{row['feedback_text']}' und '{begriff}': {score}")
                best_score = score
                best_match = kategorie_row['kategorie']
                matching_begriff = begriff
    
    result_row = {
        'customer_id': row['customer_id'],
        'feedback_text': row['feedback_text'],
        'zugeordnete_kategorie': best_match,
        'matching_wort': None if best_score < 70 else matching_begriff,
        'score': best_score
    }
    
    results.append(result_row)

# 4. Ergebnis-DataFrame erstellen
ergebnisse = pd.DataFrame(results)
print(ergebnisse)

# 5. Auswertung (Bonus)
auswertung = ergebnisse['zugeordnete_kategorie'].value_counts().reset_index()
auswertung.columns = ['Kategorie', 'Anzahl']
nicht_zuordenbar = ergebnisse[ergebnisse['matching_wort'].isnull()].shape[0]

print("\nAuswertung:")
print(f"Feedbacks pro Kategorie:\n{auswertung}")
print(f"Nicht zuordenbare Feedbacks: {nicht_zuordenbar}")

# 6. Balkendiagramm erstellen (Bonus)
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.bar(auswertung['Kategorie'], auswertung['Anzahl'])
plt.xlabel('Kategorie')
plt.ylabel('Anzahl')
plt.title('Feedbacks pro Kategorie')
plt.show()
