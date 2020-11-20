# Practica 4
#   Ejercicio 4
#       Pida al usuario tres números y un cuarto número, y compruebe si este 
#       último es divisor de los tres números primeros.
#
#
#----------------Variables
compatiblesCount = 0
numCompatibles = []
#
#----------------inputs
numUno = input("Introduce un numero :")
numDos = input("Introduce otro número :")
numTres = input("Introduce otro número :")
numCuatro = input("Introduce el número para comparar :")
#
#
#---------------Logic
#comparacion de numeros
if float(numUno) % float(numCuatro) == 0:
    numCompatibles.append(str(numUno))
    compatiblesCount += 1
#
if float(numDos) % float(numCuatro) == 0:
    numCompatibles.append(str(numDos))
    compatiblesCount += 1
#
if float(numTres) % float(numCuatro) == 0:
    numCompatibles.append(str(numTres))
    compatiblesCount += 1
#
#
#---------------Resultado
if compatiblesCount == 0:
    print("Ningun numero mencionado es divisible entre " + str(numCuatro))
else:
    print("Los numeros divisibles entre " + str(numCuatro) + \
        f" son {numCompatibles}")
