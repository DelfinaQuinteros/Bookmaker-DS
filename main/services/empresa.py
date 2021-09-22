from main.models import EmpresaModels
from main.repositories import EmpresaRepositorio

repositorio = EmpresaRepositorio

class EmpresaServices:
    def obtener_empresas(self):
        return repositorio.obtener_todos()

    def obtener_empresa_id(self):
        return repositorio.obtener_por_id(id)
