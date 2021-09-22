from flask.scaffold import F
from .. import db
from main.models import PartidoModels
from .repositorio_base import Create, Read, Update, Delete


class PartidoRepositorio(Create, Read, Update, Delete):
    def __init__(self):
        self.__modelo = PartidoModels

    def find_all(self):
        objetos = db.session.query(self.__modelo).all()
        return objetos

    def find_one(self, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        return objeto

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def delete(self, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        db.session.delete(objeto)
        db.session.commit()

    def update(self, data, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        for key, value in data:
            setattr(objeto, key, value)
        db.session.add(objeto)
        db.session.commit()
        return objeto
