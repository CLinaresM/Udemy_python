numero = int(input("Por favor, introduce un numero entero: "))

match numero:
    case 0: 
        print("El número es un cero")
    case numero if numero % 2 == 0:
        print("El número es par.")
    case numero if numero % 2 != 0:
        print("El numero es impar.")
    case _:
        print("Número no reconocido")    
