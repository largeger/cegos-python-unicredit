import pandas as pd
import numpy as np

# ==========================================
# 1. SETUP & DATEN GENERIEREN
# ==========================================
print("--- 1. Setup: Daten werden generiert ---")

# Tabelle 1: Bestellungen
orders_data = {
    'Order_ID': [101, 102, 103, 104, 105, 106],
    'Datum': ['2024-02-15', '2024-02-16', '2024-03-01', '2024-03-05', '2024-03-10', '2024-04-01'],
    'Kunden_ID': [1, 2, 1, 3, 2, 99], # Kunde 99 existiert nicht in Customers!
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

print("Orders (Head):")
print(df_orders.head(2))
print("\nCustomers (Head):")
print(df_customers.head(2))
print("\n" + "="*50 + "\n")


# ==========================================
# AUFGABE A: DER MERGE (LEFT JOIN)
# ==========================================
print("--- Lösung A: Daten verknüpfen (Merge) ---")

# Wir nutzen einen LEFT JOIN, um alle Bestellungen zu behalten,
# auch wenn der Kunde (wie ID 99) nicht in der Kundenliste ist.
df_full = pd.merge(
    df_orders, 
    df_customers, 
    left_on='Kunden_ID', 
    right_on='ID', 
    how='left'
)

# Optional: Die doppelte 'ID' Spalte (von customers) entfernen, da sie redundant ist
# df_full.drop(columns=['ID'], inplace=True)

print(df_full)
print("\n" + "="*50 + "\n")


# ==========================================
# AUFGABE B: ZEIT-ANALYSE
# ==========================================
print("--- Lösung B: Umsatz pro Monat ---")

# 1. In Datetime konvertieren
df_full['Datum'] = pd.to_datetime(df_full['Datum'])

# 2. Monatsnamen extrahieren (Erstellt neue Spalte 'Monat')
df_full['Monat'] = df_full['Datum'].dt.month_name()

# 3. Gruppieren und Summieren
monats_umsatz = df_full.groupby('Monat')['Betrag'].sum()

print(monats_umsatz)
print("\n" + "="*50 + "\n")


# ==========================================
# AUFGABE C: KOMPLEXE FILTERUNG (VIPs)
# ==========================================
print("--- Lösung C: VIP Filter (Gold ODER > 200€) ---")

# Bedingung 1: Status ist Gold
cond_gold = df_full['Status'] == 'Gold'

# Bedingung 2: Betrag größer 200
cond_high_value = df_full['Betrag'] > 200

# Verknüpfung mit ODER (|)
vip_df = df_full[cond_gold | cond_high_value]

# Wir zeigen nur relevante Spalten an, damit es übersichtlicher ist
cols_to_show = ['Order_ID', 'Name', 'Status', 'Betrag']
print(vip_df[cols_to_show])
print("\n" + "="*50 + "\n")


# ==========================================
# AUFGABE D: PIVOT TABELLE
# ==========================================
print("--- Lösung D: Pivot Tabelle (Land vs. Status) ---")

# Zeilen: Land, Spalten: Status, Werte: Betrag (Durchschnitt)
pivot = df_full.pivot_table(
    values='Betrag', 
    index='Land', 
    columns='Status', 
    aggfunc='mean'
)

# Füllt NaN Werte (falls eine Kombination nicht existiert) mit 0 oder '-' für schönere Optik
# pivot = pivot.fillna(0) 

print(pivot)
print("\n" + "="*50)