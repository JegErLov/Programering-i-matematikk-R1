# Oppgavetekst:
# Funksjonen f er gitt ved f(x) = -3x^3 + 4x^2 - 5x + 10

# a) - Lag et program som tegner grafen til f'.
from pylab import *

delta_x = 1E-8

def f(x):
    return -3*x**3 + 4*x**2 - 5*x + 10 # Funksjon

def derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x # formel

x_verdier = linspace(-5, 5, 100) # definerer aksene
dy_verdier = derivert(x_verdier) # Definerer den deriverte

plot(x_verdier, dy_verdier) # Skriver inn grafen
show() # viser grafen
# Viser den deriverte funksjonen til grafen

# b) - blir gjort på papir
# c) - Utvid programmet i oppgave a slik at det også tegner grafen til uttrykket du fant 
# i oppgave b. Kommenter
# Utvidet program, har ikke importert pylab to ganger

delta_x = 1E-8
def f(x):
 return -3*x**3 + 4*x**2 - 5*x + 10

def derivert(a):
 return (f(a + delta_x) - f(a)) / delta_x

def derivert_eksakt(x):
 return -9*x**2 + 8*x - 5

x_verdier = linspace(-5, 5, 100)
dy_verdier = derivert(x_verdier)
dy_eksakte_verdier = derivert_eksakt(x_verdier)
plot(x_verdier, dy_verdier)
plot(x_verdier, dy_eksakte_verdier)
show()

# Vi ser bare èn graf, som betyr at de to grafene som er tegnet, er sammenfallende. 
# Det betyr at tilnærmingen til den deriverte som vi fant ved hjelp av Newtons kvotient, 
# er svært god.