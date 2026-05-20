# Oppgavetekst:
# Funksjonen f er gitt ved f(x) = 5e^-2x.

# a) - Lag et program som bruker Newtons kvotient til å finne f'(1) når delta_x = 10^-8
from pylab import *

delta_x = 1E-8
def f(x):
    return 5*exp(-2*x)
def derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x

print(derivert(1))
# Output:
# -1.3533528187004151

# Kan også skrives med math modulen:
import math

delta_x = 1E-8
def f(x):
    return 5*math.exp(-2*x)
def derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x

print(derivert(1))
# Output:
# -1.3533528187004151

# b) - Lag et program som bruker Newtons symmetriske kvotient til å finne f'(1) når delta_x = 10^-8
# Importerer verken math eller pylap siden det er importert tidligere
delta_x = 1E-8
def f(x):
    return 5*exp(-2*x)
def derivert(a):
    return (f(a + delta_x) - f(a - delta_x)) / (2*delta_x)

print(derivert(1))
# Output:
# -1.3533528298026454

delta_x = 1E-8
def f(x):
    return 5*math.exp(-2*x)
def derivert(a):
    return (f(a + delta_x) - f(a - delta_x)) / (2*delta_x)

print(derivert(1))
# Output:
# -1.3533528298026454

# c- gjøres i cas