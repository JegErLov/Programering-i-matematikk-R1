# Oppgavebeskrivelse, og oppgave:
# Funksjonen f er gitt ved f(x)=2x^2 + x-5.
# a) Lag et program som finner f'(1) når delta_x = 10^-8. 
# b) Sammenlign verdien for f'(1) i oppgave a med den eksakte verdien du får ved regning

# a)

def f(x):                                       # Funksjonen vi vil derivere
    return 2*x**2 + x-5                         # Funksjonen (må byttes)

def derivert(f, a, delta_x):                    # Numerisk derivasjon i a
    return (f(a + delta_x) - f(a)) / delta_x    # Formel for numerisk derivisjon

print("f'(1) =", derivert(f, 1, 1E-8))         # Det i innerste parantes (tallene) må kanskje byttes
# Verdiene:          (funksjon, a, delta_x)

# Output:
# f'(1) = 4.999999969612645

# b)
# Hvis vi bruker regneregler, så får vi f'(x)=4x+1 som gir f'(1) = 5