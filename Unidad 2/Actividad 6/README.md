# Gestor de Tareas — Actividad 6

Breve descripción
- Aplicación de consola en Python para crear, listar, marcar como completadas y eliminar tareas.
- Soporta tipos de tareas mediante herencia: Tarea (normal), Tarea_Urgente (prioridad fija = 5) y Tarea_Recurrente (frecuencia).
- Los datos se persisten en un archivo JSON para mantener las tareas entre ejecuciones.

Ejecución
1. Ejecutar:
   - python main.py
   - o en algunas instalaciones: py main.py
2. Seguir el menú interactivo en consola:
   - Agregar Tarea: indicar tipo (normal/urgente/recurrente), título, descripción y valores solicitados.
     - Tarea_Urgente: al crearla, la prioridad se establece en 5 por diseño actual.
     - Tarea_Recurrente: se solicita prioridad y frecuencia.
   - Listar Tareas: muestra las tareas con su índice (índice base 0).
   - Marcar Tarea como Completa: indicar el índice mostrado al listar.
   - Eliminar Tarea: indicar el índice mostrado al listar.
   - Salir: guarda automáticamente las tareas en archivo JSON.

Archivo de datos
- Las tareas se guardan en `tareas.json` en la misma carpeta del proyecto.
- El formato es JSON con tipo, título, descripción, prioridad, completada y campos adicionales según tipo.

Diseño y decisiones principales
- Clases principales:
  - Tarea: encapsula atributos (propiedades para titulo, descripcion, prioridad y estado) y define Mostrar_Datos y Marcar_Completa.
  - Tarea_Urgente: hereda de Tarea, fija prioridad alta y redefine Mostrar_Datos (polimorfismo).
  - Tarea_Recurrente: hereda de Tarea, añade atributo frecuencia y redefine Mostrar_Datos.
  - Gestor_Tareas: maneja la colección de tareas, persistencia (guardar/cargar JSON) y operaciones (agregar, eliminar, marcar).
- Principios aplicados:
  - Encapsulación: atributos protegidos con propiedades y validación en setters.
  - Herencia y polimorfismo: diferentes tipos de tareas redefinen comportamiento de presentación.
  - Persistencia: guardar_tareas / cargar_tareas serializan a JSON para conservar datos.

Notas y recomendaciones
- Las operaciones que piden índices usan índices basados en la posición de la lista (0..n-1). Validar entrada numérica antes de convertir para evitar ValueError.
- Actualmente Tarea_Urgente constructor fija prioridad=5; si se desea prioridad configurable, modificar el constructor en `Clases.py`.
- Existe una variable `Archivo_Info` en `Clases.py` no utilizada; el gestor usa el nombre de archivo pasado en el constructor.

Contacto / Soporte
- Ejecuta el programa y, si aparecen errores de entrada (ValueError / IndexError), revisar los valores ingresados o reportar el error indicando el flujo reproducible.