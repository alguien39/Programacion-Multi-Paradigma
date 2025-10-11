# Creación y Manipulación de Clases y Objetos en Python

Esta Actividad contiene una implementación básica de una clase `Libro` y un script de ejemplo para demostrar su uso.

## Estructura de Archivos

- **Clases.py**: Define la clase `Libro` con atributos y métodos para gestionar libros en una biblioteca.
- **main.py**: Script de ejemplo que instancia objetos de la clase `Libro`, utiliza sus métodos y muestra su estado.

## Clase Libro

La clase `Libro` incluye los siguientes atributos:
- `titulo`: Título del libro.
- `autor`: Autor del libro.
- `publicacon`: Año de publicación.
- `prestado`: Estado del libro (prestado o disponible).

Además, cuenta con los siguientes métodos:
- `prestar()`: Marca el libro como prestado si está disponible.
- `devolver()`: Marca el libro como disponible si estaba prestado.
- `mostrar_estado()`: Devuelve una cadena con la información y estado actual del libro.

Estos atributos y métodos fueron seleccionados para cubrir las operaciones básicas de gestión de libros en una biblioteca, siguiendo las indicaciones de la actividad.

## Funcionamiento de main.py

El archivo `main.py` demuestra cómo crear instancias de la clase `Libro`, modificar sus estados mediante los métodos `prestar` y `devolver`, y mostrar la información actual de cada libro usando el método `mostrar_estado`.

No requiere interacción del usuario; simplemente ejecuta las operaciones y muestra los resultados por consola.

## Ejemplo de Uso

Al ejecutar `main.py`, se crean tres libros, se prestan algunos, se muestra su estado y se devuelve uno de ellos, mostrando los cambios en la información de cada objeto.

Este proyecto sirve como práctica para la creación, manipulación e interacción de objetos en Python.