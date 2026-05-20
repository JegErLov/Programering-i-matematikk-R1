# Oppgavetekst:                    _____
# Funksjonen f er gitt ved f(x) = V ln x-
# a) - Lag et program som finner f'(3) på to ulike måter
from pylab import *
delta_x = 1E-8
def f(x):
    return sqrt(log(x));

def derivert(a): #Den deriverte med Newtons kvotient
    return (f(a + delta_x) - f(a)) / delta_x

def derivert_sym(a): #Den deriverte med Newtons symmetriske kvotient
    return (f(a + delta_x) - f(a - delta_x)) / (2*delta_x)

print("f'(3) med Newtons kvotient: ", derivert(3))
print("f'(3) med Newtons symmetriske kvotient: ", derivert_sym(3))

# Output:
# f'(3) med Newtons kvotient: 0.15901073791013687
# f'(3) med Newtons symmetriske kvotient: 0.15901076011459736

# Oppgave b er i cas
# c) - Utvid programmet i oppgave a slik at det også tegner grafen til f og f'. Kommenter
from pylab import *
delta_x = 1E-8
def f(x):
    return sqrt(log(x))

def derivert(a):
 return (f(a + delta_x) - f(a)) / delta_x

def derivert_sym(a):
 return (f(a + delta_x) - f(a - delta_x)) / (2*delta_x)

print("f'(3) med Newtons kvotient: ", derivert(3))
print("f'(3) med Newtons symmetriske kvotient: ", derivert_sym(3))
x_verdier = linspace(2, 10, 100)
y_verdier = f(x_verdier)
dy_verdier = derivert_sym(x_verdier)
plot(x_verdier, y_verdier)
plot(x_verdier, dy_verdier)
show()

# Den oransje grafen tilhører f′, siden den viser hvordan den blå grafen alltid stiger (f′(x) > 0)
# og samtidig sakte avtar mot 0. Vi vet at f(x) er definert for x > 1, siden ln x da ikke er negativ.
# Det vi må passe på er at Newtons symmetriske kvotient beregner f(x - ∆x), og da kan ikke x = 1.
# Vi valgte derfor x-verdier i intervallet [2 , 10] da vi tegnet grafene. 