# PS. Trykk alt og z samtidig for å slippe å bla for å lese kommentarene!!!
# Løs likningen 5 ln(x^3 + 2) = 6 − x med halveringsmetoden.
import math

a = 0 # Startverdi intervall (Forandre verdi)
b = 1 # Sluttverdi intervall (Forandre verdi)
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return 5*math.log(x**3 + 2) + x - 6 # (Må forandres på etter hva oppgaven sier, dette er likningen)

# Halveringsmetoden:
m = (a + b)/2   # finner midtpunkt i opprinnelig intervall

while abs(f(m)) >= noyaktighet: # Så lenge absoluttverdien av f(m) er større eller lik noyaktighet, som er definert over, så kjøres koden under
  if f(a)*f(m) < 0: # Hvis f(a) * f(m) er mindre enn 0,
    b = m           #       Så er b lik m, altså de er det samme
  else:
    a = m           # Hvis det ikke stemmer så er a lik m
  
  m = (a + b)/2 # Her tar vi verdien av m og setter den lik (a + b) delt på 2
  
print("Løsningen på likningen er tilnærmet lik ", round(m, 4)) # Skriver ut løsningen (Forandre på 4, men i forhold til hvor mange desimaler som er ønsket)

# Output:
# Løsningen på likningen er tilnærmet lik  0.9146