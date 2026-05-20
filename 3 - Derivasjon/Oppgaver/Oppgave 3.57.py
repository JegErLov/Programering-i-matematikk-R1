# Oppgavetekst:
# funksjonen f er gitt ved f(x)=x^3 + 2x - 7.

# a) - Lag et program som finner f'(2) når delta_x = 10^-8

def f(x):
    return x**3 + 2*x - 7

def derivert(f, a, delta_x):                # Trenger ikke å ha med f som parameter, en parameter er
    return (f(a + delta_x) - f(a)) / delta_x       # det inni parantesen hvor man skriver def

print("f'(2) =", derivert(f, 2, 1E-8))      # Hvis man tar bort f fra parameteren, så må man ta 
                                            # f bort her óg

# Output:
# f'(2) = 13.999999914915406

# b) - Endre programmet i oppgave a slik at delta_x = 10^-1, og delta_x = 10^-15
# 1- delta_x = 10^-1
def f(x):
    return x**3 + 2*x - 7

def derivert(f, a, delta_x):
    return (f(a + delta_x) - f(a)) / delta_x 

print("f'(2) =", derivert(f, 2, 1E-1)) # Endret til 1E-1
# Output:
# f'(2) = 14.61000000000002

# 2- delta_x = 10^-15
def f(x):
    return x**3 + 2*x - 7

def derivert(f, a, delta_x):
    return (f(a + delta_x) - f(a)) / delta_x 

print("f'(2) =", derivert(f, 2, 1E-15)) # Endret til 1E-15
# Output:
# f'(2) = 12.434497875801751

# c) - For hver verdi av delta_x ligger den numeriske verdien for den deriverte nærmest den 
# ekskte verdien du finner ved regning?

# Vi finner først den eksakte verdien av f′(2).
# f(x) = x^3 + 2x - 7
# f'(x) = 3x^2 + 2*1-0 = 3x^2 + 2
# f'(2) = 3*2^2 + 2 = 14
# Vi ser at kjøringen med ∆x = 10^-8 gir den numeriske verdien som ligger nærmest 
# den eksakte verdien. 