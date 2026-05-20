# Oppgavetekst:
# Funksjonen f er gitt ved f(x) = 3x2 − 10 − e−x.
# Lag et program som ved hjelp av Newtons metode finner en tilnærmet verdi for nullpunktet med fire 
# desimalers nøyaktighet. Programmet i boka bruker funksjonen input for å skrive inn verdien til 
# startverdien x1. Her endrer vi verdiene rett i programmet

from pylab import *

def f(x):
    return 3*x**2 - 10 - e**(-x)    # Funksjon

x = linspace(-5, 7, 1000)           # Fra hvor, til hvor og hvor mange pungt grafens skal innom
y = f(x)                            # Graf

plot(x, y, color = "b")             # Skriver inn x og y i fargen 'b' (Dette er navn på aksene)
ylim(-20, 40)                       # Sier hvor navnene er 
axhline(y = 0, color = "k")         # Mer om aksene (h - horisontal)
axvline(x = 0, color = "k")         # Mer om aksene (v - vertical)
xlabel("x")                         # Selv forklarende
ylabel("y")                         # Selv forklarende
grid()                              # Lager en grid, sånn at det er lettere å se koordinatsystemet
show()                              # Viser grafen og alt vi har laget tidligere

# Skriv inn et tall som startverdi for Newtons metode 
x1 = 1 # Her kan du endre verdien på startverdien

delta_x = 0.00001

def f_derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x    # Formel for derivert

def ny_x_verdi(x1):
    return x1 - (f(x1) / f_derivert(x1))        # Gir en ny x verdi ved hjelp av f derivert

for i in range(10):                                         # For hver verdi til 9 skal dette kjøre
    x2 = ny_x_verdi(x1)                                     # Setter forrige funksjon til x2
    print("Et bedre forslag er gitt ved x =", round(x2, 4))
    x1 = x2                                                 # Sier at x1 og x2 er det samme

print("Med x =", x1, " er f(x) =", f(x1))