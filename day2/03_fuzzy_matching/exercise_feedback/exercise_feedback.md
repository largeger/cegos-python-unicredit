# 🧠📊 Übung: Automatische Zuordnung von Kundenfeedback zu Produktkategorien mittels RapidFuzz

## 🎯 Ziel der Aufgabe
Du sollst ein System entwickeln, das **frei formuliertes Kundenfeedback** automatisch einer passenden **Produktkategorie** zuordnet – selbst dann, wenn Kunden:

- Wörter falsch schreiben 🤦‍♂️  
- verschiedene Begriffe benutzen 🤷‍♀️  
- Fremdwörter oder Umgangssprache nutzen 💬  

Da exakte Stringvergleiche hier versagen würden, musst du **RapidFuzz** einsetzen, um die beste Übereinstimmung zu finden.

---

## 📁 Bereitgestellte Dateien

### **1. feedbacks.csv**
Diese Datei enthält echtes Kundenfeedback:

| customer_id | feedback_text |
|-------------|---------------|
| 101 | „Ich brauche dringend Ersatz für mein Ladegerät - es funktioniert nicht mehr.“ |
| 102 | „Die Kamera vom Smarthpone macht super Bilder!“ |
| 103 | „Mein Ladekabel für das Mobile Phone ist schon wieder kaputt.“ |
| 104 | „Der Akku vom Handy hält nur noch 2 Stunden.“ |

---

### **2. kategorien.csv**
Diese Datei enthält Produktkategorien und typische Begriffe dafür:

| kategorie | beispielbegriffe |
|-----------|------------------|
| Smartphone | smartphone, handy, mobile phone |
| Ladegerät | ladegerät, charger, ladekabel |
| Akku | akku, battery, energiezelle |
| Kamera | kamera, camera, fotografiemodul |

---

## 📝 Aufgabenstellung

### **1️⃣ Dateien laden**
- Lade beide CSV-Dateien in Pandas DataFrames ein.

---

### **2️⃣ Preprocessing (leicht)**
Bring alle Texte in eine vergleichbare Form:

- Alles in **Kleinschreibung** umwandeln  
- Satzzeichen & Sonderzeichen entfernen  
- Leading/trailing spaces entfernen  

🧹 *Ziel: Die Qualität des Fuzzy-Matchings erhöhen.*

---

### **3️⃣ RapidFuzz anwenden**
Für jedes Feedback sollst du:

- die Beispielbegriffe aller Kategorien als **Kandidatenliste** verwenden  
- mittels `process.extractOne()` und z. B. `fuzz.token_set_ratio`  
- den **besten passenden Begriff** über mehrere Kategorien hinweg finden  

🔍 *Du vergleichst also jeden Feedback-Text mit allen Beispielbegriffen.*

---

### **4️⃣ Threshold setzen**
Nur Matches mit Score **≥ 70** gelten als gültig.  
Wenn der beste Score darunter liegt:

➡️ Kategorie = **"Nicht zuordenbar"** ❌

---

### **5️⃣ Ergebnis-DataFrame erstellen**
Es soll folgender Output entstehen:

| customer_id | feedback_text | zugeordnete_kategorie | matching_wort | score |
|-------------|---------------|------------------------|---------------|-------|

---

### **6️⃣ ⭐ Bonus (optional)**
Erstelle eine kleine Auswertung:

- Wie viele Feedbacks pro Kategorie? 📦  
- Wie viele waren nicht zuordenbar? ❓  
- Erstelle ein Balkendiagramm mit matplotlib 📈  

---

## 🚀 Ziel dieser Übung
Du lernst:

- Fuzzy-Matching mit RapidFuzz  
- Arbeiten mit mehreren Kandidatenlisten  
- Text-Normalisierung  
- Automatische Klassifikation von unstrukturierten Textdaten  
- Robuste pragmatische Nutzung von `extractOne()`  

