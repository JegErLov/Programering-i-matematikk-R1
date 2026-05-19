def f(x):                           # Definerer funksjonen f(x)
  return 3*(x**2 - 4) / (x - 2)     # Returnerer brøken

delta_x = 0.1         # Definerer delta_x, og setter veriden til 0,1
print("x", "\t", "\t", "f(x)") # \t betyr bare at tab
for i in range(4):        # gjentar 4 ganger
  x = 2 + delta_x         # ny x-verdi
  y = round(f(x),4)       # ny y-verdi, avrundet
  print(x, "\t", "\t", y)
  delta_x = delta_x * 0.1 # ny verdi for delta_x

# Output:
# x                f(x)
# 2.1              12.3
# 2.01             12.03
# 2.001            12.003
# 2.0001           12.0003