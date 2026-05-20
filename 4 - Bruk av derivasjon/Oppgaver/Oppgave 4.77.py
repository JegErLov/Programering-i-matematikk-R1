# Oppgavetekst:
# Programmet nedenfor bruker numerisk andrederivasjon til å finne infleksjonspunkter. 
# a) - Kjør programmet for noen ulike intervaller [x0 , x1]. Sammenlikn med resultatet du får ved 
# å regne eksakt. 
# b) - Undersøk om programmet gir ønsket resultat for funksjonen f gitt ved 
# f(x) = x4 + 12x3 + 30x2 + x. Programmet i boka bruker funksjonen input for å skrive inn verdien 
# til radiene x0 og x1. Her endrer vi verdiene rett i programmet.

h = 1E-3
# Skriv inn tall for å angi intervallet programmet sjekker 
x0 = 0 # Her kan du endre starten på intervallet
x1 = 5 # Her kan du endre slutten på intervallet

def f(x):
    return x**3 + x**2 + x + 1  # Funksjon
  
def andrederivert(a , h):
    return 1/h**2 * (f(a+h) - 2*f(a) + f(a-h)) # Formel for andrederivert

x = x0 # Setter x0 til det samme som x
while True:
    p = andrederivert(x , h)
    q = andrederivert(x + h , h)
    if p*q <= 0:
        print(round(x + h/2 , 2) , "er et infleksjonspunkt.") # rount(tall/formel , desimaler)
        break
    elif x >= x1:
        print("f har ikke infleksjonspunkt i intervallet [",x0,",",x1,"].")
        break
    x = x + h

