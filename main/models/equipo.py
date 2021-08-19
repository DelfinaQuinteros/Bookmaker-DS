from .. import db

class Equipo(db.Model):
    __tablename__ = 'equipos'
    __id = db.Column('id', db.Integer, primary_key=True)
    __nombre = db.Column('nombre', db.String(100), nullable=False)
    __escudo = db.Column('escudo', db.String(100), nullable=False)
    __pais = db.Column('pais', db.String(100), nullable=False)

    def __repr__(self):
        return '<Equipo: %r %r %r >' % (self.__nombre, self.__escudo, self.__pais)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo

    @escudo.deleter
    def escudo(self):
        del self.__escudo

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @pais.deleter
    def pais(self):
        del self.__pais


    def to_json(self):
        equipo_json = {
            'id': self.__id,
            'nombre': str(self.__nombre),
            'escudo': str(self.__escudo),
            'pais': str(self.__pais),
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

