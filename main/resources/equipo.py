from flask_restful import Resource
from flask import request, jsonify
from main import db
from main.models import EquipoModels

class Equipos(Resource):
    @staticmethod
    def get():
        page = 1
        per_page = 10
        equipos = db.session.query(EquipoModels)
        if request.get_json():
            filtro = request.get_json().items()
            for key, value in filtro:
                if key == "page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        equipos = equipos.paginate(page, per_page, True, 30)
        return jsonify({'equipos': [equipos.to_json() for equipos in equipos.items],
                        'total': equipos.total,
                        'page': equipos.page,
                        'pages': equipos.pages
                        })

    def post(self):
        equipo = EquipoModels.from_json(request.get_json())
        try:
            db.session.add(equipo)
            db.session.commit()
            return equipo.to_json(), 201
        except:
            return '', 404


class Equipo(Resource):
    @staticmethod
    def get(self, id):
        equipo = db.session.query(EquipoModels).get_or_404(id)
        return empresa.to_json()

    def delete(id):
        equipo = db.session.query(EquipoModels).get_or_404(id)
        try:
            db.session.delete(equipo)
            db.session.commit()
            return '', 204
        except:
            return '', 404


    def put(self, id):
        equipo = db.session.query(EquipoModels).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(equipo, key, value)
        try:
            db.session.add(equipo)
            db.session.commit()
            return equipo.to_json(), 201
        except:
            return '', 404
