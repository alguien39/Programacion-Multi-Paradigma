from functools import reduce

# Filtrar ventas mayores a 100
def es_mayor_a_100(venta):
    return venta["monto"] > 100

# Aplicar impuesto y generar una nueva venta
def aplicar_impuesto(venta):
    return {
        "id": venta["id"],
        "monto_original": venta["monto"],
        "monto_final": venta["monto"] * 1.15
    }

# Acumular montos finales
def sumar_totales(acumulado, venta):
    return acumulado + venta["monto_final"]

def procesar_ventas(ventas):
    # Filtramos ventas
    ventas_filtradas = filter(es_mayor_a_100, ventas)
    #Aplicamos el impuesto
    ventas_transformadas = list(map(aplicar_impuesto, ventas_filtradas))

    # Reducir la lista para obtener el total
    total = reduce(sumar_totales, ventas_transformadas, 0)

    return ventas_transformadas, total


ventas_ejemplo = [ 
{'id': 1, 'monto': 50},
{'id': 2, 'monto': 150},
{'id': 3, 'monto': 200},
{'id': 4, 'monto': 80},
{'id': 5, 'monto': 300},
]

print(procesar_ventas(ventas_ejemplo))