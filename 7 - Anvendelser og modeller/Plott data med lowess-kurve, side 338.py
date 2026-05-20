# Oppgavetekst:
# Programmet laster inn data fra en ekstern fil og plotter dataene sammen med en lowess-kurve. 

from pylab import *
# import statsmodels.api as sm # lowess-kommando (Ikke ferdiginstallert)


hopen = loadtxt("hopen.csv", delimiter = ";", skiprows = 1, usecols = (2,3))
aar = hopen[:, 0]
temp = hopen[:, 1]

plot(aar, temp)                 # plotter dataene
xlabel("År")                    # gir navn til x-aksen
ylabel("Temperatur (grader C)") # gir navn til y-aksen

# Nye linjer
# lowess = sm.nonparametric.lowess (Bruker ikke)

# Erstatter lowles uten å importere noe mer
koeffisienter = polyfit(aar, temp, 5)
polynom_funksjon = poly1d(koeffisienter)
z = polynom_funksjon(aar)

# vi beregner de glattede temperaturene
# z = lowess(temp, aar, frac = 0.2, return_sorted = False) (Følger med lowless)

# vi plotter de glattede verdiene, "r" gir rød kurve 
plot(aar, z, "r")

show()

# Sikkert godt nokk forklart, se eventuelt de andre plot data filene