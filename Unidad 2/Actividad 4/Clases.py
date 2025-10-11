class Libro:
    def __init__(self,titulo,autor,publicacon,prestado=False):
        self.titulo = titulo
        self.autor = autor
        self.publicacon = publicacon
        self.prestado = prestado
    bibliteca = "Biblbioteca Central"
    def prestar(self):
        if self.prestado == False:
            self.prestado = True
            return "El libro ha sido prestado"
        else:
            return "El libro ya esta prestado"
    def devolver(self):
        if self.prestado == True:
            self.prestado = False
            return "El libro ha sido devuelto"
        else:
            return "El libro no estaba prestado"
    def mostrar_estado(self):
        return(str(self.titulo) + " de " + str(self.autor) + " publicado en " + str(self.publicacon) + ".\nEstado: " + ("Prestado" if self.prestado else "Disponible"))