from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ClienteModels
from main.map import Cliente_Schema

cliente_schema = Cliente_Schema()
class Clientes(Resource):
    def get(self):
        clientes = db.session.query(ClienteModels)
        return cliente_schema.dump(clientes, many=True)

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


