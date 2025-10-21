import json
import os

Archivo_Info = "Tareas.json"

class Tarea:
    def __init__(self, titulo, descripcion, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self._Completada = False
    
    @property
    def Completada(self):
        return self._Completada
    
    @Completada.setter
    def Completada(self, valor):
        if isinstance(valor, bool):
            self._Completada = valor
        else:
            raise ValueError("El valor debe ser un booleano.")
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._titulo = valor
        else:
            raise ValueError("El título debe ser una cadena no vacía.")
        
    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        if isinstance(valor, str):
            self._descripcion = valor
        else:
            raise ValueError("La descripción debe ser una cadena.")
    
    @property
    def prioridad(self):
        return self._prioridad
    
    @prioridad.setter
    def prioridad(self, valor):
        if isinstance(valor, int) and 1 <= valor <= 5:
            self._prioridad = valor
        else:
            raise ValueError("La prioridad debe ser un entero entre 1 y 5.")
        
    def Marcar_Completa(self):
        self.Completada = True

    def Mostrar_Datos(self):
        estado = "Completada" if self.Completada else "Pendiente"
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nPrioridad: {self.prioridad}\nEstado: {estado}"
    

class Tarea_Urgente(Tarea):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion, prioridad=5)
    
    def Mostrar_Datos(self):
        datos_base = super().Mostrar_Datos()
        return f"{datos_base}\n¡Esta tarea es urgente!"
    
class Tarea_Recurrente(Tarea):
    def __init__(self, titulo, descripcion, prioridad, frecuencia):
        super().__init__(titulo, descripcion, prioridad)
        self.frecuencia = frecuencia
    
    @property
    def frecuencia(self):
        return self._frecuencia
    
    @frecuencia.setter
    def frecuencia(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._frecuencia = valor
        else:
            raise ValueError("La frecuencia debe ser una cadena no vacía.")
    
    def Mostrar_Datos(self):
        datos_base = super().Mostrar_Datos()
        return f"{datos_base}\nFrecuencia: {self.frecuencia} Dias"
    
class Gestor_Tareas:
    def __init__(self, archivo):
        self.archivo = archivo
        self.tareas : list[Tarea] = []
        self.cargar_tareas(archivo)
    
    def agregar_tarea(self, tarea: Tarea):
        self.tareas.append(tarea)
        self.guardar_tareas(self.archivo)

    def eliminar_tarea(self, indice: int):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            self.guardar_tareas(self.archivo)
        else:
            raise IndexError("Índice de tarea fuera de rango.")
        
    def listar_tareas(self):
        for tarea in self.tareas:
            print(tarea.Mostrar_Datos())
            print("-" * 20)
        
    def marcar_tarea_completa(self, indice: int):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].Marcar_Completa()
            self.guardar_tareas(self.archivo)
        else:
            raise IndexError("Índice de tarea fuera de rango.")

    def guardar_tareas(self, archivo: str):
        datos = []
        for tarea in self.tareas:
            tipo_tarea = "Tarea"
            if isinstance(tarea, Tarea_Urgente):
                tipo_tarea = "Tarea_Urgente"
            elif isinstance(tarea, Tarea_Recurrente):
                tipo_tarea = "Tarea_Recurrente"
            tarea_dict = {
                "tipo": tipo_tarea,
                "titulo": tarea.titulo,
                "descripcion": tarea.descripcion,
                "prioridad": tarea.prioridad,
                "completada": tarea.Completada
            }
            if isinstance(tarea, Tarea_Recurrente):
                tarea_dict["frecuencia"] = tarea.frecuencia
            datos.append(tarea_dict)
        
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)
    
    def cargar_tareas(self, archivo: str):
        if not os.path.exists(archivo):
            return
        
        with open(archivo, 'r') as f:
            datos = json.load(f)
        
        for tarea_dict in datos:
            tipo_tarea = tarea_dict.get("tipo", "Tarea")
            if tipo_tarea == "Tarea_Urgente":
                tarea = Tarea_Urgente(
                    titulo=tarea_dict["titulo"],
                    descripcion=tarea_dict["descripcion"]
                )
            elif tipo_tarea == "Tarea_Recurrente":
                tarea = Tarea_Recurrente(
                    titulo=tarea_dict["titulo"],
                    descripcion=tarea_dict["descripcion"],
                    prioridad=tarea_dict["prioridad"],
                    frecuencia=tarea_dict["frecuencia"]
                )
            else:
                tarea = Tarea(
                    titulo=tarea_dict["titulo"],
                    descripcion=tarea_dict["descripcion"],
                    prioridad=tarea_dict["prioridad"]
                )
            tarea.Completada = tarea_dict["completada"]
            self.tareas.append(tarea)
        
    