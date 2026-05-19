import math
def g(x):
    return (math.exp(x) - 1) / x
delta_x = 0.1
print("x", "\t", "\t", "g(x)")
for i in range(4): # gjentar 4 ganger
    x = 0 + delta_x # ny x-verdi
    y = round(g(x), 4) # ny y-verdi, avrundet
    print(x, "\t", "\t", y)
    delta_x = delta_x * 0.1 # ny verdi for delta_x

# Utskriften ser slik ut:
# x         g(x)
# 0.1       1.0157
# 0.01      1.005
# 0.001     1.0005
# 0.0001    1.0001