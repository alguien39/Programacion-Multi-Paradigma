import os
import random

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def generar_codigo_tiket():
    return "".join(str(random.randint(0, 9)) for _ in range(10))

def confirmar_accion():
    pregunta= "¿Confirmar? (s/N): "
    r = input(pregunta).strip().lower()
    return r == "s"