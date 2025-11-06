class Libro:
    """Representa un libro en el sistema de biblioteca."""
    
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio 
        self.estado = "disponible"
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.anio}) - {self.estado}"
    
    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del libro."""
        self.estado = nuevo_estado


class Usuario:
    """Representa un usuario de la biblioteca."""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []
    
    def __str__(self):
        return f"Usuario: {self.nombre}, Libros prestados: {len(self.libros_prestados)}"
    
    def tomar_prestado(self, libro):
        """Agrega un libro a la lista de préstamos."""
        self.libros_prestados.append(libro)
    
    def devolver_libro(self, libro):
        """Remueve un libro de la lista de préstamos."""
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)