from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime


class Apuesta(db.Model):
    __tablename__ = 'apuestas'
    __id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    __fecha = db.Column('fecha', db.DateTime, nullable=False, default=datetime.now())
    __monto = db.Column('monto', db.Float('equipo.id'), nullable=False)
    __equipo_ganador_id = db.Column('equipo_ganador_id', db.ForeignKey('equipos.id'), nullable=False)
    __partido = db.Column('partido', db.Integer, db.ForeignKey('partidos.id'), nullable=False)
    __cliente_id = db.Column('cliente', db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    equipo_ganador = db.relationship('Equipo', back_populates='apuestas')

    def __repr__(self):
        return '<Apuesta: %r %r %r %r %r %r>' % (
            self.__id, self.__fecha, self.__monto, self.__equipo_ganador, self.__partido, self.__cliente_id)

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
    def equipo_ganador_id(self):
        return self.__equipo_ganador_id

    @equipo_ganador_id.setter
    def equipo_ganador_id(self, equipo_ganador_id):
        self.__equipo_ganador_id = equipo_ganador_id

    @equipo_ganador_id.deleter
    def equipo_ganador_id(self):
        del self.__equipo_ganador_id

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
