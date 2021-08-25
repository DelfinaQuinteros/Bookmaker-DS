from marshmallow import Schema, fields, validate, post_load
from main.models import EquipoModels


class Equipo_Schema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True)
    escudo = fields.String(required=True)
    pais = fields.String(required=True)

    @post_load
    def make_equipo(self, data, **kwargs):
        return  EquipoModels(**data)

