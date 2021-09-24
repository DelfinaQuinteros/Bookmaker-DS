from main.models import EmpresaModels
from main.repositories import EmpresaRepositorio

repositorio = EmpresaRepositorio

class EmpresaServices:
    def obtener_empresas(self):
        return repositorio.find_all()

    def obtener_empresa_id(self, id):
        return repositorio.find_one(id)
