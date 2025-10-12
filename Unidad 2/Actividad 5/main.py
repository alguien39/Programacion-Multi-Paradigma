from Clases import producto, Inventario

unInventario = Inventario()

#Definicion de productos de prueba
p1 = producto("Laptop Hp", 10000)
p1.stock = 5
p2 = producto("Monitor Samsung", 5000)
p2.stock = 10
p3 = producto("Teclado Logitech", 1500)
p3.stock = 15
p4 = producto("Mouse Razer", 800)
p4.stock = 20

lista_productos = [p1, p2, p3, p4]
for prod in lista_productos:
    unInventario.agregar_producto(prod)

#Metodos del menu
def Agregar_Producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    p = producto(nombre, precio)
    p.stock = stock
    unInventario.agregar_producto(p)
    print("Producto agregado exitosamente.")

def Modificar_Sock():
    nombres = list(unInventario.productos.keys())
    for i, nombre in enumerate(nombres, 1):
        print(f"{i}) {unInventario.productos[nombre].nombre}")
    opcion = int(input("Seleccione el producto a modificar: ")) - 1
    producto_seleccionado = unInventario.productos[nombres[opcion]]
    respuesta = input(f"Desea modificar el stock del producto {producto_seleccionado.nombre}? (s/n)")
    if respuesta.lower() == 's':
        nuevo_stock = int(input("Ingrese el nuevo stock: "))
        producto_seleccionado.stock = nuevo_stock
        print("Stock modificado exitosamente.")
    respuesta = input(f"Desea modificar el precio del producto {producto_seleccionado.nombre}? (s/n)")
    if respuesta.lower() == 's':
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        producto_seleccionado.precio = nuevo_precio
        print("Precio modificado exitosamente.")

def buscar_Producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    p = unInventario.buscar_producto(nombre)
    if p:
        print(f"Producto: {nombre} encontrado.")
    else:
        print("Producto no encontrado.")

def comparar_Productos():
    nombre1 = input("Ingrese el nombre del primer producto: ")
    nombre2 = input("Ingrese el nombre del segundo producto: ")
    prod1 = unInventario.buscar_producto(nombre1)
    prod2 = unInventario.buscar_producto(nombre2)
    if prod1 and prod2:
        if prod1 == prod2:
            print("Los productos son iguales.")
        else:
            print("Los productos son diferentes.")
    else:
        print("Uno o ambos productos no existen.")

#Programa principal
respuesta = 0
while respuesta != 6:
    print("1. Agregar producto")
    print("2. Modificar stock o precio")
    print("3. Buscar producto")
    print("4. Comparar productos")
    print("5. Calcular valor total del inventario")
    print("6. Salir")
    respuesta = int(input("Seleccione una opcion: "))
    if respuesta == 1:
        Agregar_Producto()
    elif respuesta == 2:
        Modificar_Sock()
    elif respuesta == 3:
        buscar_Producto()
    elif respuesta == 4:
        comparar_Productos()
    elif respuesta == 5:
        print(f"El valor total del inventario es: {unInventario.total_valor_inventario()}")
    elif respuesta == 6:
        print("Saliendo del programa...")
    else:
        print("Opcion no valida, intente de nuevo.")