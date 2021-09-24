import logging
from app import app
from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import EquipoModels
from main.map import Equipo_Schema


equipo_schema = Equipo_Schema()


class Equipos(Resource):
    def get(self):
        equipo = db.session.query(EquipoModels)
        return equipo_schema.dump(equipo, many=True)

    def post(self):
        equipo = equipo_schema.load(request.get_json())
        try:
            db.session.add(equipo)
            db.session.commit()
            return equipo_schema.dump(equipo), 201
        except:
            return '', 404


class Equipo(Resource):
    def get(self, id):
        equipo = db.session.query(EquipoModels).get_or_404(id)
        app.logger.info("Equipo: %s", equipo)
        return equipo_schema.dump(equipo)

    def delete(self, id):
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
            return equipo_schema.dump(equipo), 201
        except:
            return '', 404
