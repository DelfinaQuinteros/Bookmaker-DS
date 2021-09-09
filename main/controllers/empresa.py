from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import EmpresaModels
from main.map import Empresa_Schema
from main.services import EmpresaServices

empresa_schema = Empresa_Schema()
empresa_services = EmpresaServices()

class Empresas(Resource):
    def get(self):
        return empresa_service.dump(empresa_services.obtener_empresas(), many=True)

    def post(self):
        empresas = empresa_schema.load(request.get_json())
        try:
            db.session.add(empresas)
            db.session.commit()
            return empresa_schema.dump(empresas), 201
        except:
            return '', 404


class Empresa(Resource):
    def get(self, id):
        empresa = db.session.query(EmpresaModels).get_or_404(id)
        return empresa_schema.dump(empresa)

    def delete(self, id):
        empresa = db.session.query(EmpresaModels).get_or_404(id)
        try:
            db.session.delete(empresa)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        empresa = db.session.query(EmpresaModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(empresa, key, value)
        try:
            db.session.add(cliente)
            db.session.commit()
            return empresa_schema .dump(empresa), 201
        except:
            return '', 404

