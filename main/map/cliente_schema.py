from marshmallow import Schema, fields, validate

class Cliente_Schema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.String(required=True)
    apellido = fields.String(required=True)
    email = fields.String(required=True, validate=validate.Email())
