from math import sqrt

# Punkt Q(x|y)
qX = 812
qY = 177

# Streckfaktor
a = qY / pow(qX, 2)

# Abstand der senkrechten Tragseile
d = 1624 / 67

# Gesamtlänge der senkrechten Tragseile
g = 0

for i in range(1, 34):
    x = qX - (i * d)
    y = a * pow(x, 2)
    #print("Punkt " + str(i) + " (" + str(x) + " | " + str(y) + ")")
    g = g + (4 * y)

print("\nFunktionsgleichung: f(x) = " + str(a) + " * x^2")
print("\nDie Gesamtlänge der senkrechten Tragseile beträgt " + str(g) + " Meter.\n")


# Steigungsdreieck; je kleiner deltaX, desto genauer die Länge des Seils
deltaX = qX / 2
deltaY = 0

preY = qY

gesC = 0

for j in range(1, qX // 2):
    x = qX - j
    y = a * pow(x, 2)
    print("Punkt " + str(j) + " (" + str(x) + " | " + str(y) + ")")
    deltaY = preY - y
    c = sqrt(pow(deltaX, 2) + pow(deltaY, 2))
    gesC += c
    print(str(c))

print("\nDie Gesamtlänge des großen parabelförmigen Tragseils beträgt " + str(gesC) + " Meter.")
print(str(2 * sqrt(pow(qX, 2) + pow(qY, 2))))
