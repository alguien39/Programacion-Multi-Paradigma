while (True):
    calificacion = int(input("Ingrese su calificacion de 0 a 100: "))
    if (calificacion >= 90 and calificacion <= 100):
        print("A")
    elif (calificacion >= 80 and calificacion < 90):
        print("B")
    elif (calificacion >= 70 and calificacion < 80):
        print("C")
    elif (calificacion >= 60 and calificacion < 70):
        print("D")
    elif (calificacion >= 0 and calificacion < 60):
        print("F")
    else:
        print("La calificacion ingresada no es valida")
    print("Fin del Programa")
    continuar = input("Desea continuar? (Si/No) ")
    if (continuar == "No"):
        break