from pylab import *

y = array([3.73, 3.53, 3.75, 3.63, 3.82])   # Inndataa
n = len(y)                                  # Antall data
y_snitt = sum(y) / n                        # Gjennomsnitt
s = sqrt(sum((y - y_snitt)**2) / (n - 1))   # Standaravvik

print("Gjennomsnittet er:", round(y_snitt, 2)) # (Gjennomsnitt, antall desimaler her 2)
print("Standaravviket er:", round(s, 2)) # (Standaravvik, antall desimaler her 2)

# Output:
# Gjennomsnittet er: 3.69
# Standaravviket er: 0.11