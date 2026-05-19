def g(x): # Definerer g(x)
    return (x**2 - 9) / (x - 3) # Returnerer brøken

delta_x = 0.1       # Definerer delta_x, og setter verdien til 0,1
print("x", "\t", "\t", "g(x)") # \t betyr tab
for i in range(4):          # gjentar 4 ganger
    x = 3 + delta_x         # ny x-verdi
    y = round(g(x), 4)      # ny y-verdi, avrundet
    print(x, "\t", "\t", y)
    delta_x = delta_x * 0.1 # ny verdi for delta_x

# Output
# x                g(x)
# 3.1              6.1
# 3.01             6.01
# 3.001            6.001
# 3.0001           6.0001