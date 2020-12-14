import math
x1 = int (input("Introduce el valor x del primer punto: "))
y1 = int (input("Introduce el valor y del primer punto: "))
x2 = int (input("Introduce el valor x del segundo punto: "))
y2 = int (input("Introduce el valor y del segundo punto: "))

a = (x2 - x1)**2
b = (y2 - y1)**2
c = math.sqrt(a+b)

print("La distancia entre los puntos es: ", c)
