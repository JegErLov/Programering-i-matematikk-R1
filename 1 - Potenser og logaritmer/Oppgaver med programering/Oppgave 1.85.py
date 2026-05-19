# Oppgavetekst:
# Bruk cas og regn ut. Oppgi svaret med to desimaler.
# LAG også et program som regner ut logaritmene.

import math

# Det er gjort på to forskjellige måter, a, og b har en måte og c har en annen. I oppgave a, 
# så bruker vi den innebygde logaritme variabelen fra pylab, men i oppgave b og c hvor grunntallet 
# som er noe annet en 2, 10 eller e som er de valgene vi har ved å bruke pylab, da må vi importere 
# math, også skrive det på en litt annen måte en det vi gjorde på den første. 
# Man kan selvfølgelig skrive inn alle på den siste måten.

# Resulttatet skrives etter oppgaven

print("a) log2 7 =", math.log2(7))                  # a) log2 7 = 2.807354922057604
print("b) log3 4 =", math.log(4,3))                 # b) log3 4 = 1.2618595071429148
print("c) log7 45 =", math.log(45,7))               # c) log7 45 = 1.9562375434540753

# !!! Viktig husk komma mellom tekst og kode (f.eks log2(7))

# Oppgaven sier også at vi skal oppgi svaret med to desimaler, det gjøres slik:
print("a) log2 7 =", round(math.log2(7), 2))        # a) log2 7 = 2.81
print("b) log3 4 =", round(math.log(4,3), 2))       # b) log3 4 = 1.26
print("c) log7 45 =", round(math.log(45,7), 2))     # c) log7 45 = 1.96