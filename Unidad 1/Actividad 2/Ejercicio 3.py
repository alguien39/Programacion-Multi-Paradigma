eleccion = 1

while (eleccion != 5 and eleccion > 0 and eleccion <= 5):
    print("--Calculadora Python--")
    print("Opciones: \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Salir")
    eleccion = int(input("Ingrese la operacion que desea realizar (1/2/3/4/5): "))
    if (eleccion ==  1):
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 + num2
        print("El resultado de la suma es: "+str(resultado))
    elif (eleccion == 2):
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 - num2
        print("El resultado de la resta es: "+str(resultado))
    elif (eleccion == 3):
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 * num2
        print("El resultado de la multiplicacion es: "+str(resultado))
    elif (eleccion == 4):
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado de la division es: "+str(resultado))
        else:
            print("No se puede dividir entre 0")
    if eleccion == 5:
        print("Gracias por usar la calculadora")
        break