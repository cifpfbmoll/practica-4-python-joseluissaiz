# Practica 4
#   Ejercicio 3
#       Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, 
#       y pida los datos según que caso y muestre el resultado.
#
#----------------Menu - descripcion
print("Calcular el area de una figura")
#
#----------------tipo de operacion
tipoOperacion = input("Triangulo o cuadrado? : [t,c]")
#
#----------------Logic
#calcular el area dependiendo del tipo de operacion y mostrar resultado
if tipoOperacion == "t":
    baseTriangulo = input("Introduce la base del triangulo :")
    alturaTriangulo = input("Introduce la altura del triangulo :")
    areaTriangulo = (float(baseTriangulo) * float(alturaTriangulo)) / 2
    print("El area del triangulo es de " + str(round(areaTriangulo,2)))
elif tipoOperacion == "c":
        ladoCuadrado = input("Introduce la base o la altura del cuadrado :")
        areaCuadrado = float(ladoCuadrado) * float(ladoCuadrado)
        print("El area del cuadrado es de " + str(round(areaCuadrado,2)))
else:
    print("La operacion elegida no es valida.")


