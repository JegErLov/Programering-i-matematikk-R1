# Kode for gjennomsnittlig vekstfart med og uten brukerinput (Bruker skriver inn verdier)

# Vanlig
def f(x):
    return 2*x**3                       # Forandre på funksjonen

def snittfart(f, x1, x2):               # Ikke rør denne
    return (f(x2) - f(x1)) / (x2 - x1)

snitt = round(snittfart(f, -6, 0), 2)   # Forandre på tallene, her står -6 som startvedi,
# og 0 som sluttverdi, 2 tallet er anntal desimaler

print("Gjennomsnittlig vekstfart i intervallet [-6, 0] er", snitt)  # Forandre på det som er i [] 
                                                                    # sånn at det er riktige tall

# Med
print("Du skal velge intervallet under")            # Ikke nødvendig å ha med
x1 = float(input("Skriv in x1 (intervall fra): "))  # Kan forandre på det som står som tekst
x2 = float(input("Skriv in x2 (intervall til): "))  # Kan forandre på det som står som tekst

def f(x):
    return 0.06*x**2 + 4*x - 7                      # Forandre til riktig funksjon

def snittfart(f, x1, x2):
    return (f(x2) - f(x1)) / (x2 - x1)

snitt = round(snittfart(f, x1, x2), 2)              # Ikke forandre noe i den innerste parantesen,
# kan forandre på 2 tallet for å få en annen mengde
print("Gjennomsnittlig vekstfart i intervallet [" , x1 , "," , x2 , "] er", snitt)