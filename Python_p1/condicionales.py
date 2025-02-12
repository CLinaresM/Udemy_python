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
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e 
#imprima por pantalla si la contraseña introducida por el usuario 
#coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas
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

"""
entero = int(input("Ingrese un número entero: "))

if entero % 2 ==0 :
    print(" El numero", entero, " es par")
else:
    print(" El numero", entero, " es impar")
"""


#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
# iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad 
# y sus ingresos mensuales
# ymuestre por pantalla si el usuario tiene que tributar o no.
"""
age = int(input("Ingrese su edad: "))
income = int(input("Indique sus ingresos mensuales: "))

if age < 16:
    print ("No debe tributar")
elif income > 1000:
    print("Señor usuario debe tributar")

else:
    print("señor usuario no debe tributar")
"""

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y 
# el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
# que le corresponde.
"""
nombre=input("Ingresa tu nombre: ")
sexo=input("Ingresa tu sexo 'M o H': ")

if sexo == "M":
    if nombre.lower()< "m":
        group="A"
    else:
        group="B"

else:
    if nombre.lower()>"n":
        group="A"
    else:
        group="B"
print("Tu grupo es: ", group)        


name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)


name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)
"""
#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

#Renta	                 Tipo impositivo
#Menos de 10000€	          5%
##Entre 10000€ y 20000€	     15%
#Entre 20000€ y 35000€	     20%
#Entre 35000€ y 60000€	     30%
#Más de 60000€	             45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
rentaAnual=int(input("Ingresa su renta anual: "))

if rentaAnual<10000:
    impositivo=5
elif rentaAnual<20000:
    impositivo=15
elif rentaAnual<35000:
    impositivo=20
elif rentaAnual<60000:
    impositivo=30
else:
    impositivo=45
print(f"te corresponde el impositivo del: {impositivo}")
"""

#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación 
# comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
# pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla
# con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada 
# por la puntuación del nivel.

#  Nivel	                   Puntuación
#Inaceptable	             0.0
#Aceptable	                 0.4
#Meritorio	                 0.6 o más

#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero
# que recibirá el usuario.
"""
puntuacion=float(input("ingresa tu puntuacion: "))
dinero=2400
if puntuacion == 0.0:
    print(f"Tu nivel de rendimiento es Inaceptable y la cantidad por ello es de {puntuacion * dinero}€")
elif puntuacion == 0.4:
    print(f"Tu nivel de rendimiento es Aceptable y la cantidad por ello es de {puntuacion*dinero,}€")
elif puntuacion==0.6:
    print(f"Tu nivel de rendimiento es Meritorio0.6
     y la cantidad por ello es de {puntuacion*dinero,}€")


bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))
"""

#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
#  de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al
# usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
#  si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

"""
edad=int(input("ingresa tu edad: "))
menor="Ingresa gratis"
medio="Debe pagar 5€"
mayor="debe pagar 10€"

if edad <= 4:
    print(menor)
elif edad<=18:
    print(medio)
else:
    print(mayor)    

edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")
"""
#

# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")