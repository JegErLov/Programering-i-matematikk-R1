# Oppgavetekst:
# Programmet laster inn data fra en ekstern fil og plotter dataene uten videre behandling. 
# PS. husk å laste ned og legge filen på samme plass som koden, og ikke i noe undermappe, 
# det liker ikke koden
# Finner ikke filen til hopen, derfor er det ikke murlig å kjøre denne koden, eller teste at alt 
# virker for å bruke koden på andre filer bytt ut hopen, og hopen.csv med riktig navn

from pylab import *

hopen = loadtxt("hopen.csv", delimiter = ";", skiprows = 1, usecols = (2,3))
aar = hopen[:, 0] # Antall år
temp = hopen[:, 1] # Temperatur

plot(aar, temp)                 # plotter dataene
xlabel("År")                    # gir navn til x-aksen
ylabel("Temperatur (grader C)") # gir navn til y-aksen
show()                          # Viser grafen