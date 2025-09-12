#Ejercicios de Practica de condicionales
#Recive el valor de el lado

#Ejercicio 1
"""lado = float(input("Ingrese el lado de el cuadrado: "))
if (lado > 0):
    area = lado * lado
    print("El area del cuadrado es: "+str(area))
else:
    print("El valor del lado no es valido")"""

#Ejercicio 2 Condicional If-Then
"""tengoHijos = True
print(type(tengoHijos))
print("tengo hijos: "+str(tengoHijos))"""

#Ejercicio 3 Condicional If-Then-elif-Else
"""Temperatura = float(input("Cual es la temperatura ambiente? "))
Dinero = float(input("Cuanto dinero tienes? "))
if (Temperatura > 27 and Dinero >= 5):
    print("Comprar Helado")
elif (Temperatura < 15):
    print("Comprar chocolate")
else:
    print("Comprar Jugo de naranja")
print("Fin del Programa")"""

#Ejercicio Practico
"""distancia = int(input("Ingrese la distancia a la que se encuentra de su pareja: "))
if (distancia <= 4 ):
    print("Voy corriendo!!!") """

#Ejercicio Practico 2
"""NumCamiseta = int(input("Ingrese el numero de la camiseta del jugador:"))
if (NumCamiseta == 19):
    print("Anda pa' alla, bobo")"""

#Ejercicio Practico 3
"""Magnitud = float(input("Ingrese la magnitud del sismo:"))
if (Magnitud >= 5.2):
    print("Alerta de Tsunami.")"""


#Ejercicio 1 Condicinal Anidado
"""tipo = input("Ingrese el tipo de atraccion (Montana Rusa, Tren)")
if (tipo == "Montana Rusa"):
    estatura = float(input("Ingrese su estatura en metros: "))
    if (estatura >= 1.61):
        print("Diviertete en la montana rusa")
    else:
        print("Estatura no permitida")
elif (tipo ==  "Tren"):
    print("Diviertete en el tren")"""

#Ejercicio Practico Condicional Anidado 1
"""generoFavorito = input("Cual es tu genero musical favorito? ")
if (generoFavorito == "Rock"):
    print("Que buen gusto")
else:
    print("Que asco")"""

#Ejercicio Practico Condicional Anidado 2
"""votacionesMichael =  int(input("Ingrese el numero de votos para Michael: "))
votacionesAna = int(input("Ingrese el numero de votos para Ana: "))

if (not votacionesMichael == votacionesAna):
    if (votacionesMichael > votacionesAna):
        print("Gana Michael con "+str(votacionesMichael)+" votos")
    else:
        print("Gana Ana con "+str(votacionesAna)+" votos")
else:
    print("Empate con "+str(votacionesAna)+" votos")"""

#Ejercicio practico con ciclos While
"""i = 1
while (i <= 5):
    print(i)
    i = i + 1
print("Fin del programa")"""

#Ejercicio Practico 2 con ciclos While
"""Num = int(input("Ingrese el numero de veces que quiere que se repita el ciclo: "))
i = 1
while (i <= Num):
    print("****")
    i = i + 1
print("Fin del programa")"""

#Ejercicio Practico 3 con ciclos While
while (True):
    contrasena = input("Ingrese la contrasena: ")
    if contrasena == "Roberto":
        print("Contrasena correcta")
        break
    print("Contrasena incorrecta, intente de nuevo")
print("Fin del programa")