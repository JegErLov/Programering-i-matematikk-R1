# Kodesnuttene i boka har ingen utskrift, de viser kommandoene vi bruker når vi skal laste inn data
# fra en ekstern fil. I de påfølgende kodesnuttene behandler vi dataene på ulike måter. 

from pylab import *

# Leser inn de to siste kolonnene av datafilen
hopen = loadtxt("hopen.csv", delimiter = ";", skiprows = 1, usecols=(2, 3)) 

# Trekker ut kolonnen med årstall
aar = hopen[:, 0]

# Trekker ut kolonnen med temperaturer
temp = hopen[:, 1]

print("Nå er dataene lastet inn. Gå til neste eksempelkode for å arbeide videre med dataene.")