numero = int(input("Ingresa un numero: "))

match numero:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case 4:
        print("cuatro")    
    case _:
        print("Número no reconocido")