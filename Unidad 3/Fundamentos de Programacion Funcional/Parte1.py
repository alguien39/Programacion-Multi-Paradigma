#FUN A
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

#FUN B
contador = 0
def siguiente_id():
    global contador
    contador  += 1
    return f"ID-{contador}"

#FUN C
def agregar_fecha(registro):
    from datetime import datetime
    registro['fecha'] = datetime.now().isoformat()
    return registro

#FUN D
def filtrar_positivos(numeros):
    return [n for n in numeros if n>0]

#FUN E
import random
def mezclar_lista(lista):
    random.shuffle(lista)
    return lista