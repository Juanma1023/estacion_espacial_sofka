
from naves_espaciales.create import Json
from naves_espaciales.funtions import limpiar
from naves_espaciales.consultas import consulta_simple, consulta_avanzada

import sys


if __name__ == "__main__":
    limpiar(seg=0)
    listaNaves = []
    opcion = ''
    while opcion != 'X':
        print("----------------NAVES ESPACIALES ----------------")
        print("-------------------------------------------------")
        print("Opciones")
        print("")
        print("1 - Crear nueva Nave Espacial")
        print("2 - Consulta Simple")
        print("3 - Consulta Avanzada")
        print("X - Salir")
        print("")

        opcion = input("Digite la opcion deseada: ")
        if opcion == "1":
            limpiar(seg=0)
            objeto = Json()
            objeto.read()
            objeto.write()
        if opcion == "2":
            objeto = Json()
            objeto.read()
            consulta_simple()
        if opcion == "3":
            objeto = Json()
            objeto.read()
            consulta_avanzada()

        if opcion == 'X':
            print("Saliendo...")
            limpiar(seg = 2)
            sys.exit()
