from .. import db

class Empresa(db.Model):
    __tablename__ = 'empresas'
    __id = db.Column('id',db.Integer, primary_key=True)
    __razon_social = db.Column('razon social',db.String(100), nullable=False)
    __email = db.Column('email',db.String(120), nullable=False)

    def __init__(self, razon_social, email):
        self.__razon_social = razon_social
        self.__email = email

    def __repr__(self):
        return '<Empresa: %r %r >' % (self.__razon_social, self.__email)

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
    def razon_social(self):
        return self.__razon_social

    @razon_social.setter
    def razon_social(self, razon_social):
        self.__razon_social = razon_social

    @razon_social.deleter
    def razon_social(self):
        del self.__razon_social

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email

