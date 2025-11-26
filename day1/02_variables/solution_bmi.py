# Teil 1: Einfacher BMI-Rechner

# Eingaben vom Benutzer
name = input("Wie heißt du? ")
groesse = float(input("Wie groß bist du in Metern? (z.B. 1.78) "))
gewicht = float(input("Wie viel wiegst du in kg? "))

# BMI berechnen
bmi = gewicht / (groesse ** 2)

# Ergebnis ausgeben
print(f"\nHallo {name}!")
print(f"Dein BMI beträgt: {bmi:.2f}")





# Teil 2: Einordnung des BMI
if bmi < 18.5:
    print("Kategorie: Untergewicht")
elif 18.5 <= bmi < 25:
    print("Kategorie: Normalgewicht")
elif 25 <= bmi < 30:
    print("Kategorie: Übergewicht")
else:
    print("Kategorie: Adipositas")
