# ============================================
#   Demo Template: Kontrollstrukturen in Python
# ============================================

print("=== Kontrollstrukturen Demo ===")

# -------- IF / ELIF / ELSE --------
zahl = 3  # Beispielwert

if zahl < 0:
    print("Zahl ist negativ")
elif zahl == 0:
    print("Zahl ist genau Null")
else:
    print("Zahl ist positiv")

# -------- MATCH / CASE (Python 3.10+) --------
farbe = "rot"

print("\nMatch/Case Beispiel:")
match farbe:
    case "rot":
        print("Farbe ist Rot")
    case "blau":
        print("Farbe ist Blau")
    case "grün":
        print("Farbe ist Grün")
    case _:
        print("Farbe unbekannt")

# -------- FOR-SCHLEIFE über Liste --------
liste = ["Apfel", "Banane", "Kirsche", "Khaki"]
print("\nFor-Schleife über Liste:")
for item in liste:
    print(f"- {item}")

# -------- BREAK & CONTINUE --------
print("\nDemo: break & continue")
for i in liste:
    if i == "Banane":
        continue   # überspringt Banane
    if i == "Kirsche":
        break      # stoppt die Schleife komplett
    print(i)

# -------- WHILE-SCHLEIFE --------
print("\nCountdown mit while:")
start = 5
while start > 0:
    print(start)
    start = start - 1 # Abbruchbedingung
print("Fertig!")
