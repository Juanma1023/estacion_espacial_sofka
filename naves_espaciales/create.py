from naves_espaciales.funtions import limpiar
from naves_espaciales.vehiculo_lanzadera.lanzadera import Lanzadera
from naves_espaciales.no_tripuladas.nave_no_tripulada import NoTripulada
from naves_espaciales.tripuladas.nave_tripulada import Tripulada

import sys
import json

class Json():
    json_file = {}
    def read(self):
        with open("naves_espaciales\\naves_registradas\\naves.json") as file:
            self.json_file = json.load(file)
            print(self.json_file)

    def write(self):
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
                    tipo = 'Lanzadera'
                    break
                if tipo_nave == 'N':
                    tipo = 'No Tripulada'
                    break
                if tipo_nave == 'T':
                    tipo = 'Tripulada'
                    break
            limpiar(seg=0)
            print("-------------------------------------------------")
            nombre = input("Ingrese el nombre de la nave: ")
            pais_creacion = input("Ingrese el pais de origen: ")
            limpiar(seg=0)
            print("-------------------------------------------------")
            print("Estado Actual de la nave: ")
            print("")
            print("1 - Actualmente funcionando")
            print("2 - Destruida")
            print("3 - Retirada")
            print("")
            while True:
                status = input("Ingrese el estado actual de la nave: ")
                if status == "1":
                    status = "Actualmente funcionando"
                    break
                if status == "2":
                    status = "Destruida"
                    break
                if status == "3":
                    status = "Retirada"
                    break
                
            limpiar(seg=0)
            peso = input("Ingrese el peso de la nave en toneladas: ")
            
            if tipo == "Lanzadera":
                altitud= input("Ingrese la altitud de la nave: ")
                capacidad = input("Ingrese la capacidad de la nave en Toneladas: ")
                empuje = input("Ingrese el empuje de la nave en Toneladas: ")
                mision = input("Ingrese la mision de la nave: ")
                listaCombustible = ['H(liq.)+O(liq.)','Solido + Queroseno + N(liq.)',
                                'Queroseno + N(liq.)', 'C2H8N2 + NO', 'UDMH + N2O4']
                print("-------------------------------------------------")
                print("Tipos de Combustible")
                print("")
                for i in range(0, len(listaCombustible)):
                    print(i+1, "-", listaCombustible[i])
                print("")
                tipo_comb = input("Seleccione el tipo de combustible: ")
                combustible = None
                while True:
                    for i in range(0,len(listaCombustible)):
                        if int(tipo_comb) == i:
                            combustible = listaCombustible[i-1]
                            print(combustible)
                            break
                    if combustible is not None:
                        break
                    else:
                        tipo_comb = input("Seleccione una opcion correcta: ")

                lanzadera = Lanzadera(tipo, nombre, pais_creacion, status, peso, combustible,altitud,capacidad,empuje,mision)
                lanzadera_datos = {
                    "Tipo": lanzadera.tipo,
                    "Nombre": lanzadera.nombre,
                    "Pais": lanzadera.pais_creacion,
                    "Estado": lanzadera.status,
                    "Peso (Kg)": lanzadera.peso,
                    "Combustible": lanzadera.combustible,
                    "Altitud": lanzadera.altitud,
                    "Capacidad": lanzadera.capacidad,
                    "Empuje": lanzadera.empuje,
                    "Mision": lanzadera.mision
                }
            
                self.json_file["lanzadera"].append(lanzadera_datos)
                with open("naves_espaciales\\naves_registradas\\naves.json","w") as file:
                    json.dump(self.json_file, file)

                    
            if tipo == "No Tripulada":
                empuje = input("Ingrese el empuje de la nave en Toneladas: ")
                velocidad  = input("Ingrese la velocidad en que viaja la nave en Km/h: ")
                mision = input("Ingrese la mision de la nave: ")

                listaCombustible = ['MNH + NO4','Solido + Liquido',
                                'N2H4', 'NO4 + N2H4 + He', 'N(comp.) + N2H4','PuO2',
                                'N2O4 + UDMH', 'N2H4 + Amina', 'MMH+NO']
                print("-------------------------------------------------")
                print("Tipos de Combustible")
                print("")
                for i in range(0, len(listaCombustible)):
                    print(i+1, "-", listaCombustible[i])
                print("")
                tipo_comb = input("Seleccione el tipo de combustible: ")
                combustible = None
                while True:
                    for i in range(0,len(listaCombustible)):
                        if int(tipo_comb) == i:
                            combustible = listaCombustible[i-1]
                            print(combustible)
                            break
                    if combustible is not None:
                        break
                    else:
                        tipo_comb = input("Seleccione una opcion correcta: ")

                no_tripulada = NoTripulada(tipo, nombre, pais_creacion, status, peso, combustible,empuje,velocidad,mision)
                noTripulada_datos = {
                    "Tipo": no_tripulada.tipo,
                    "Nombre": no_tripulada.nombre,
                    "Pais": no_tripulada.pais_creacion,
                    "Estado": no_tripulada.status,
                    "Peso (Kg)": no_tripulada.peso,
                    "Combustible": no_tripulada.combustible,
                    'Empuje': no_tripulada.empuje,
                    'Velocidad': no_tripulada.velocidad,
                    'Mision': no_tripulada.mision
                }
            
                self.json_file['noTripulada'].append(noTripulada_datos)
                with open("naves_espaciales\\naves_registradas\\naves.json","w") as file:
                    json.dump(self.json_file, file)
                
            if tipo == "Tripulada":
                orbita = input("Ingrese la orbita en Km: ")
                capacidad  = input("Ingrese la capacidad de personas que puede tenerla nave: ")

                listaCombustible = ['Solido','Aerozina50 + NO4', 'Queroseno + H(liq.)', 'NO + Amina','PuO2',
                                'NO4 + UDMH', 'N2H4 + UDMH', 'N2O4 + MMH']
                print("-------------------------------------------------")
                print("Tipos de Combustible")
                for i in range(0, len(listaCombustible)):
                    print(i+1, "-", listaCombustible[i])
                print("")
                tipo_comb = input("Seleccione el tipo de combustible: ")
                combustible = None
                while True:
                    for i in range(0,len(listaCombustible)):
                        if int(tipo_comb) == i:
                            combustible = listaCombustible[i-1]
                            print(combustible)
                            break
                    if combustible is not None:
                        break
                    else:
                        tipo_comb = input("Seleccione una opcion correcta: ")

                tripulada = Tripulada(tipo, nombre, pais_creacion, status, peso, combustible,orbita,capacidad)
                tripulada_datos = {
                    "Tipo": tripulada.tipo,
                    "Nombre": tripulada.nombre,
                    "Pais": tripulada.pais_creacion,
                    "Estado": tripulada.status,
                    "Peso (Kg)": tripulada.peso,
                    "Combustible": tripulada.combustible,
                    "Orbita": tripulada.orbita,
                    "Capacidad": tripulada.capacidad
                }
            
                self.json_file["tripulada"].append(tripulada_datos)
                with open("naves_espaciales\\naves_registradas\\naves.json","w") as file:
                    json.dump(self.json_file, file)

                
                
            print("\n")
            print("REGISTRO EXITOSO")
            limpiar(seg=3)

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





'''
def consulta_simple():
    print("-------------------------------------------------")
    print("1 - Consultar Tipo de Nave")
    print("2 - Consultar todas las naves registradas")
    print("")
    msg = input("Ingrese la opcion deseada: ")
    while True:
        if msg == "1":
            print("Lanzadera")
            print("No Tripulada")
            print("ripulada")
            break
        if msg == "2":
            for i in range(len(listaNaves)):
                print(listaNaves[i])
            break
        else:
            msg = input("Ingrese una opcion correcta: ")
'''
        
