from main.models import EmpresaModels
from main.repositories import Repositorio

repositorio = Repositorio(EmpresaModels)
class EmpresaServices:
    def obtener_empresas(self):
        return repositorio.obtener_todos()
