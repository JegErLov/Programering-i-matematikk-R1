# Kapittel 3C Den algebraiske definisjonen av den deriverte side 131

# Oppgavetekst:
# Forklar programmet nedenfor.

def f(x):
    return (x - 1)/(x + 2)

def snittfart(f, x, delta_x):
    return (f(x + delta_x) - f(x)) / delta_x

print(snittfart(f, 3, 1E-8))

# Forklaring fra løsningsforsklaget med modifikasjoner:

# I programmet defineres f(x)= (x - 1) / (x + 2, dette skjer på linje 1 og 2
# På linje 4 og 5 defineres en funksjon som regner ut den gjennomsnittlige vekstfarten til en
# funksjon f i intervallet [x , x + delta_x]. Vi ser da at lengden av intervallet er delta_x, 
# som blir divisoren i linje 5.
# På linje 7 beregnes og skrives ut den gjennomsnittlige vekstfarten til f i intervallet
# [3, 3 + 10^-8], dette skjer siden 1E-8 betegner 1 * 10^-8

# Output (ikke viktig for denne oppgaven, men kjekt å ha):
# 0.11999999882661427