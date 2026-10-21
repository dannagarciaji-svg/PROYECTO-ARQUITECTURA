from repositories import material_repository


def listar_materiales():
    return material_repository.obtener_materiales()