from .. import db

class Cliente(db.Model):
    __id = db.Column('id',db.Integer, primary_key=True)
    __nombre = db.Column('nombre',db.String(100), nullable=False)
    __apellido = db.Column('apellido',db.String(100), nullable=False)
    __email = db.Column('mail',db.String(120), nullable=False)

    def __repr__(self):
        return '<Cliente: %r %r %r >' % (self.__nombre, self.__apellido, self.__email)

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
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @apellido.deleter
    def apellido(self):
        del self.__apellido

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email


    def to_json(self):
        cliente_json = {
            'id': self.__id,
            'nombre': str(self.__nombre),
            'apellido': str(self.__apellido),
            'email': str(self.__email),
        }
        return cliente_json

    @staticmethod
    def from_json(cliente_json):
        id = cliente_json.get('id')
        nombre = cliente_json.get('nombre')
        apellido = cliente_json.get('apellido')
        email = cliente_json.get('email')
        return Cliente(id=id,
                       nombre=nombre,
                       apellido=apellido,
                       email=email,
                       )
