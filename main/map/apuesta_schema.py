from marshmallow import Schema, fields, validate, post_load
from main.models import ApuestaModel


class ApuestaSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha = fields.DateTime(required=False)
    monto = fields.Float(required=True)
    equipo_ganador = fields.Integer(required=True)
    partido = fields.Integer(required=True)
    cliente_id = fields.Integer(required=True)

    @post_load
    def make_apuesta(self, data, **kwargs):
        return ApuestaModel(**data)
