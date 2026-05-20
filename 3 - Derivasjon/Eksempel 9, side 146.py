from pylab import *

delta_x = 1E-8          # Definerer delta_x som 10^-8

def f(x):               # Definerer funksjonen
    return x**2 + 2*x   # Funksjonsuttrykket

def derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x # Formel for den deriverte

x_verdier = linspace(-5, 5, 100)    # Definerer x verdiene (-5 = startverdi, 5 = sluttverdi, 
# 100 antall repitisjoner (hvor mange pungt som legges inn (bestemmer hvor 'smooth' grafen er)))
y_verdier = f(x_verdier)            # Definerer y verdiene
dy_verdier = derivert(x_verdier)    # Definerer derivert y verdi? 

plot(x_verdier, y_verdier)          # Skriver inn graf
plot(x_verdier, dy_verdier)         # Skriver inn graf
show()                              # Viser grafene