from flask_restful import Resource
from flask import request, jsonify
from main import db
from main.models import EmpresaModels

class Empresas(Resource):
    @staticmethod
    def get():
        page = 1
        per_page = 10
        empresas = db.session.query(EmpresaModels)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        empresas = empresas.paginate(page, per_page, True, 30)
        return jsonify({'empresas': [empresa.to_json() for empresas in empresas.items],
                        'total': empresas.total,
                        'page': empresas.page,
                        'pages': empresas.pages
                        })

    def post(self):
        empresa = EmpresaModels.from_json(request.get_json())
        try:
            db.session.add(empresa )
            db.session.commit()
            return empresa.to_json(), 201
        except:
            return '', 404


class Empresa(Resource):
    @staticmethod
    def get(self, id):
        empresa = db.session.query(EmpresaModels).get_or_404(id)
        return empresa.to_json()

    def delete(id):
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
            db.session.add(empresa)
            db.session.commit()
            return empresa.to_json(), 201
        except:
            return '', 404
