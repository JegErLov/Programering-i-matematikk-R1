# Oppgave 1.108 d skal løses med halveringsmetoden (Eksempel 26)
from pylab import * # Trenger ikke å importere flere ganger
# Husk alt+z for å se alt av kommentarer uten å bla

# 1)
a = 0.5 # Startverdi intervall **** Kan ikke være a = 0 (Vet ikke hvorfor)
b = 1.5 # Sluttverdi intervall
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return log10(x**2) + log10(x) # (Må forandres på etter hva oppgaven sier, dette er likningen)

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
# Løsningen på likningen er tilnærmet lik  1.0

# 2)
a = -3.0 # Startverdi intervall
b = -1.5 # Sluttverdi intervall
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return 10**(x+5) - 1000 # (Må forandres på etter hva oppgaven sier, dette er likningen)

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
# Løsningen på likningen er tilnærmet lik  -2.0

# 3)
a = -2.0 # Startverdi intervall
b = 0.0 # Sluttverdi intervall    **** Vi kan ikke bruke b = 2 (vet ikke hvorfor)
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return log10(x**2) + log10(x) # (Må forandres på etter hva oppgaven sier, dette er likningen)

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
# Løsningen på likningen er tilnærmet lik  1.0