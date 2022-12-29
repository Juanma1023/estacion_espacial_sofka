class NaveEspacial:
    def __init__(self, tipo, nombre, pais_creacion, status, peso, combustible):
        self.tipo = tipo
        self.nombre = nombre
        self.pais_creacion = pais_creacion
        self.status = status
        self.peso = peso
        self.combustible = combustible

    def __str__(self):
        return f"Tipo de Nave: {self.tipo} \nNombre: {self.nombre} \n\\\
                Pais Origen: {self.pais_creacion} \nEstado de la Nave: {self.status} \n \\\
                Peso KG: {self.peso} \nCombustible: {self.combustible}"