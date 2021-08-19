from main import db

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    escudo = db.Column(db.String(100), nullable=False)
    pais = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Equipo: %r %r %r >' % (self.nombre, self.escudo, self.pais)

    def to_json(self):
        equipo_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'escudo': str(self.escudo),
            'pais': str(self.pais),
        }
        return equipo_json

    @staticmethod
    def from_json(equipo_json):
        id = equipo_json.get('id')
        nombre = equipo_json.get('nombre')
        escudo = equipo_json.get('escudo')
        pais = equipo_json.get('pais')
        return Equipo(id=id,
                       nombre=nombre,
                       escudo=escudo,
                       pais=pais,
                       )

"""
    def __init__(self):
        pass
    
    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_escudo(self, escudo):
        self.__escudo = escudo

    def get_escudo(self):
        return self.__escudo

    def set_pais(self, pais):
        self.__pais = pais

    def get_pais(self):
        return self.__pais
"""
