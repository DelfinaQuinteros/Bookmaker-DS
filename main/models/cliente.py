from main import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Cliente: %r %r %r >' % (self.nombre, self.apellido, self.email)

    def to_json(self):
        cliente_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'email': str(self.email),
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
                       escudo=escudo,
                       email=email,
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

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_apellido(self):
        return self.__apellido

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email
"""