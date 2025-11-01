import json
import os

class Factura:
    def __init__(self, codigoTiket, RFCReceptor, concepto, importeTotal, formaPago):
        self.__RFCEmisor = str("BAMJ041020292")
        if (len(str(codigoTiket)) == 10 ): self.__codigoTiket = codigoTiket
        else: raise Exception("El Codigo De Tiked debe ser de 10 caracteres")
        if (len(RFCReceptor) == 13): self.__RFCReceptor = RFCReceptor
        else: raise Exception("El RFC debe ser una cadena de 13 caracteres alfanumericos")
        self.__concepto = concepto
        importe = float(importeTotal)
        if (importe > 0): self.__importeTotal = importeTotal
        else: raise Exception("El importe a de ser mayor a 0")
        if (self.ComprobarFormaPago(formaPago)): self.__formaPago = formaPago
        else: raise Exception("Forma De Pago No Valida")

    @property
    def RFCEmisor(self):
        return self.__RFCEmisor
    
    @property
    def codigoTiket(self):
        return self.__codigoTiket
    
    @codigoTiket.setter
    def codigoTiket(self, cod):
        if (len(str(cod)) == 10):
            self.__codigoTiket = cod
        else:
            raise Exception("Codigo De Tiket Invalido")
        
    @property
    def RFCReceptor(self):
        return self.__RFCReceptor
    
    @RFCReceptor.setter
    def RFCReceptor(self, RFC):
        if (len(RFC) == 13):
            self.__RFCReceptor = RFC
        else:
            raise Exception("El RFC debe ser una cadena valida de 13 caracteres alfanumericos")
    
    @property
    def concepto(self):
        return self.__concepto
    
    @concepto.setter
    def concepto(self, cad):
        self.__concepto = cad
    
    @property
    def importeTotal(self):
        return self.__importeTotal
    
    @importeTotal.setter
    def importeTotal(self, importe):
        fimporte = float(importe)
        if (fimporte > 0):
            self.__importeTotal = fimporte
        else:
            raise Exception("Valor Invalido")
        
    @property
    def formaPago(self):
        return self.__formaPago
    
    @formaPago.setter
    def formaPago(self, forma):
        match forma:
            case 'Tarjeta Debito' | 'Tarjeta Credito' | 'Efectivo' | 'Cheque':
                self.__formaPago = forma
            case _:
                raise Exception("Forma De Pago Invalida")
            
    def __str__(self):
        strFactura = "Factura:" + self.codigoTiket + "\n Datos Del Emisor:\n RFC del Emisor: " + self.RFCEmisor + " Nombre: Joham Barberena\n Datos del Receptor:\n RFC del Receptor: " + self.RFCReceptor + " Concepto: " + self.concepto + " Importe Total: $" + str(self.importeTotal) + " Forma De Pago: " + self.formaPago
        return strFactura

    @staticmethod
    def ComprobarFormaPago(forma):
        match forma:
            case 'Tarjeta Debito' | 'Tarjeta Credito' | 'Efectivo' | 'Cheque':
                return True
            case _:
                return False

class GestorFacturas:
    def __init__(self, archivo="facturas.json"):
        self.archivo = archivo
        self.facturas = []
        self.cargar_facturas(archivo)

    def agregar_factura(self, factura):
        if not isinstance(factura, Factura):
            raise Exception("Debe proporcionar una instancia de Factura")
        self.facturas.append(factura)
        self.guardar_facturas(self.archivo)

    def buscar_factura(self, codigoTiket):
        for f in self.facturas:
            try:
                if f.codigoTiket == codigoTiket:
                    return f
            except Exception:
                continue
        return None

    def eliminar_factura(self, codigoTiket):
        f = self.buscar_factura(codigoTiket)
        if f:
            self.facturas.remove(f)
            self.guardar_facturas(self.archivo)
            return True
        return False

    def listar_facturas(self):
        if not self.facturas:
            print("No hay facturas registradas.")
            return
        for idx, f in enumerate(self.facturas):
            print(f"[{idx}]")
            try:
                print(str(f))
            except Exception:
                print(Exception("No se pudo mostrar la factura"))
            print("-" * 30)

    def guardar_facturas(self, archivo):
        datos = []
        for f in self.facturas:
            try:
                datos.append({
                    "codigoTiket": f.codigoTiket,
                    "RFCReceptor": f.RFCReceptor,
                    "concepto": f.concepto,
                    "importeTotal": f.importeTotal,
                    "formaPago": f.formaPago
                })
            except Exception:
                continue
        with open(archivo, "w", encoding="utf-8") as fh:
            json.dump(datos, fh, indent=2, ensure_ascii=False)

    def cargar_facturas(self, archivo):
        if not os.path.exists(archivo):
            self.facturas = []
            return
        try:
            with open(archivo, "r", encoding="utf-8") as fh:
                datos = json.load(fh)
        except Exception:
            self.facturas = []
            return

        self.facturas = []
        for item in datos:
            try:
                f = Factura(
                    item.get("codigoTiket"),
                    item.get("RFCReceptor"),
                    item.get("concepto"),
                    item.get("importeTotal"),
                    item.get("formaPago")
                )
                self.facturas.append(f)
            except Exception:
                continue