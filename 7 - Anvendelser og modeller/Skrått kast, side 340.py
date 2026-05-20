# Oppgavetekst:
# Programmer leser inn en tekstfil med data generert fra Tracker og plotter dem. 

from pylab import *

data = loadtxt("skraattkast.txt")   # Henter datafil
t = data[:, 0]                      # Henter ut data fra filen
x = data[:, 1]                      # Henter ut data fra filen
n = len(t)                          # Henter ut antallet fra t
fart = zeros(n)                     # Setter farten til null og det er n antall nuller

for i in range(0, n-1):             # For hver verdi fra 0 til ett tall mindre enn n
    fart[i] = (x[i+1] - x[i]) / (t[i+1] - t[i])     # Formel og uthenting av data

plot(t[0:n-1], fart[0:n-1])         # Skriver inn i graf
xlabel("Tid (s)")                   # Navngir x aksen
ylabel("Fart i x-retning (m/s)")    # Navngir y aksen
grid()                              # Lager en grid
show()                              # Viser alt