#print('Hola Mundo')

#Escribir un programa que pregunte al usuario su edad
#y muestre por pantalla si es mayor de edad o no.

"""
edad = int(input("Por favor ingrese su edad: "))

if edad > 18:
    print("Ya eres mayor de edad")
else:
    print("Eres menor de edad")
"""
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario 
# coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""
key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")
"""

#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.

"""
n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)
"""

#Escribir un programa que pida al usuario
#un número entero y muestre por pantalla si es par o impar.

"""entero = int(input("Ingrese un número entero: "))

if entero % 2 ==0 :
    print(" El numero", entero, " es par")
else:
    print(" El numero", entero, " es impar")
"""


#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad 
# y sus ingresos mensuales
# ymuestre por pantalla si el usuario tiene que tributar o no.

age = int(input("Ingrese su edad: "))
income = int(input("Indique sus ingresos mensuales: "))

if age < 16:
    print ("No debe tributar")
elif income > 1000:
    print("Señor usuario debe tributar")

else:
    print("señor usuario no debe tributar")