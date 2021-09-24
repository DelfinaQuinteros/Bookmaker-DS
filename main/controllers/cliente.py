from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ClienteModels
from main.map import Cliente_Schema
from main.map import ClienteFiltros

cliente_schema = Cliente_Schema()


class Clientes(Resource):
    def get(self):
        filtros = request.data
        clientes = db.session.query(ClienteModels)
        filtrar_clientes = ClienteFiltros(clientes)
        for key, value in request.get_json().items():
            consulta = filtrar_clientes.aplicar_filtro(key, value)
            return cliente_schema.dump(consulta.all(), many=True)

    def post(self):
        cliente = cliente_schema.load(request.get_json())
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente_schema.dump(cliente), 201
        except:
            return '', 404


class Cliente(Resource):
    def get(self, id):
        cliente = db.session.query(ClienteModels).get_or_404(id)
        return cliente_schema.dump(cliente)

    def delete(self, id):
        cliente = db.session.query(ClienteModels).get_or_404(id)
        try:
            db.session.delete(cliente)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        cliente = db.session.query(ClienteModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente_schema.dump(cliente), 201
        except:
            return '', 404
