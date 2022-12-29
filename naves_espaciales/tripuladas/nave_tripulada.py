from naves_espaciales.nave_espacial import NaveEspacial

class Tripulada(NaveEspacial):
    def __init__(self, tipo, nombre, pais_creacion, status, peso, combustible, orbita,capacidad):
        super().__init__(tipo, nombre, pais_creacion, status, peso, combustible,)
        self.orbita = orbita
        self.capacidad = capacidad
