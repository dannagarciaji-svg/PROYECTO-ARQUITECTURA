from repositories import reporte_repository


def consultar_resumen_clientes():
    return reporte_repository.obtener_resumen_clientes()