# Oppgavetekst:
# Siri har laget programmet nedenfor.
from pylab import * 

delta_x = 1E-8

def f(x):
    return x**x

def fderivert(a):
    return (f(a + delta_x) - f(a)) / delta_x

x_verdier = linspace(0, 20, 1000)
derivert_verdier = fderivert(x_verdier)

for i in range(0, 999):
    if derivert_verdier[i] * derivert_verdier[i+1] <= 0:
        ekstremalpungt = 1/2 * (x_verdier[i] + x_verdier[i+1])
        print("Ekstremalpunktet er ", ekstremalpungt)

# Output:
# Ekstremalpunktet er  0.37037037037037035