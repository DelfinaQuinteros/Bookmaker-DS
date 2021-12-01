from .. import db
from main.models import PartidoModel
from main.repositories import PartidoRepositorio

repositorio = PartidoRepositorio()


class PartidoServices:
    def obtener_partidos_no_finalizados(self):
        partidos = db.session.query(PartidoModel).filter('finalizado' == False).all()
        return partidos

    def obtener_partidos(self):
        return repositorio.find_all()
