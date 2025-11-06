from operaciones import Biblioteca
from datos import BibliotecaData

biblioteca = Biblioteca()
    
# Cargar datos existentes
BibliotecaData.cargar_datos(biblioteca)
    
while True:
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Registrar usuario")
    print("3. Mostrar libros disponibles")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Guardar y salir")
        
    opcion = input("Seleccione una opción: ").strip()
        
    if opcion == "1":
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        anio = input("Año: ").strip()
        if titulo and autor and anio:
            resultado = biblioteca.agregar_libro(titulo, autor, anio)
            print(resultado)
        else:
            print("Error: Todos los campos son obligatorios")
        
    elif opcion == "2":
        nombre = input("Nombre de usuario: ").strip()
        if nombre:
            resultado = biblioteca.agregar_usuario(nombre)
            print(resultado)
        else:
            print("Error: El nombre es obligatorio")
            
    elif opcion == "3":
        resultado = biblioteca.mostrar_libros_disponibles()
        print(resultado)
            
    elif opcion == "4":
        titulo = input("Título del libro: ").strip()
        usuario = input("Nombre de usuario: ").strip()
        if titulo and usuario:
            resultado = biblioteca.prestar_libro(titulo, usuario)
            print(resultado)
        else:
            print("Error: Título y usuario son obligatorios")
            
    elif opcion == "5":
        titulo = input("Título del libro: ").strip()
        usuario = input("Nombre de usuario: ").strip()
        if titulo and usuario:
            resultado = biblioteca.devolver_libro(titulo, usuario)
            print(resultado)
        else:
            print("Error: Título y usuario son obligatorios")
            
    elif opcion == "6":
        BibliotecaData.guardar_datos(biblioteca)
        print("Datos guardados. ¡Hasta pronto!")
        break
            
    else:
        print("Opción no válida. Por favor, seleccione 1-6.")
