from math import sqrt

""" print("*" * 10 + "Perimetro del cuadrado" + "*" * 10)
lado = int(input("Lado del cuadrado: "))
res = lado * lado
print ("El prerimetro es: " + str(res))
print("*" * 10 + "Perimetro del cuadrado" + "*" * 10)

print ("*" * 10 + "Perimetro del equilatero" + "*" * 10)
lado = int(input("lados del triangulo equilatero: "))
res = lado * 3
print ("El perimetro del triangulo es: " + str(res))
print ("*" * 10 + "Perimetro del equilatero" + "*" * 10) """

""" print ("*" * 10 + "El altura del isosceles" + "*" * 10)
lado = int(input("Cuanto mide lado: "))
base = int(input("cuanto mide la base: "))
base2 = base / 2
res = sqrt((lado ** 2)-(base2 ** 2))
print ("La altura del isoseles: " + str(res))
print ("*" * 10 + "El altura del isosceles" + "*" * 10) """

print ("*" * 10 + "El area del isosceles" + "*" * 10)
lado = int(input("Cuanto mide el lado: "))
base = int(input("cuanto mide la base: "))
base2 = base / 2
altura = sqrt((lado ** 2) - (base2 ** 2))
area = base * altura / 2
print ("El area del isosceles es " + str(area))
print ("*" * 10 + "El area del isosceles" + "*" * 10)