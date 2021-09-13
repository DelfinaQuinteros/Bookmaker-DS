from .. import db
from main.models import PartidoModels

repositorio = Repositorio(PartidoModels)
class PartidoServices:
    def obtener_partidos_no_finalizados(self):
        partidos = db.session.query(PartidoModels).filter('finalizado' == False).all()
        return partidos

    def obtener_partidos(self):
        return repositorio.obtener_todos()