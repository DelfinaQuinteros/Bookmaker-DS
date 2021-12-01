from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime


class Apuesta(db.Model):
    __tablename__ = 'apuestas'
    __id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    __fecha = db.Column('fecha', db.DateTime, nullable=False, default=datetime.now())
    __monto = db.Column('monto', db.Float('equipo.id'), nullable=False)
    __equipo_ganador = db.Column('equipo_ganador', db.ForeignKey('equipos.id'), nullable=False)
    __partido = db.Column('partido', db.Integer, db.ForeignKey('partidos.id'), nullable=False)
    __cliente_id = db.Column('cliente', db.Integer, db.ForeignKey('clientes.id'), nullable=False)

    def __repr__(self):
        return '<Apuesta: %r %r %r %r %r %r>' % (self.__id, self.__fecha, self.__monto, self.__equipo_ganador, self.partido, self.cliente_id)

    @hybrid_property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @hybrid_property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @fecha.deleter
    def fecha(self):
        del self.__fecha

    @hybrid_property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, monto):
        self.__monto = monto

    @monto.deleter
    def monto(self):
        del self.__monto

    @hybrid_property
    def equipo_ganador(self):
        return self.__equipo_ganador

    @equipo_ganador.setter
    def equipo_ganador(self, equipo_ganador):
        self.__equipo_ganador = equipo_ganador

    @equipo_ganador.deleter
    def equipo_ganador(self):
        del self.__equipo_ganador

    @hybrid_property
    def partido(self):
        return self.__partido

    @partido.setter
    def partido(self, partido):
        self.__partido = partido

    @partido.deleter
    def partido(self):
        del self.__partido

    @hybrid_property
    def cliente_id(self):
        return self.__cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self.__cliente_id = cliente_id

    @cliente_id.deleter
    def cliente_id(self):
        del self.__cliente_id    

"""
    def to_json(self):
        apuesta_json = {
            'id': self.__id,
            'fecha': str(self.__fecha),
            'monto': self.__monto,
            'equipo_ganador': self.__equipo_ganador,
            'partido': self.__partido,
            'cliente_id': self.cliente_id
        }
        return apuesta_json

    @staticmethod
    def from_json(apuesta_json):
        id = apuesta_json.get('id')
        fecha = apuesta_json.get('fecha')
        monto = apuesta_json.get('monto')
        equipo_ganador = apuesta_json.get('equipo_ganador')
        partido = apuesta_json.get('partido')
        cliente_id = apuesta_json.get('cliente_id')
        return Apuesta(
            id=id,
            fecha=fecha,
            monto=monto,
            equipo_ganador=equipo_ganador,
            partido=partido,
            cliente_id=cliente_id
        )
"""        