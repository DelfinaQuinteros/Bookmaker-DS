from flask_restful import Resource
from flask import request
from main.services import PartidoService, ApuestaService
from main.models import ApuestaModel
from .. import db
from main.map import ApuestaSchema

apuesta_schema = ApuestaSchema()

class Apuestas(Resource):
    def get(self):
        services = ApuestaService()
        return apuesta_schema.dump(services.obtener_apuestas(), many=True)

    def post(self):
        services = ApuestaService()
        apuesta = services.agregar_apuesta()
        if apuesta:
            return apuesta_schema.dump(apuesta)
        return '', 404

