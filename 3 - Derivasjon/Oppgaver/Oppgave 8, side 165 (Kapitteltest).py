# Oppgavetekst:
# Nedenfor ser du et program og utskriften til programmet. Hva gjør programmet? 
# Kommenter utskriften.

from pylab import *

def f(x):
    return log(x)

def derivert1(a, delta_x):
    return (f(a + delta_x) - f(a)) / delta_x

def derivert2(a, delta_x):
    return (f(a + delta_x) - f(a - delta_x)) / (2*delta_x)

print(derivert1(1, 1E-8))
print(derivert2(1, 1E-8))

# Output:
# 0.9999999889225291
# 0.9999999994736442