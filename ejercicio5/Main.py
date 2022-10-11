def bisiesto():
    valor = int(input("Ingresa un año para saber si es bisiesto: "))

    if valor % 4 == 0 and (valor % 100 != 0 or valor % 400 == 0):
        print(f"El año {valor} es bisiesto")
    else:
        print("No es bisiesto")


bisiesto()
