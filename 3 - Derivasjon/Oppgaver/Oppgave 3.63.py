# Oppgavetekst:
# a) - Lag et kjørbart dataprogram ned utgangspungt i pseudokoden nedenfor
"""
Definer funksjonen f
    Hvis x < 1 f(x) = x^2-2
    Ellers er f(x) = -x^2
Definer en funksjon som deriverer
Lag en liste x_verdier med 400 x_verdier jevnt fordelt i intervallet[-5,5]
Lag en tom liste dy_verdier
For hver x i x_verdier, fra og med den første til og med den siste
    Legg inn derivert(x) i dy_verdier
Tegn grafen til dy_verdier som funksjon av x_verdier
"""
from pylab import *

def f(x):
    if x < 1:
        return x**2-2
    else:
        return -x**2

def derivert(a):
    return (f(a + 1E-8) - f(a)) / 1E-8

x_verdier = linspace(-5, 5, 400) 
dy_verdier = []

for a in x_verdier:
    dy_verdier.append(derivert(a))

plot(x_verdier, dy_verdier)
show()

# b) - Forklar hva programmet gjør
# Pseudokoden forklarer ganske greit, men for å ta det kort, så improteret vi alt fra pylab modulen,
# også definerer vi f(x) og formelen for den deriverte. i stedet for å skrive delta_x = 1E-8 så 
# skriver vi i dette programmet 1E-8 hver gang det er snakk om delta_x i formelen. Dette er på 
# grunn av at pseudokoden ikke sa at vi skulle definere en variabel for delta_x. Videre legger vi 
# inn verdiene til x, også sier vi at deriverte y_verdier skal legges inn i listen for hver x verdi 
# etter dette skriver vi ut grafen.