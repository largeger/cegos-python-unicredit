import pandas as pd


# Verkäufe Januar
verkaeufe_jan = pd.DataFrame({
'Bestell-ID': [1, 2, 3],
'Produkt': ['Laptop', 'Maus', 'Monitor'],
'Menge': [1, 2, 1],
'Preis': [1200, 25, 300]
})
verkaeufe_jan.to_excel('verkaeufe_jan.xlsx', index=False)


# Verkäufe Februar
verkaeufe_feb = pd.DataFrame({
'Bestell-ID': [4, 5, 6],
'Produkt': ['Tastatur', 'Maus', 'Laptop'],
'Menge': [3, 5, 1],
'Preis': [45, 25, 1200]
})
verkaeufe_feb.to_excel('verkaeufe_feb.xlsx', index=False)


# Kunden Januar
kunden_jan = pd.DataFrame({
'Bestell-ID': [1, 2, 3],
'Kunde': ['Alice', 'Bob', 'Charlie'],
'Stadt': ['Berlin', 'München', 'Hamburg'],
'Treueprogramm': ['Ja', 'Nein', 'Ja']
})
kunden_jan.to_excel('kunden_jan.xlsx', index=False)


# Kunden Februar
kunden_feb = pd.DataFrame({
'Bestell-ID': [4, 5, 6],
'Kunde': ['David', 'Eva', 'Frank'],
'Stadt': ['Berlin', 'München', 'Hamburg'],
'Treueprogramm': ['Nein', 'Ja', 'Nein']
})
kunden_feb.to_excel('kunden_feb.xlsx', index=False)