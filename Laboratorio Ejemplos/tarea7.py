#Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor
def retornar_mayor(v1, v2):
    resultado = v1 if v1 > v2 else v2
    return resultado


# bloque principal
valor1 = int(input("Ingrese el primer valor:"))
valor2 = int(input("Ingrese el segundo valor:"))
print(retornar_mayor(valor1, valor2))