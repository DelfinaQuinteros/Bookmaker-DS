from flask_restful import Resource
from flask import request
from main.services import ApuestaService
from main.map import ApuestaSchema
from ..repositories import ApuestaRepositorio

apuesta_schema = ApuestaSchema()
repositorio_apuesta = ApuestaRepositorio()
apuesta_service = ApuestaService()


class Apuesta(Resource):
    def get(self, id):
        return apuesta_schema.dump(repositorio_apuesta.find_one(id))


class Apuestas(Resource):
    def get(self):
        return apuesta_schema.dump(repositorio_apuesta.find_all(), many=True)

    def post(self):
        services = ApuestaService()
        apuesta = apuesta_schema.load(request.get_json())
        return services.agregar_apuesta(apuesta), services.registrar_apuestas(apuesta)
