from .. import db
from sqlalchemy.ext.hybrid import hybrid_property


class Empresa(db.Model):
    __tablename__ = "empresas"
    __id = db.Column('id', db.Integer, primary_key=True)
    __razon_social = db.Column('razon_social', db.String(50), nullable=False)
    __email = db.Column('email', db.String(120), nullable=False)
    __activado = db.Column('activado', db.Boolean, nullable=False)

    def __repr__(self):
        return '<Empresa: %r %r >' % (self.__id, self.__email)

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
    def razon_social(self):
        return self.__razon_social

    @razon_social.setter
    def razon_social(self, razon_social):
        self.__razon_social = razon_social

    @razon_social.deleter
    def razon_social(self):
        del self.__razon_social

    @hybrid_property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email
        
    @hybrid_property
    def activado(self):
        return self.__activado

    @activado.setter
    def activado(self, activado):
        self.__activado = activado

    @activado.deleter
    def activado(self):
        del self.__activado
