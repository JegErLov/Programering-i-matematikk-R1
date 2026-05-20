# Oppgavetekst:                                       _______
# Funksjonene u og v er gitt ved u(x)=x^2-3x og v(x)=V lnx +x.
# a) - Lag et program som finner u'(7) og v'(7), og som skriver ut u'(7)*v(7)+u(7)*v'(7).
#      Funksjonen f er gitt ved f(x) = u(x)*v(x)

from pylab import *
delta_x = 1E-8
def u(x):
    return x**2 - 3*x

def v(x):
    return sqrt(log(x) + x)

def derivert(g, a):
    return (g(a + delta_x) - g(a - delta_x)) / (2*delta_x)

print("u'v + uv' =" , derivert(u, 7)*v(7) + u(7)*derivert(v, 7))

# Output:
# u'v + uv' = 38.25011763858166

# b) - Utvid programmet i oppgave a slik at det også skriver ut f'(7).
#      Kommenter utskriften.

from pylab import *
delta_x = 1E-8
def u(x):
    return x**2 - 3*x

def v(x):
    return sqrt(log(x) + x)

def f(x):
    return u(x)*v(x)

def derivert(g, a):
    return (g(a + delta_x) - g(a - delta_x)) / (2*delta_x)

print("f' =", derivert(f, 7))
print("u'v + uv' =", derivert(u, 7)*v(7) + u(7)*derivert(v, 7))

# Komentar til programmet (kriterie i oppgave):
# Utskriften viser, ikke uventet, at vi får samme resultat når vi deriverer funksjonen numerisk 
# direkte, og når vi bruker produktregelen.

# Output:
# (uv)' = 38.25011773983533
# u'v + uv' = 38.25011763858166