# Practica 4
#   Ejercicio 5
#       Pida al usuario un importe en euros y diga si el cajero automático le
#       puede dar dicho importe utilizando el mismo billete y el más grande
#       (recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5 €).
#
#
#----------------Variables
numBilletes = 0
#----------------inputs
numUno = input("Introduce una cantidad (€) :")
#
#
#
#---------------Logic
# si el numero mencionado es divisible entre los posibles billetes
if float(numUno) % 500 == 0:
    numBilletes = float(numUno) / 500
    print("El cajero te devuelve " + str(int(numBilletes)) + " billete/s de 500€.")
elif float(numUno) % 200 == 0:
    numBilletes = float(numUno) / 200
    print("El cajero te devuelve " + str(int(numBilletes)) + " billete/s de 200€.")
elif float(numUno) % 100 == 0:
    numBilletes = float(numUno) / 100
    print("El cajero te devuelve " + str(int(numBilletes)) + " billete/s de 100€.")
elif float(numUno) % 50 == 0:
    numBilletes = float(numUno) / 50
    print("El cajero te devuelve " + str(int(numBilletes)) + " billete/s de 50€.")
elif float(numUno) % 20 == 0:
    numBilletes = float(numUno) / 20
    print("El cajero te devuelve " + str(int(numBilletes)) + " billete/s de 20€.")
elif float(numUno) % 10 == 0:
    numBilletes = float(numUno) / 10
    print("El cajero te devuelve " + str(int(numBilletes)) + " billete/s de 10€.")
elif float(numUno) % 5 == 0:
    numBilletes = float(numUno) / 5
    print("El cajero te devuelve " + str(int(numBilletes)) + " billete/s de 5€.")
else:
    print("El cajero no puede devolverte el cambio solo en billetes")