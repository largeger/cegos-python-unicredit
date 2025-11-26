# BMI Test
name = input("Wie heisst Du?")
gewicht = float(input("Wie viel wiegst Du?"))
groesse = float(input("Wie gross bist Du? Bitte in Metern eingeben"))
bmi = gewicht / groesse**2
print("Dein BMI ist: ", bmi)