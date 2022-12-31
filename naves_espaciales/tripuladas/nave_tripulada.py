from naves_espaciales.nave_espacial import NaveEspacial

class Tripulada(NaveEspacial):
    def __init__(self, tipo, nombre, pais_creacion, status, peso, combustible, orbita,capacidad):
        super().__init__(tipo, nombre, pais_creacion, status, peso, combustible,)
        self.orbita = orbita
        self.capacidad = capacidad
    
    def __str__(self):
        return f"\n\
                Tipo de Nave: {self.tipo} \n\
                Nombre: {self.nombre} \n\
                Pais Origen: {self.pais_creacion} \n\
                Estado de la Nave: {self.status} \n\
                Peso KG: {self.peso} \n\
                Combustible: {self.combustible} \n\
                Orbita: {self.orbita} \n\
                Capacidad: {self.capacidad}"
