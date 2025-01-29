rango = int(input("Ingresa un numero entero: "))

match rango:
    case rango if rango < 0:
        print("El numeor ingresado es menor que 0")
        
    case rango if rango