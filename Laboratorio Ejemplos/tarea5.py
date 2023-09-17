import sys

def mostrar_perimetro(lado):
    per = lado * 4
    print("El perímetro es", per)


def mostrar_superficie(lado):
    sup = lado * lado
    print("La superficie es", sup)


def calcular_area(lado):
    return lado * lado


def cargar_dato():
    try:
        la = int(input("Ingrese el valor del lado de un cuadrado:"))
        opcion = input("Quiere calcular el perimetro o la superficie ?")
    except ValueError:
        sys.exit("El valor ingresado no es válido.")

    if opcion == "perimetro":
        mostrar_perimetro(la)
    else:
        mostrar_superficie(la)


cargar_dato()
