# 🐼 Verkaufsdaten-Analyse: Lösung

import pandas as pd
import numpy as np

# -------------------------------
# 1. Datensatz erstellen
# -------------------------------
data = {
    'Datum': ['2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03', '2024-01-04'],
    'Produkt': ['Laptop', 'Maus', 'Monitor', 'Laptop', 'Tastatur', 'Maus'],
    'Kategorie': ['Elektronik', 'Zubehoer', 'Elektronik', 'Elektronik', 'Zubehoer', 'Zubehoer'],
    'Preis': [1200, 25, 300, 1200, np.nan, 25],  # Ein fehlender Preis
    'Menge': [1, 10, 2, 1, 5, 12],
    'Stadt': ['Berlin', 'Muenchen', 'Berlin', 'Hamburg', 'Berlin', 'Muenchen']
}

df = pd.DataFrame(data)

# -------------------------------
# Aufgabe A: Erster Überblick
# -------------------------------
print("=== Erste 5 Zeilen ===")
print(df.head(), "\n")

print("=== Info ===")
print(df.info(), "\n")

print("=== Statistische Kennzahlen ===")
print(df.describe(), "\n")

# -------------------------------
# Aufgabe B: Datenbereinigung
# -------------------------------

# Fehlenden Preis ersetzen
df['Preis'].fillna(45.0, inplace=True)

# Datum in datetime konvertieren
df['Datum'] = pd.to_datetime(df['Datum'])

print("=== Nach Datenbereinigung ===")
print(df, "\n")

# -------------------------------
# Aufgabe C: Feature Engineering
# -------------------------------
df['Umsatz'] = df['Preis'] * df['Menge']

print("=== Mit Umsatz-Spalte ===")
print(df, "\n")

# -------------------------------
# Aufgabe D: Analyse & Filterung
# -------------------------------

# Verkäufe in Berlin
berlin_sales = df[df['Stadt'] == 'Berlin']
print("=== Verkäufe in Berlin ===")
print(berlin_sales, "\n")

# Verkauf mit höchstem Umsatz
max_sale = df[df['Umsatz'] == df['Umsatz'].max()]
print("=== Verkauf mit höchstem Umsatz ===")
print(max_sale, "\n")

# -------------------------------
# Aufgabe E: Gruppierung & Aggregation
# -------------------------------

# Gesamtumsatz pro Stadt
total_sales_per_city = df.groupby('Stadt')['Umsatz'].sum()
print("=== Gesamtumsatz pro Stadt ===")
print(total_sales_per_city, "\n")

# Gesamtmenge pro Kategorie
total_quantity_per_category = df.groupby('Kategorie')['Menge'].sum()
print("=== Gesamtmenge pro Kategorie ===")
print(total_quantity_per_category, "\n")
