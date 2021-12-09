from flask_restful import Resource
from flask import request
from .. import db
from main.map import EmpresaSchema
from main.services import EmpresaService


empresa_schema = EmpresaSchema()
empresa_service = EmpresaService()


class Empresa(Resource):
    def get(self, id):
        return empresa_schema.dump(empresa_service.obtener_empresa_por_id(id))


class Empresas(Resource):
    def post(self):
        empresa = empresa_schema.load(request.get_json())
        db.session.add(empresa)
        db.session.commit()
        return empresa_schema.dump(empresa), 201
