# Practica 4
#   Ejercicio 1
#       Pida al usuario 5 numeros y diga cual es mayor y cual es menor
#
#----------------inputs
numUno = input("Introduce un numero :")
numDos = input("Introduce otro número :")
numTres = input("Introduce otro número :")
numCuatro = input("Introduce otro número :")
numCinco = input("Introduce otro número :")
#
#
#---------------Logic
#listar elementos seleccionados
numerosLista = [int(numUno),int(numDos),int(numTres),int(numCuatro),
int(numCinco)]
#
#sortear lista
numerosLista.sort()
#
#primer numero y ultimo de la lista
numerosListaFirst = numerosLista[0]
numerosListaLast = numerosLista[-1]
#---------------Resultado
#numero mayor
print("El numero mayor es :" + str(numerosListaLast))
#numero menor
print("El numero menor es :" + str(numerosListaFirst))

