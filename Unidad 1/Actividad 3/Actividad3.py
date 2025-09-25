eleccion = 1
lstTareas = []
print("SISTEMA GESTOR DE TAREAS PERSONALES")
while (eleccion != 5 and eleccion > 0 and eleccion <= 5):
    print("1)Agregar Tarea \n2)Mostrar Tareas Pendientes\n3)Marcar Tareas Como Completadas\n4)Eliminar Tareas\n5)Salir")
    eleccion = int(input("Seleccione lo que desea realizar...\n"))
    if (eleccion == 1):
        print("Agregar Tarea")
        NombreTarea = input("Ingrese el nombre de la tarea a agregar.\n")
        Tarea = {
            "Nombre": NombreTarea,
            "Estado": "Pendiente"
        }
        print("Tarea Agregada exitosamente :D")
        lstTareas.append(Tarea)
    elif (eleccion == 2):
        print("Tareas Pendientes")
        y = 0
        while (y < len(lstTareas)):
            if(lstTareas[y]["Estado"] == "Pendiente"):
                print (lstTareas[y]["Nombre"])
            y = y + 1
    elif (eleccion == 3):
        print("Marcar Tareas Como Completadas")
        z = "Si"
        while (z != "No"):
            y = 0
            while (y < len(lstTareas)):
                print (str(y+1)+") "+lstTareas[y]["Nombre"])
                y = y + 1
            y = int(input("Elegir Tarea A Marcar Como Completa:\n")) - 1
            x = input("Está seguro de que quiere completar la tarea:" + lstTareas[y]["Nombre"] + "?\nSi/No\n")
            if(x != "No" and y < len(lstTareas) and y >= 0):
                lstTareas[y]["Estado"] = "Completada"
            z = input("Desea Marcar Otra tarea como completada?\nSi/No\n")
    elif (eleccion == 4):
        print("Eliminar Tareas")
        z = "Si"
        while (z != "No"):
            y = 0
            while (y < len(lstTareas)):
                print (str(y+1)+") "+lstTareas[y]["Nombre"])
                y = y + 1
            y = int(input("Elegir Tarea A Eliminar:")) - 1
            x = input("Está seguro de que quiere ELIMINAR la tarea:" + lstTareas[y]["Nombre"] + "?\nSi/No\n")
            if(x != "No" and y < len(lstTareas) and y >= 0):
                lstTareas[y].pop()
            z = input("Desea ELIMINAR otra tarea?\nSi/No\n")
    elif (eleccion == 5):
        break
    else:
        print("Opcion Invalida: "+ i)