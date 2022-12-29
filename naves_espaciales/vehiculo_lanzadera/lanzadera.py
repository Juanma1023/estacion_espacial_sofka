from naves_espaciales.clase_principal import NaveEspacial


class Lanzadera(NaveEspacial):
    def __init__(self, tipo, nombre, pais_creacion, status, peso, combustible, altitud, capacidad, empuje, mision):
        super().__init__(tipo, nombre, pais_creacion, status, peso, combustible)
        self.altitud = altitud
        self.capacidad = capacidad
        self.empuje = empuje
        self.mision = mision
                
