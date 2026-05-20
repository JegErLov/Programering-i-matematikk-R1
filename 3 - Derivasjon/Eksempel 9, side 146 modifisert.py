import matplotlib.pyplot as plt
import numpy as np

delta_x =1E-8           # Definerer delta_x som 10^-8
def f(x):               # Funksjonen 
    return x**2 + 2*x   # Funksjonsuttrykk

def derivert(a):        # Derivisjon med formel
    return (f(a + delta_x)-f(a))/delta_x

x_verdier = np.linspace(-5,5,100)   # definerer x verdier
y_verdier = f(x_verdier)            # definerer y verdier
dy_verdier = derivert(x_verdier)    # definerer derivert y verdier

plt.plot(x_verdier, y_verdier)      # Skriver inn graf 1 
plt.plot(x_verdier, dy_verdier)     # Skriver inn graf 2
plt.show()                          # Viser grafene


# Samme kode, men med flere ting som labels:
delta_x = 1E-8

def f(x):
    return x**2 + 2*x

def derivert(a):
    return (f(a + delta_x) - f(a)) / (delta_x)

x_verdier = np.linspace(-5, 5, 100)
y_verdier = f(x_verdier)
dy_verdier = derivert(x_verdier)

plt.plot(x_verdier, y_verdier, label = "f(x)")
plt.plot(x_verdier, dy_verdier, label = "f'(x)")
# Alt over er likt
plt.xlabel("x")         # Lager en label til grafen, der står det 'x'
plt.ylabel("f(x)")      # lager en label til grafen, der står det 'f(x)'
plt.legend()            # Skriver lablene
plt.show()              # Viser