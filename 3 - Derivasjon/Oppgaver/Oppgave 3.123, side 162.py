# x    | –3 | –2 | –1 | 0 | 1 | 2 | 3 |  4 |
# f(x) |  9 |  4 |  1 | 0 | 1 | 4 | 9 | 14 |

# a) - Forklar hva programmet nedenfor gjør.
# b) - Vi ser at sammenhengen mellom x-verdier og f(x)-verdier er gitt ved f(x) = x2. 
#      Utvid programmet i oppgave a til også å tegne grafen til f '(x) = 2x. Kommenter.

from pylab import *     # Importerer alt fra pylab modulen

x = [-3, -2, -1, 0, 1, 2, 3, 4]     # Listen med x-verdier
f = [9, 4, 1, 0, 1, 4, 9, 16]       # Listen med f(x)-verdier

n = len(x)      # Setter n til lengden av x
g = zeros(n)    # Setter g verdien av n (f.eks 5), hvis n er 5 så gjør zeros konstantet at det 
                # blir 5 nuller

for i in range(0, n-1): # For hver verdi innenfor rekken 0 til en verdi mindre enn n 
                        # (hvis n er 10 så går det til 9)
    g[i] = (f[i+1] - f[i]) / (x[i+1] - x[i])    # Regner ut stigningstallet 
                                                # (den gjenomsnttlige endringen)

plot(x[0 : n-1], f[0 : n-1])    # Skriver grafen i system, men kun med de første verdiene i listene
plot(x[0 : n-1], g[0 : n-1])    # Skriver grafen i system, men den tegner den deriverte
grid()                          # Lager en grid (linjer i koordinatsystemet)
show()                          # Viser grafene i et koordinatsystem