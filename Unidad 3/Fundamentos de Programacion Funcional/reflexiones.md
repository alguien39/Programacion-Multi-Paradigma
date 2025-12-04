# Análisis e Identificación de cada una de las funciones

1. **Calcular promedio**

La primera función es **pura**, ya que no viola ninguna de las características que podrían hacerla impura. No modifica nada fuera de sí misma ni depende de valores aleatorios o cambiantes, como el tiempo.


2. **Siguiente ID**

La segunda función es **impura**, porque utiliza una variable global, lo que implica modificar un estado externo a la función.  
Puede convertirse en una función pura si, en lugar de usar una variable global, recibe el contador como parámetro y trabaja únicamente con él.

```python
contador = 0
def siguiente_id(contador):
    contador += 1
    return f"ID-{contador}"
```

3. agregar una fecha a un registro

La tercera función es impura, ya que modifica el diccionario original y además depende de la fecha actual, la cual cambia constantemente. Esto provoca que, con la misma entrada, la salida no siempre sea la misma.

Puede transformarse en una función pura si, en lugar de obtener la fecha actual dentro de la función, la recibe como parámetro. Además, debe trabajar sobre una copia del diccionario para evitar efectos secundarios:

```python
def agregar_fecha(registro, fecha):
    copia = registro.copy()
    copia["fecha"] = fecha
    return copia
```

4. Filtrar Positivos

La cuarta función es pura, ya que no modifica la lista original, no depende de factores externos y siempre produce la misma salida para la misma entrada.

5. Mezclar lista

La quinta función es impura, pues utiliza un valor aleatorio para mezclar la lista y además modifica la lista original. La aleatoriedad implica que el resultado no será el mismo para entradas idénticas, lo cual rompe la pureza.