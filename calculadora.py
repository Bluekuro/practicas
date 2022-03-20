from os import *
def sumar():
    print(" **  Sumar  **  ")
    print()
    sumando1 = int(input("Ingresa sumando 1: "))
    sumando2 = int(input("Ingresa sumando 2: "))
    print()
    res = sumando1 + sumando2
    print ("** El resultado es: " + str(res))
def resta():
    print(" **  Resta  **  ")
    print()
    minuendo = int(input("Ingresa minuendo: "))
    sustraendo = int(input("Ingresa sustraendo: "))
    print()
    res = minuendo - sustraendo
    print("** Elresultado es: " + str(res))
def multiplicacion():
    print(" **  Multiplicacion  **  ")
    print()
    factor1 = int(input("Ingresa factor 1: "))
    factor2 = int(input("Ingresa factor 2: "))
    print()
    res = factor1 * factor2
    print ("**El resultado es: " + str(res))
def divicion():
    print(" **  Division  **  ")
    print()
    divisor = int(input("Insgresa el divisor: "))
    dividendo = int(input("Insgresa el dividendo: "))
    if(divisor == 0):
        print()
        print("**El resultado es Infinito")
    else:
        res = divisor / dividendo
        print()
        print ("**El resultado es: " + str(res))
while(True):
    system("clear")
    print("*" *10 + " Calculadora " + "*"*10)
    print()
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("0.Salir")
    print()
    print("*" *10 + " Calculadora " + "*"*10)
    print()
    opcion = int(input("Ingresa opcion: "))
    if(opcion == 1):
        system("clear")
        print()
        sumar()
        print()
    elif(opcion == 2):
        print()
        resta()
        print()
    elif(opcion == 3):
        print()
        multiplicacion()
        print()
    elif(opcion == 4):
        print()
        divicion()
        print()
    elif(opcion == 0):
        print()
        print("**Cerrado")
        print()
        break
    else:
        print()
        print("**Opcion invalida")
        print()
    input("Presiona una tecla para continuar")
system("cowsay Adios")
input("Presiona una tecla para continuar: ")
system("clear")
