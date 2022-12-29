from naves_espaciales.nave_espacial import NaveEspacial


class NoTripulada(NaveEspacial):
    def __init__(self,tipo, nombre, pais_creacion, status, peso, combustible, empuje, velocidad, mision):
        super().__init__(tipo,nombre,pais_creacion,status, peso,combustible)
        self.empuje = empuje
        self.velocidad = velocidad
        self.mision = mision
