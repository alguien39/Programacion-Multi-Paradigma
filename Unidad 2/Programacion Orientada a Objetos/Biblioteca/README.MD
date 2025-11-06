# Sistema de Gestión de Biblioteca

## Descripción
Sistema simple de gestión de biblioteca que permite administrar libros y usuarios, realizar préstamos y devoluciones, y persistir los datos.

## Estructura del Código
- `modelos.py`: Clases Libro y Usuario
- `operaciones.py`: Clase Biblioteca con lógica de operaciones
- `datos.py`: Funciones para guardar/cargar datos en JSON
- `main.py`: Programa principal con menú interactivo

Cómo ejecutar
1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar: `python main.py` (o `py main.py`).
3. Seguir las opciones del menú.

Flujo y opciones del menú
1. Agregar libro  
   - Se piden: Título, Autor, Año.  
   - El libro queda con estado "disponible".

2. Registrar usuario  
   - Se pide: Nombre.  
   - El usuario queda registrado para pedir préstamos.

3. Mostrar libros disponibles  
   - Muestra los libros cuyo estado es "disponible".

4. Prestar libro  
   - Se piden: Título del libro y Nombre del usuario.  
   - Si el libro existe y está disponible, se marca como "prestado" y se añade al usuario.

5. Devolver libro  
   - Se piden: Título del libro y Nombre del usuario.  
   - Si el usuario tiene el libro prestado, se devuelve y pasa a "disponible".

6. Guardar y salir  
   - Guarda los datos en `datos_biblioteca.json` y cierra el programa.

Notas importantes
- Los datos se persisten en `datos_biblioteca.json` en la carpeta del proyecto.  
- Introduce los datos tal cual (evitar campos vacíos). 