import math
x1 = int (input("Introduce el valor x del primer punto: "))
y1 = int (input("Introduce el valor y del primer punto: "))
x2 = int (input("Introduce el valor x del segundo punto: "))
y2 = int (input("Introduce el valor y del segundo punto: "))
x3 = int (input("Introduce el valor x del tercer punto: "))
y3 = int (input("Introduce el valor y del tercer punto: "))

ab = math.sqrt((x2 - x1)**2 + (y2 -y1)**2)
bc = math.sqrt((x3 - x2)**2 + (y3 -y2)**2)
ac = math.sqrt((x3 - x1)**2 + (y3 -y1)**2)

print("La distancia entre el primer punto y el segundo es ", ab, ".")
print("La distancia entre el segundo punto y el tercero es ", bc, ".")
print("La distancia entre el primer punto y el tercero es ", ac, ".")

if ((ab + bc) == ac):
    print("Por lo tanto los punto son colineales.")
else:
    print("Por lo tanto los punto no son colineales.")
    
        


