# Captura de entrada del usuario
numero = int(input("Ingrese un número entero: "))

# Utilizar la declaración match para clasificar el número
match numero:
    case numero if numero < 0:
        print(f"El número {numero} se encuentra en el Rango 1: Números negativos.")
    case numero if 0 <= numero < 10:
        print(f"El número {numero} se encuentra en el Rango 2: Números entre 0 y 9.")
    case numero if numero >= 10:
        print(f"El número {numero} se encuentra en el Rango 3: Números mayores o iguales a 10.")
    case _:
        print(f"El número {numero} no se encuentra en ningún rango conocido.")


