# Oppgave a og c kan gjøres i GeoGebra, og er derfor ikke med her
# Vi bruker verdiene som vi fikk fra a som start og slutt verdi

# Oppgave b:
# Igjen modifisert kode fra eksempel 26
# Punkt A
a = -1.0 # Startverdi intervall
b = 0.0 # Sluttverdi intervall
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return 0.5*x**3 - 2*x**2 + 1 # (Må forandres på etter hva oppgaven sier, dette er likningen)

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
# Løsningen på likningen er tilnærmet lik  -0.6554

# Punkt B
a = 0.0 # Startverdi intervall
b = 1.0 # Sluttverdi intervall
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return 0.5*x**3 - 2*x**2 + 1 # (Må forandres på etter hva oppgaven sier, dette er likningen)

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
# Løsningen på likningen er tilnærmet lik  0.7892

# Punkt C
a = 3.0 # Startverdi intervall
b = 4.0 # Sluttverdi intervall
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være (kan forandres, men kommer ann på oppgaven)

def f(x): # definerer funksjonen
  return 0.5*x**3 - 2*x**2 + 1 # (Må forandres på etter hva oppgaven sier, dette er likningen)

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
# Løsningen på likningen er tilnærmet lik  3.8662

#   L = {–0,655 , 0,789 , 3,866}