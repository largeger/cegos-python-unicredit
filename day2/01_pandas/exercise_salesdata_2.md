# 🧩 Pandas Challenge #2: CRM & Sales Analyse (Fortgeschritten)

Willkommen zur nächsten Stufe! Hier simulieren wir einen echten Business-Case: Du musst Bestelldaten mit Kundendaten verknüpfen.

---

## 1. 🛠️ Das Szenario & Setup

Wir haben zwei Datensätze:
1.  **`df_orders`**: Die Bestellungen (Transaktionen).
2.  **`df_customers`**: Die Stammdaten der Kunden (CRM).

Kopiere diesen Code, um zu starten:

```python
import pandas as pd
import numpy as np

# Tabelle 1: Bestellungen
orders_data = {
    'Order_ID': [101, 102, 103, 104, 105, 106],
    'Datum': ['2024-02-15', '2024-02-16', '2024-03-01', '2024-03-05', '2024-03-10', '2024-04-01'],
    'Kunden_ID': [1, 2, 1, 3, 2, 99], # Kunde 99 existiert nicht in der Kunden-DB!
    'Betrag': [150.00, 25.50, 500.00, 45.00, 120.00, 30.00]
}

# Tabelle 2: Kunden
customer_data = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Land': ['DE', 'AT', 'DE', 'CH'],
    'Status': ['Gold', 'Silver', 'Bronze', 'Gold']
}

df_orders = pd.DataFrame(orders_data)
df_customers = pd.DataFrame(customer_data)
```

---

## 2. ⚡ Deine Mission

### Aufgabe A: Der "Merge" (Daten verknüpfen) 🤝

Wir wollen wissen, welcher Kunde welche Bestellung getätigt hat.

1.  Verbinde `df_orders` (links) mit `df_customers` (rechts).
2.  **Wichtig:** Nutze einen **Left Join**, damit wir keine Bestellungen verlieren (auch wenn der Kunde nicht gefunden wird, wie bei Kunde 99).
3.  *Hinweis:* Die Spalten heißen unterschiedlich (`Kunden_ID` vs. `ID`).
4.  Speichere das Ergebnis in einem neuen DataFrame namens `df_full`.

### Aufgabe B: Zeit-Analyse 📅

Wir wollen wissen, in welchem Monat wir am meisten Umsatz machen.

1.  Konvertiere die Spalte `Datum` in `datetime`.
2.  Erstelle eine neue Spalte `Monat` (z.B. als Name "February" oder Zahl 2).
      - *Tipp:* Nutze `df['Datum'].dt.month_name()` oder `.dt.month`.
3.  Wie hoch war der **Gesamtumsatz pro Monat**?

### Aufgabe C: Komplexe Filterung (Die "VIPs") 💎

Wir suchen "High Potential" Transaktionen.
Filtere `df_full` nach Zeilen, die **eine** der folgenden Bedingungen erfüllen:

  * Der Kunde hat den Status **"Gold"**.
  * **ODER**: Der Bestellwert (`Betrag`) ist **größer als 200€**.

### Aufgabe D: Pivot-Tabelle 📊

Erstelle eine Übersichtstabelle (Matrix), die folgendes zeigt:

  * **Zeilen:** `Land`
  * **Spalten:** `Status`
  * **Werte:** Durchschnittlicher `Betrag`