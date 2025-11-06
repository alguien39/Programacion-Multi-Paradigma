from modelos import Libro, Usuario


class Biblioteca:
    """Gestiona las operaciones de la biblioteca."""
    
    def __init__(self):
        self.libros = []
        self.usuarios = []
    
    def agregar_libro(self, titulo, autor, anio):
        """Agrega un libro al catálogo."""
        nuevo_libro = Libro(titulo, autor, anio)
        self.libros.append(nuevo_libro)
        return f"Libro '{titulo}' agregado exitosamente"
    
    def agregar_usuario(self, nombre):
        """Registra un nuevo usuario."""
        nuevo_usuario = Usuario(nombre)
        self.usuarios.append(nuevo_usuario)
        return f"Usuario '{nombre}' registrado exitosamente"
    
    def mostrar_libros_disponibles(self):
        """Muestra todos los libros disponibles."""
        disponibles = [libro for libro in self.libros 
                      if libro.estado == "disponible"]
        
        if not disponibles:
            return "No hay libros disponibles"
        
        resultado = "Libros disponibles:\n"
        for libro in disponibles:
            resultado += f"- {libro}\n"
        return resultado
    
    def buscar_libro(self, titulo):
        """Busca un libro por título."""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    
    def buscar_usuario(self, nombre):
        """Busca un usuario por nombre."""
        for usuario in self.usuarios:
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None
    
    def prestar_libro(self, titulo_libro, nombre_usuario):
        """Gestiona el préstamo de un libro."""
        usuario = self.buscar_usuario(nombre_usuario)
        libro = self.buscar_libro(titulo_libro)
        
        if not libro:
            return "Libro no encontrado"
        if not usuario:
            return "Usuario no encontrado"
        if libro.estado != "disponible":
            return "El libro no está disponible"
        
        libro.cambiar_estado("prestado")
        usuario.tomar_prestado(libro)
        return f"Libro '{titulo_libro}' prestado a {nombre_usuario}"
    
    def devolver_libro(self, titulo_libro, nombre_usuario):
        """Gestiona la devolución de un libro."""
        usuario = self.buscar_usuario(nombre_usuario)
        libro = self.buscar_libro(titulo_libro)
        
        if not libro:
            return "Libro no encontrado"
        if not usuario:
            return "Usuario no encontrado"
        
        # Verificar si el usuario tiene el libro prestado
        usuario_tiene_libro = any(l.titulo.lower() == titulo_libro.lower() 
                                 for l in usuario.libros_prestados)
        
        if not usuario_tiene_libro:
            return f"El usuario {nombre_usuario} no tiene el libro '{titulo_libro}' prestado"
        
        libro.cambiar_estado("disponible")
        usuario.devolver_libro(libro)
        return f"Libro '{titulo_libro}' devuelto por {nombre_usuario}"
    
    def obtener_libros(self):
        """Retorna la lista de libros."""
        return self.libros
    
    def obtener_usuarios(self):
        """Retorna la lista de usuarios."""
        return self.usuarios