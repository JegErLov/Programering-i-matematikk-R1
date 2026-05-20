# a) - Skriv av, og kjør programmet i eksempel 9
from pylab import *

delta_x = 1E-8
def f(x):
    return x**2 + 2*x

def derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x

x_verdier = linspace(-5, 5, 100)
y_verdier = f(x_verdier)
dy_verdier = derivert(x_verdier) 
plot(x_verdier, y_verdier)
plot(x_verdier, dy_verdier)
show()

# b) - Hvilken av grafene i eksempel 9 er grafen til f', og hvilken er grafen til f?
# Den blåe grafen er f(x), og den orange grafen er f'(x)

# c) - Forklar hva de ulike delene av programmet gjør (se under)
# d) - Endre programmet slik at det bare skriver ut grafen til f'.

#from pylab import *    # Importerer modulen (ER ikke behov for det flere ganger, 
# derfor er den kommentert ut)

delta_x = 1E-8          # Definerer delta_x som 10^-8

def f(x):               # Definerer funksjonen
    return x**2 + 2*x   # Funksjonsuttrykket

def derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x # Formel for den deriverte

x_verdier = linspace(-5, 5, 100)    # Definerer x verdiene
y_verdier = f(x_verdier)            # Definerer y verdiene
dy_verdier = derivert(x_verdier)    # Definerer derivert y verdi

# plot(x_verdier, y_verdier)        # Ta vekk denne linjen (har kommentertert den ut)
plot(x_verdier, dy_verdier)         # Skriver inn graf, linjen over gjør det samme
show()                              # Viser grafene