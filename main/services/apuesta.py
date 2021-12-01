from .. import db
from main.models import ApuestaModel, PartidoModel
from .command import Command, Tarea
from main.map import ApuestaSchema
from flask import request


apuesta_schema = ApuestaSchema()

class ApuestaService:
    
    def agregar_apuesta(self):       
        apuesta = apuesta_schema.load(request.get_json())
        if self.registrar_apuestas(apuesta):
            db.session.add(apuesta)
            db.session.commit()
            print("DEVUELVE LA APUESTA")
            return apuesta
        return False


    def obtener_apuestas(self):
        apuestas = db.session.query(ApuestaModel).all()
        return apuestas
    

    def registrar_apuestas(self, apuesta):
        tarea = Tarea()
        # tarea.agregar(ValidarMontos())
        # tarea.agregar(GuardarApuesta())
        tarea.execute(apuesta)
        if tarea.agregar(ValidarPartido.execute(apuesta.partido)):
            pass
        else:
            return False


class ValidarPartido(Command):

    @staticmethod
    def execute(param):
        #lógica para validar apuesta del partido
        partido = db.session.query(PartidoModel).get_or_404(param)
        if partido is not None:
            return True


class ValidarMontos(Command):
    def execute(self, param):
        #lógica para validar montos de apuesta
        pass


class GuardarApuesta(Command):
    def execute(self, param):
        db.session.add(apuesta)
        db.session.commit()
        return apuesta.to_json(), 201


class EnviarMail(Command):
    def execute(self, param):
        #lógica para enviar mail de confirmación de apuesta
        pass
