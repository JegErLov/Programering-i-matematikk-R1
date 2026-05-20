# Vi plotter rulletidene med en regresjonsmodell.

from pylab import *

lengde = array([20, 40, 60, 80, 100])
y_snitt = array([1.33, 2.06, 2.74, 3.26, 3.69])
SE = array([0.06, 0.07, 0.08, 0.04, 0.05])

# plotter blå prikker
plot(lengde, y_snitt, "b.")
# plotter røde vertikale linjer
vlines(lengde, y_snitt - 2*SE, y_snitt + 2*SE, "r")

xlabel("Lengde (cm)") # gir navn til x-aksen
ylabel("Tid (sekunder)") # gir navn til y-aksen

# Tre nye linjer fra side 332
x = linspace(10, 110, 100)
y = 0.195*x**0.6413
plot(x, y, "--") # vi får stiplet linje med "--"

show()