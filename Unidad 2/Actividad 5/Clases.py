class producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        if precio >= 0:
            self._precio = precio
        else:
            print("El precio no puede ser menor a 0")
            self._precio = 0
        self.__stock = 0

    @property 
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, n):
        if n >= 0:
            self.__stock = n
        else:
            print("El stock no puede menor a 0")

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, p):
        if p >= 0:
            self._precio = p
        else:
            print("El precio no puede ser menor a 0")
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self._precio}, Stock: {self.__stock}"
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre
    
class Inventario:
    def __init__(self):
        self.__productos = dict()

    @property
    def productos(self):
        return self.__productos

    def agregar_producto(self, producto):
        if producto.nombre not in self.__productos:
            self.__productos[producto.nombre] = producto
        else:
            self.__productos[producto.nombre].stock += producto.stock
    
    def buscar_producto(self,nombre):
        if nombre in self.productos:
            return self.productos[nombre]
        else:
            return None
        
    def total_valor_inventario(self):
        total = 0
        for producto in self.__productos.values():
            total += producto.precio * producto.stock
        return total
    
    def __len__(self):
        return len(self.productos)
    
    def __str__(self):
        resultado = "Inventario:\n"
        for producto in self.__productos.values():
            resultado += f"{producto.nombre}" + f" Precio: {producto.precio}" + f" Stock: {producto.stock}\n\n"
        return resultado