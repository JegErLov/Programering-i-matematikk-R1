# Oppgavetekst:
# Programmet laster inn data fra en ekstern fil og plotter dataene sammen med et glidende 
# gjennomsnitt.

from pylab import *

hopen = loadtxt("hopen.csv", skiprows = 1, usecols = (2,3))
aar = hopen[:, 0]
temp = hopen[:, 1]

plot(aar, temp)                 # plotter dataene
xlabel("År")                    # gir navn til x-aksen
ylabel("Temperatur (grader C)") # gir navn til y-aksen

# Nye linjer (fortsettelse på den forrige koden)
k = 7 # bruker glidende gjennomsnitt med k = 7
temp_glatt = [] # tom liste for de glattede temperaturene

# løkke som beregner de glattede verdiene
for i in range (k, len(temp) - k):
    temp_glatt.append(mean(temp[(i - k):(i + k)]))

# plotter de glattede verdiene, "k" gir sort linje
plot(aar[k:len(temp) - k], temp_glatt, "k")

show()