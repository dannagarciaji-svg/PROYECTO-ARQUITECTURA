
from services import cliente_service
from services import suela_service
from services import pedido_service
from services import material_service
from services import reporte_service


def obtener_datos_pagina():
    clientes = cliente_service.listar_clientes()
    suelas = suela_service.listar_suelas()
    colores = suela_service.listar_colores()
    pedidos = pedido_service.listar_pedidos()
    materiales = material_service.listar_materiales()
    reporte_clientes = reporte_service.consultar_resumen_clientes()

    pedidos_pendientes = sum(
        1 for pedido in pedidos if pedido[6] == "Pendiente"
    )

    total_referencias = len(suelas)
    total_pedidos = len(set(pedido[0] for pedido in pedidos))

    return {
        "clientes": clientes,
        "suelas": suelas,
        "colores": colores,
        "pedidos": pedidos,
        "materiales": materiales,
        "reporte_clientes": reporte_clientes,
        "kpi_por_pedidos": pedidos_pendientes,
        "kpi_total_referencias": total_referencias,
        "kpi_total_pedidos": total_pedidos,
        "kpi_modulo_reportes": len(reporte_clientes),
    }
