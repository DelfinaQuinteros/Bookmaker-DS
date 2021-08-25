from marshmallow import Schema, fields, validate, post_load
from main.models import ClienteModels


class Cliente_Schema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True)
    apellido = fields.String(required=True)
    email = fields.String(required=True, validate=validate.Email())

    @post_load
    def make_cliente(self, data, **kwargs):
        return  ClienteModels(**data)

