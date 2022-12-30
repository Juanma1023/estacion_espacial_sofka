from naves_espaciales.nave_espacial import NaveEspacial


class NoTripulada(NaveEspacial):
    def __init__(self,tipo, nombre, pais_creacion, status, peso, combustible, empuje, velocidad, mision):
        super().__init__(tipo,nombre,pais_creacion,status, peso,combustible)
        self.empuje = empuje
        self.velocidad = velocidad
        self.mision = mision

    def __str__(self):
        return f"Informacion Ingresada: \n\
                Tipo de Nave: {self.tipo} \n\
                Nombre: {self.nombre} \n\
                Pais Origen: {self.pais_creacion} \n\
                Estado de la Nave: {self.status} \n\
                Peso KG: {self.peso} \n\
                Combustible: {self.combustible} \n\
                Empuje (Ton): {self.empuje} \n\
                Velocidad: {self.velocidad} \n\
                Mision: {self.mision}"