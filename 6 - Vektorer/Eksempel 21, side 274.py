# Oppgavetekst:
# Lag et program som avgjør om to vektorer er ortogonale. Hvis de ikke er ortogonale, skal
# programmet fortelle om vinkelen mellom dem er spiss eller stump.

# Programmet i boka bruker funksjonen input for å skrive inn verdien til vektorkoordinatene. 
# Her endrer vi verdiene rett i programmet.
# Legger derfor med den med input funksjonen.
# -------------------------------------------------------------------

# Skriv inn koordinatene til vektoren u = [x1, y1]
x1 = 0 # Her kan du endre 1. koordinaten til den ene vektoren
y1 = 1 # Her kan du endre 2. koordinaten til den ene vektoren

# Skriv inn koordinatene til vektoren v = [x2, y2]
x2 = 0 # Her kan du endre 1. koordinaten til den andre vektoren
y2 = 2 # Her kan du endre 2. koordinaten til den andre vektoren

skalarprodukt = x1*x2 + y1*y2   # Formel for skalarproduktet

if skalarprodukt == 0:       # Hvis skalarproduktet er 0 så er den ortogonal
    print("Vektorne er ortogonale.")
elif skalarprodukt > 0:      # Hvis skalarproduktet er større enn 0 så er det en spiss vinkel
    print("Vinklen mellom vektorne er spiss.")
else:     # Hvis skalarproduktet ikke inngår i noen av de før så er det en stump vinkel
    print("Vinklen mellom vektorne er stump.")

# Med input funksjonen

print("Skriv inn koordinatene til vektoren u = [x1, y1]") # Henter koordinatene til x1, og y1
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Skriv inn koordinatene til vektoren u = [x2, y2]") # Henter koordinatene til x2, og y2
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

skalarprodukt = x1 * x2 + y1 * y2   # Formel for skalarproduktet

if skalarprodukt == 0: # Hvis skalarproduktet er 0 så er den ortogonal
    print("Vektorne er ortogonale.")
elif skalarprodukt > 0: # Hvis skalarproduktet er større enn 0 så er det en spiss vinkel
    print("Vinklen mellom vektorne er spiss.")
else: # Hvis skalarproduktet ikke inngår i noen av de før så er det en stump vinkel
    print("Vinklen mellom vektorne er stump.")