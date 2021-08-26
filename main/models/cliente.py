from .. import db
<<<<<<< HEAD
from sqlalchemy.ext.hybrid import hybrid_property


class Cliente(db.Model):
    __tablename__ = 'clientes'
    __id = db.Column('id', db.Integer, primary_key=True)
    __nombre = db.Column('nombre', db.String(100), nullable=False)
    __apellido = db.Column('apellido', db.String(100), nullable=False)
    __email = db.Column('email', db.String(120), nullable=False)
=======

class Cliente(db.Model):
    __tablename__ = 'clientes'
    __id = db.Column('id',db.Integer, primary_key=True)
    __nombre = db.Column('nombre',db.String(100), nullable=False)
    __apellido = db.Column('apellido',db.String(100), nullable=False)
    __email = db.Column('mail',db.String(120), nullable=False)
>>>>>>> 0ffbba7845137d67670098c4a015d9dcbc70648c

    def __init__(self, nombre, apellido, email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email

    def __repr__(self):
        return '<Cliente: %r %r %r >' % (self.__nombre, self.__apellido, self.__email)
<<<<<<< HEAD

    @hybrid_property
    def id(self):
        return self.__id

=======

    @property
    def id(self):
        return self.__id

>>>>>>> 0ffbba7845137d67670098c4a015d9dcbc70648c
    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

<<<<<<< HEAD
    @hybrid_property
=======
    @property
>>>>>>> 0ffbba7845137d67670098c4a015d9dcbc70648c
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

<<<<<<< HEAD
    @hybrid_property
=======
    @property
>>>>>>> 0ffbba7845137d67670098c4a015d9dcbc70648c
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @apellido.deleter
    def apellido(self):
        del self.__apellido

<<<<<<< HEAD
    @hybrid_property
=======
    @property
>>>>>>> 0ffbba7845137d67670098c4a015d9dcbc70648c
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email

