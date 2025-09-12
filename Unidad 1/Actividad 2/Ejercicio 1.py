while(True):
    Eleccion = input("Que area desea calcular? (Cuadrado, Triangulo) ")
    if (Eleccion == "Cuadrado"):
        lado = float(input("Ingrese el lado del cuadrado: "))
        if (lado > 0):
            area = lado * lado
            print("El area del cuadrado es: "+str(area))
        else:
            print("El valor del lado debe ser mayor a 0")
    elif (Eleccion == "Triangulo"):
        base = float(input("Ingrese la base del triangulo:"))
        altura = float(input("Ingrese la altura del triangulo: "))
        if (base > 0 and altura > 0):
            area = (base * altura) / 2
            print("El area del triangulo es: "+str(area))
        else:
            print("Los valores de base y altura deben ser mayores a 0")
    else:
        print("La opcion ingresada no es valida")
    continuar = input("Desea continuar? (Si/No) ")
    if (continuar == "No"):
        break