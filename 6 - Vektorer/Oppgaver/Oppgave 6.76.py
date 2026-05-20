print("Skriv inn koordinatene til vektoren u = [x1 , y1]")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Skriv inn koordinatene til vektoren v = [x2 , y2]")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

skalarprodukt = x1*x2 + y1*y2

if skalarprodukt == 0:
    # Hvis skalarprodukt er 0 så er vektorne ortogonale
    print("Vektorene er ortogonale.")
elif x1*y2 == x2*y1:
    # Hvis skalarprodukt er produktet av stykket over så er vektorne parallelle
    print("Vektorene er parallelle.")
else:
    # Hvis verken eller stemmer så er vektorene verken ortogonele eller parallelle
    print("Vektorene er verken ortogonale eller parallelle.")