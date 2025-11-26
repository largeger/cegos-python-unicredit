# -------------------------------------------
# Python Template: Listen, Dictionaries, Sets, Tupel & range
# -------------------------------------------

# 🧱 Liste (List) – veränderbar, geordnet, erlaubt Duplikate
fruechte = ["Apfel", "Banane", "Kirsche"]
fruechte.append("Orange")
fruechte.remove("Apfel")
# print("Bitte noch mehr Obst")
# fruechte.append(input())
print("Liste:", fruechte)


# 🔑 Dictionary – Schlüssel/Wert Paare, veränderbar, keine doppelten Schlüssel
person = {
    "name": "Lara",
    "alter": 28,
    "stadt": "Berlin"
}
person["alter"] = 29  # Wert ändern
print("Dictionary:", person)


# 🧺 Set – ungeordnet, keine Duplikate
tiere = {"Hund", "Katze", "Vogel"}
tiere.add("Fisch")
tiere.add("Katze")  # wird NICHT hinzugefügt (Duplikat)
print("Set:", tiere)


# 🎁 Tupel (Tuple) – geordnet, unveränderbar
farben = ("Rot", "Grün", "Blau")
# farben.append("Gelb")  # Fehler: Tupel sind unveränderbar
print("Tupel:", farben)


# 🔁 range – Zahlenfolge erzeugen
zahlen = list(range(1, 6))  # 1 bis 5
print("range:", zahlen)

# typische Schleife über range
for i in range(3):
    print("range Schleifenwert:", i)
