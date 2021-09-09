from flask_restful import Resource
from flask import request
from main.services import PartidoServices


class Apuestas(Resource):
    def get(self):
        services = PartidoServices()
        return services.obtener_partidos_no_finalizados
