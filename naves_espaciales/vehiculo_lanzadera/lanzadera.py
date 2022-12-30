from naves_espaciales.nave_espacial import NaveEspacial


class Lanzadera(NaveEspacial):
    def __init__(self, tipo, nombre, pais_creacion, status, peso, combustible, altitud, capacidad, empuje, mision):
        super().__init__(tipo, nombre, pais_creacion, status, peso, combustible)
        self.altitud = altitud
        self.capacidad = capacidad
        self.empuje = empuje
        self.mision = mision
                
    def __str__(self):
        return f"Informacion Ingresada: \n\
                Tipo de Nave: {self.tipo} \n\
                Nombre: {self.nombre} \n\
                Pais Origen: {self.pais_creacion} \n\
                Estado de la Nave: {self.status} \n\
                Peso KG: {self.peso} \n\
                Combustible: {self.combustible} \n\
                Altitud: {self.altitud} \n\
                Capacidad: {self.capacidad} \n\
                Empuje: {self.empuje} \n\
                Mision: {self.mision}"