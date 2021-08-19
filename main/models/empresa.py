from main import db

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    razon_social = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Empresa: %r %r >' % (self.razon_social, self.email)

    def to_json(self):
        empresa_json = {
            'id': self.id,
            'razon_social': str(self.razon_social),
            'email': str(self.email),
        }
        return eempresa_json

    @staticmethod
    def from_json(empresa_json):
        id = empresa_json.get('id')
        razon_social = empresa_json.get('razon_social')
        email = empresa_json.get('email')
        return Empresa(id=id,
                      razon_social=razon_social,
                      email=email,
                      )
"""   
    def __init__(self):
        pass

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_razon_social(self, razon_social):
        self.__razon_social = razon_social

    def get_razon_social(self):
        return self.__razon_social


    def set_mail(self, email):
        self.__email = email

    def get_mail(self):
        return self.__email
"""
