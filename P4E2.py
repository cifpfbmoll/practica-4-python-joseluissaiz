# Practica 4
#   Ejercicio 2
#       Pida al usuario 5 números y diga si estos estaban en orden decreciente,
#       creciente o desordenados.
#
#----------------imports
import operator 
import itertools 
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
#comprobar con creciente y decreciente
if numerosLista == sorted(numerosLista):
    print("La lista es creciente")
elif numerosLista == sorted(numerosLista, reverse=True):
    print("La lista es decreciente")
else:
    print("La lista esta desordenada")

