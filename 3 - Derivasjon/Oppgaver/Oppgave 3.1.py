# Oppgavetekst:
# Programmet nedenfor regner ut den gjennomsnittlige vekstfarten i et intervall for en funksjon.

# a, b
# a - Skriv av og kjør programmet. b - Forkalr hva de ulike delene av progeammet gjør.
def f(x):                               # Definerer funksjonen f(x)
    return 0.06*x**2 + 4*x - 7          # Denne linjen returnerer selve funksjonen

def snittfart(f, x1, x2):               # Definerer snittfarten og henter inn verdiene for x1 og x2
    return (f(x2) - f(x1)) / (x2 - x1)  # Returnerer formelen (formelen er i kapittel 3a på side 116)

snitt = round(snittfart(f, -1, 3), 2)   # Definerer variabelen med verdiene for x1 og x2, og i 
# tillegg sier vi at vi skal bruke funksjonen f(x) som vi definerte tidligere også sier at det 
# skal være 2 desimaler i svaret.
print("Gjennomsnittlig vekstfart i intervallet [-1, 3] er", snitt) # Skriver ut svaret
# Output:
# Gjennomsnittlig vekstfart i intervallet [-1, 3] er 4.12

# c
# Endre programmet slik at det regner ut gjennomsnittlig vekstfart i intervallet [-6,0] 
# for funksjonen g gitt ved g(x) = 2x^3.
def g(x):
    return 2*x**3

def snittfart(f, x1, x2):
    return (f(x2) - f(x1)) / (x2 - x1)

snitt = round(snittfart(g, -6, 0), 2)

print("Gjennomsnittlig vekstfart i intervallet [-6, 0] er", snitt)
# Output:
# Gjennomsnittlig vekstfart i intervallet [-6, 0] er 72.0

# d
# Endre programmet slik at du selv kan velge intervall når du kjører programmet. 
# Intervallet du har valgt, skal også stå i utskriften.


print("Du skal velge intervallet under")
x1 = float(input("Skriv in x1 (intervall fra): "))
x2 = float(input("Skriv in x2 (intervall til): "))

def f(x):
    return 0.06*x**2 + 4*x - 7 

def snittfart(f, x1, x2):
    return (f(x2) - f(x1)) / (x2 - x1)

snitt = round(snittfart(f, x1, x2), 2)
print("Gjennomsnittlig vekstfart i intervallet [" , x1 , "," , x2 , "] er", snitt)