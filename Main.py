from math import sqrt

# Punkt Q(x|y)
qX = 812
qY = 177

# Streckfaktor
a = qY / pow(qX, 2)

# Abstand der senkrechten Tragseile
d = 1624 / 67

# Gesamtlänge der senkrechten Tragseile
l = 0

for i in range(1, 34):
    x = qX - (i * d)
    y = a * pow(x, 2)
    #print("Punkt " + str(i) + " (" + str(x) + " | " + str(y) + ")")
    l += 4 * y

print("\nFunktionsgleichung: f(x) = " + str(a) + " * x^2")
print("\nDie Gesamtlänge der senkrechten Tragseile beträgt " + str(l) + " Meter.\n")


# Anzahl der Steigungsdreicke; je mehr, desto genauer die Länge des Seils
k = 10000000

# Steigungsdreieck; je kleiner deltaX, desto genauer die Länge des Seils
deltaX = qX / k
deltaY = 0
dY = 0

gesC = 0

for j in range(1, k+1):
    print(str(j))
    x = qX - (j * deltaX)
    y = a * pow(x, 2)
    print("Punkt " + str(j) + " (" + str(x) + " | " + str(y) + ")")
    deltaY = qY - y - dY
    dY += deltaY
    print(str(deltaX) + " | " + str(deltaY))
    c = sqrt(pow(deltaX, 2) + pow(deltaY, 2))
    gesC += 4*c

print("\nDie Gesamtlänge der zwei großen parabelförmigen Tragseile beträgt " + str(gesC) + " Meter.")
