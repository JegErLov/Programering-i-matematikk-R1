# I denne oppgaven så ligger både a og b
# PS. Trykk alt og z samtidig for å slippe å bla for å lese kommentarene!!!
import math

# Oppgave a
# Denne delen av oppgaven bruker koden fra eksempel 26

a = 1.0 # Startverdi intervall
b = 2.0 # Sluttverdi intervall
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return math.log10(x + 2) - 2 + x # (Må forandres på etter hva oppgaven sier, dette er likningen)

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
# Løsningen på likningen er tilnærmet lik  1.4608

# Oppgave b
a = 4.0 # Startverdi intervall
b = 5.0 # Sluttverdi intervall
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return 350*1.2**x - 756 # (Må forandres på etter hva oppgaven sier, dette er likningen)

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
# Løsningen på likningen er tilnærmet lik  4.2239