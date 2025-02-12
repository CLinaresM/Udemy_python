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

"""

name=str(input("Introduce tu nombre completo: "))

print(name.lower())
print(name.upper())
print(name.title())

"""


#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
#  muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""
name=input("Ingresa tu nombre: ")

print(f"{name.upper()} tiene {len(name)} letras" )
print(name.upper() + " tiene " + str(len(name)) + " letras")
"""

#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, 
# y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])
"""
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""
frase=input("introduce una frase: ")
print(frase[::-1])
"""

#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal en minúscula, 
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""25.30

frase=input("Introduce una frase: ")
vocal=input("Introduce una Vocal: ")
print(frase.replace(vocal, vocal.upper()))
"""
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
# otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
email = input("Introduce tu correo electrónico: ")
print(email[:email.find("@"):]+ "@ceu.es")
"""
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
# y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
precio=input("Ingresa el valordel producto en euros con dos decimales: ")
print(precio[:precio.find(".")], "euros y ", precio[precio.find(".")+1:],"centimos")
"""

#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por 
#pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""
fecha = input("introduce tu fecha d enacimiento con el siguiente fromato dd/mm/aaaa: ")
print("Dia: ", fecha[:2])
print("Mes: ", fecha[3:5])
print("Año: ", fecha[6:])


fecha = input("introduce tu fecha de nacimiento con el siguiente fromato dd/mm/aaaa: ")
mesaño=fecha[fecha.find("/")+1:]
print("Día: ", fecha[:fecha.find("/")])
print("Mes: ",mesaño[:mesaño.find("/")])
print("Año: ", mesaño[mesaño.find("/")+1:])
"""

#Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
#separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""
producto=input("Ingrese los productos a comprarn separelos por comas: ")
print(producto.replace(",", "\n"))
"""
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades
#y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 
#6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 
#8 dígitos enteros y 2 decimales.

"""
producto=input("Ingresa el nombre del producto: ")
precio=float(input("Ingresa el precio del producto: "))
cantidad=int(input("Ingresa la cantidad de unidades del producto: "))
total= float(precio*cantidad)

print(f"{producto}: {cantidad:3d} unidades x valor {precio:9.2f} = $ {total:11.2f}")
"""
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))