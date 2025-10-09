from Clases import Libro

libro1 = Libro("Game Of Thrones", "George R. R. Martin", 1996, False)
libro2 = Libro("El Hobbit","J. R. R. Tolkien", 1937, False)
libro3 = Libro("Storm Of Swords","George R. R. Martin", 2000,False)

libro2.prestar()
libro3.prestar()

print("Libro 1: \n"+libro1.mostrar_estado())
print("\nLibro 2: \n"+libro2.mostrar_estado())
print("\nLibro 3: \n"+libro3.mostrar_estado())

libro3.devolver()

print("\n Libro Devuelto: "+libro3.mostrar_estado())