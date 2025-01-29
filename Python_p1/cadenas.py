#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por 
# pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

"""
name=input("What's your name?: ")
m=input("Enter a number: ")

print( (name + "\n") * int(m))
"""

#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por 
# pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas 
# las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

name=str(input("Introduce tu nombre completo: "))

print(name.lower())
print(name.upper())
print(name.title())