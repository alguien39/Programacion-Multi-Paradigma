from Modules.model import Factura, GestorFacturas
from Modules import util

def crear_factura(gestor: GestorFacturas):
    util.limpiar_pantalla()
    print("Crear nueva factura\n")
    codigo = util.generar_codigo_tiket()
    print(f"Código generado: {codigo}")

    while True:
        rfc = input("RFC Receptor (13 chars): ")
        if len(rfc) == 13:
            break
        print("RFC inválido. Debe tener 13 caracteres.")

    concepto = input("Concepto: ") or "Sin concepto"

    while True:
        s = input("Importe total (ej. 123.45): ")
        try:
            importe = float(s)
            if importe <= 0:
                print("El importe debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Importe inválido. Intente de nuevo.")

    formas = ["Efectivo", "Tarjeta Debito", "Tarjeta Credito", "Cheque"]
    print("Formas de pago disponibles:")
    for i, f in enumerate(formas, 1):
        print(f"{i}. {f}")
    while True:
        sel = input("Seleccione forma de pago (1-4): ")
        try:
            idx = int(sel) - 1
            if 0 <= idx < len(formas):
                forma = formas[idx]
                break
        except Exception:
            pass
        print("Selección inválida.")

    print("\nResumen:")
    print(f"Código: {codigo}")
    print(f"RFC Receptor: {rfc}")
    print(f"Concepto: {concepto}")
    print(f"Importe: {importe}")
    print(f"Forma de pago: {forma}")

    if not util.confirmar_accion():
        print("Operación cancelada.")
        return

    try:
        f = Factura(codigo, rfc, concepto, importe, forma)
        gestor.agregar_factura(f)
        print("Factura agregada correctamente.")
    except Exception as e:
        print("Error creando la factura:", e)


def listar_facturas(gestor: GestorFacturas):
    util.limpiar_pantalla()
    print("Listado de facturas\n")
    gestor.listar_facturas()


def eliminar_factura(gestor: GestorFacturas):
    util.limpiar_pantalla()
    print("Eliminar factura\n")
    codigo = input("Ingrese codigoTiket de la factura a eliminar: ")
    f = gestor.buscar_factura(codigo)
    if not f:
        print("No se encontró la factura con ese código.")
        return
    print("Factura encontrada:")
    try:
        print(str(f))
    except Exception:
        print(f"codigoTiket: {f.codigoTiket} - RFC: {f.RFCReceptor} - Importe: {f.importeTotal}")
    if util.confirmar_accion():
        if gestor.eliminar_factura(codigo):
            print("Factura eliminada.")
        else:
            print("No se pudo eliminar la factura.")
    else:
        print("Operación cancelada.")


def menu():
    gestor = GestorFacturas()
    while True:
        print("\n--- Gestor de Facturas (sencillo) ---")
        print("1. Crear factura")
        print("2. Listar facturas")
        print("3. Eliminar factura")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            crear_factura(gestor)
        elif opcion == "2":
            listar_facturas(gestor)
        elif opcion == "3":
            eliminar_factura(gestor)
        elif opcion == "4":
            print("Guardando y saliendo...")
            gestor.guardar_facturas(gestor.archivo)
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()