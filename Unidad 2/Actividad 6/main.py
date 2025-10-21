from Clases import Tarea, Tarea_Urgente, Tarea_Recurrente, Gestor_Tareas
import sys

gestor = Gestor_Tareas(archivo="tareas.json")

def Agregar_Tarea():
    tipo = input("Tipo de Tarea (normal/urgente/recurrente): ").strip().lower()
    titulo = input("Título: ")
    descripcion = input("Descripción: ")

    if tipo == "urgente":
        tarea = Tarea_Urgente(titulo, descripcion)
    elif tipo == "recurrente":
        prioridad = int(input("Prioridad (1-5): "))
        frecuencia = input("Frecuencia (diaria/semanal/mensual): ")
        tarea = Tarea_Recurrente(titulo, descripcion, prioridad, frecuencia)
    else:
        prioridad = int(input("Prioridad (1-5): "))
        tarea = Tarea(titulo, descripcion, prioridad)

    gestor.agregar_tarea(tarea)
    print("Tarea agregada exitosamente.")

def mostrar_lista():
    if not gestor.tareas:
        print("No hay tareas registradas.")
        return
    for idx, tarea in enumerate(gestor.tareas):
        print(f"[{idx}]")
        print(tarea.Mostrar_Datos())
        print("-" * 30)

def Eliminar_tarea():
    mostrar_lista()
    indice = int(input("Índice de la tarea a eliminar: "))
    try:
        gestor.eliminar_tarea(indice)
        print("Tarea eliminada exitosamente.")
    except IndexError as e:
        print(e)

def Marcar_Tarea_Completa():
    mostrar_lista()
    indice = int(input("Índice de la tarea a marcar como completa: "))
    try:
        gestor.marcar_tarea_completa(indice)
        print("Tarea marcada como completa.")
    except IndexError as e:
        print(e)


while True:
    print("\nGestor de Tareas")
    print("1. Agregar Tarea")
    print("2. Eliminar Tarea")
    print("3. Listar Tareas")
    print("4. Marcar Tarea como Completa")
    print("5. Salir")

    opcion = input("Seleccione una Opcion: ").strip()
    if opcion == "1":
        Agregar_Tarea()
    elif opcion == "2":
        Eliminar_tarea()
    elif opcion == "3":
        mostrar_lista()
    elif opcion == "4":
        Marcar_Tarea_Completa()
    elif opcion == "5":
        print("Saliendo del gestor de tareas.")
        sys.exit()
    else:
        print("Opción no válida. Intente nuevamente.")