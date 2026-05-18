from pylab import *
# Once more with halveringsmetoden (eksempel 26)
a = 0.0 # Startverdi intervall
b = 1.0 # Sluttverdi intervall
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return 13500 * 1.025**x - 15000 # (Må forandres på etter hva oppgaven sier, dette er likningen)

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
# Løsningen på likningen er tilnærmet lik  4.2669