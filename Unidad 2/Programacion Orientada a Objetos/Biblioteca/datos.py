import json
from modelos import Libro, Usuario


class BibliotecaData:
    """Maneja la persistencia de datos de la biblioteca."""
    
    @staticmethod
    def guardar_datos(biblioteca, archivo="datos_biblioteca.json"):
        """Guarda el estado de la biblioteca en un archivo JSON."""
        datos = {
            "libros": [
                {
                    "titulo": libro.titulo,
                    "autor": libro.autor,
                    "anio": libro.anio,
                    "estado": libro.estado
                }
                for libro in biblioteca.obtener_libros()
            ],
            "usuarios": [
                {
                    "nombre": usuario.nombre,
                    "libros_prestados": [
                        {
                            "titulo": libro.titulo,
                            "autor": libro.autor,
                            "anio": libro.anio
                        }
                        for libro in usuario.libros_prestados
                    ]
                }
                for usuario in biblioteca.obtener_usuarios()
            ]
        }
        
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    
    @staticmethod
    def cargar_datos(biblioteca, archivo="datos_biblioteca.json"):
        """Carga el estado de la biblioteca desde un archivo JSON."""
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
        except FileNotFoundError:
            print("No se encontró archivo de datos previo. Iniciando con biblioteca vacía.")
            return
        
        # Cargar libros
        for libro_data in datos.get("libros", []):
            # Verificar si el libro ya existe
            libro_existente = biblioteca.buscar_libro(libro_data["titulo"])
            if not libro_existente:
                libro = Libro(
                    libro_data["titulo"],
                    libro_data["autor"],
                    libro_data["anio"]
                )
                libro.estado = libro_data["estado"]
                biblioteca.libros.append(libro)
        
        # Cargar usuarios
        for usuario_data in datos.get("usuarios", []):
            # Verificar si el usuario ya existe
            usuario_existente = biblioteca.buscar_usuario(usuario_data["nombre"])
            if not usuario_existente:
                usuario = Usuario(usuario_data["nombre"])
                biblioteca.usuarios.append(usuario)
                
                # Recuperar libros prestados
                for libro_prestado_data in usuario_data.get("libros_prestados", []):
                    libro = biblioteca.buscar_libro(libro_prestado_data["titulo"])
                    if libro:
                        usuario.libros_prestados.append(libro)
                        libro.estado = "prestado"