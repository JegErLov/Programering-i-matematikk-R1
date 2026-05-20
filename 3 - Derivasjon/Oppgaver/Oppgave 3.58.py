# Oppgavetekst:
# Funksjonen f er gitt ved f(x)=x^2.
# Lag et program som bruker Newtons symmetriske kvotient til å finne den deriverte i 
# punktet -1 når delta_x = 10^-8

def f(x):           # Definerer funksjonen
    return x**2     # Funksjonsuttrykket

def derivert(a, delta_x):
    return (f(a + delta_x) - f(a - delta_x))/(2*delta_x) # Formelen til Newtons symmetriske kvotient

print(derivert(-1, 1E-8)) # Skriver ut koden, med punktet -1 (a) og 1E-8 (delta_x)