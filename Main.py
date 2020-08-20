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
    print("Punkt " + str(i) + " (" + str(x) + " | " + str(y) +")")
    g = g + (2 * y)

print("\nFunktionsgleichung: f(x) = " + str(a) + " * x^2")
print("\nDie Gesamtlänge der senkrechten Tragseile beträgt " + str(g) + " Meter.")