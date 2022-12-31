from naves_espaciales.funtions import limpiar

import json
import sys

def read(nave):
    with open("naves_espaciales\\naves_registradas\\naves.json") as file:
        json_file = json.load(file)
        print(json_file[nave])


def consulta_simple():
    limpiar(seg=0)
    print ("-------------------------------------------------------")
    print ("Por el momento solo poseemos la consulta por tipo de nave")
    print ("-------------------------------------------------------")
    print ("Al señalar el tipo de nave, te mostrara las naves de este tipo")
    msg = input("Consultar tipo de nave (Si/No): ")
    if msg.lower() == "si":
        limpiar(seg=0)
        print("-------------------------------------------------")
        print("Tipo de Nave Espacial")
        print("")
        print("L - Lanzadera")
        print("N - No Tripulada")
        print("T - Tripulada")
        print("")
        while True:
            tipo_nave = input("Seleccione el tipo de Nave Espacial: ")
            if tipo_nave == 'L':
                tipo = "lanzadera"
                limpiar(seg=0)
                read(tipo)
                break
            if tipo_nave == 'N':
                tipo = "noTripulada"
                limpiar(seg=0)
                read(tipo)
                break
            if tipo_nave == 'T':
                tipo = "tripulada"
                limpiar(seg=0)
                read(tipo)
                break
    elif msg.lower() == "no":
        print("Gracias")
    print("")
    print("Desea regresar al menú")
    msg = input("Si / No:  ")
    while True:
        if msg.lower() == "no":
            print("Saliendo...")
            limpiar(seg = 3)
            sys.exit()
        elif msg.lower() == "si":
            None
            limpiar(seg = 0)
            break
        else:
            msg = input("Ingrese Si / No si desea regresar al menú")


def read_comp(nave,nombre):
    with open("naves_espaciales\\naves_registradas\\naves.json") as file:
        json_file = json.load(file)
        for data in json_file[nave]:
            if data["Nombre"] == nombre:
                print(data)
    
def consulta_avanzada():
    limpiar(seg=0)
    print ("----------------------------------------------------------------------------")
    print ("Por el momento solo poseemos la consulta por tipo de nave y su nombre")
    print ("----------------------------------------------------------------------------")
    msg = input("Desea consultar(Si/No): ")
    if msg.lower() == "si":
        limpiar(seg=0)
        print("-------------------------------------------------")
        print("Tipo de Nave Espacial")
        print("")
        print("L - Lanzadera")
        print("N - No Tripulada")
        print("T - Tripulada")
        print("")
        while True:
            tipo_nave = input("Seleccione el tipo de Nave Espacial: ")
            nombre = input("Digite el nombre de la nave: ")
            if tipo_nave == 'L':
                tipo = "lanzadera"
                limpiar(seg=0)
                read_comp(tipo, nombre)
                break
            if tipo_nave == 'N':
                tipo = "noTripulada"
                limpiar(seg=0)
                read_comp(tipo, nombre)
                break
            if tipo_nave == 'T':
                tipo = "tripulada"
                limpiar(seg=0)
                read_comp(tipo, nombre)
                break
    elif msg.lower() == "no":
        print("Gracias")
    print("")
    print("Desea regresar al menú")
    msg = input("Si / No:  ")
    while True:
        if msg.lower() == "no":
            print("Saliendo...")
            limpiar(seg = 3)
            sys.exit()
        elif msg.lower() == "si":
            None
            limpiar(seg = 0)
            break
        else:
            msg = input("Ingrese Si / No si desea regresar al menú")
