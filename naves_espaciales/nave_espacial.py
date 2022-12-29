from naves_espaciales.funtions import limpiar
from naves_espaciales.clase_principal import NaveEspacial
from naves_espaciales.vehiculo_lanzadera.lanzadera import Lanzadera
listaNaves = []




def crear_nave():
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
    limpiar(seg=0)
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
            print(i+1, "-" , listaCombustible[i])
        print("")
        print("")
        while True:
            tipo_comb = input("Seleccione el tipo de combustible: ")
            if tipo_comb == "1":
                combustible = listaCombustible[0]
                break
            if tipo_comb == "2":
                combustible = listaCombustible[1]
                break
            if tipo_comb == "3":
                combustible = listaCombustible[2]
                break
            if tipo_comb == "4":
                combustible = listaCombustible[3]
                break
            if tipo_comb == "5":
                combustible = listaCombustible[4]
                break
        
        lanzadera = Lanzadera(tipo, nombre, pais_creacion, status, peso, combustible,altitud,capacidad,empuje,mision)
        print(lanzadera)
            
    if tipo == "No Tripulada":
        listaCombustible = ['MNH + NO4','Solido + Liquido',
                        'N2H4', 'NO4 + N2H4 + He', 'N(comp.) + N2H4','PuO2',
                        'N2O4 + UDMH', 'N2H4 + Amina', 'MMH+NO']
        print("-------------------------------------------------")
        print("Tipos de Combustible")
        print("")
        for i in range(1, len(listaCombustible)):
            print(i , "-" , listaCombustible[i-1])
        print("")
        tipo_comb = input("Seleccione el tipo de combustible: ")
        for i in range(0,len(listaCombustible)):
            while True:
                if tipo_comb == str(i):
                    combustible = listaCombustible[i]
                    break
                tipo_comb = input("Ingrese un valor correcto: ")
    
    if tipo == "Tripulada":
        listaCombustible = ['Solido','Aerozina50 + NO4', 'Queroseno + H(liq.)', 'NO + Amina','PuO2',
                        'NO4 + UDMH', 'N2H4 + UDMH', 'N2O4 + MMH']
        print("-------------------------------------------------")
        print("Tipos de Combustible")
        print("")
        for i in range(1, len(listaCombustible)):
            print(i, "-", listaCombustible[i-1])
        print("")
        tipo_comb = input("Seleccione el tipo de combustible: ")
        while True:
            for i in range(0,len(listaCombustible)):
                if tipo_comb == str(i):
                    combustible = listaCombustible[i]
                    break
            tipo_comb = input("Ingrese un valor correcto")
    crearNave = NaveEspacial(tipo, nombre, pais_creacion,status,peso, combustible)
    listaNaves.append(crearNave)
    for i in range(len(listaNaves)):
        print(listaNaves[i])

    print("REGISTRO EXITOSO")