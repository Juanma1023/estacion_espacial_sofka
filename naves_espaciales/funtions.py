import os
import time
import platform

def limpiar(seg):
    """
    Borra la pantalla después de un número específico de segundos
    :param segundos: El número de segundos a esperar antes de borrar la pantalla (optional)
    """
    sistema = platform.system()
    time.sleep(seg)
    if sistema == "Windows":
        os.system('cls')