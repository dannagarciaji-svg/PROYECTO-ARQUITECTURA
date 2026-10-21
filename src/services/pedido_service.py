
from repositories import pedido_repository


def listar_pedidos():
    return pedido_repository.obtener_pedidos()


def registrar_pedido(id_cliente, id_suela, color, cantidad):
    if not id_cliente:
        raise ValueError("Debe seleccionar un cliente.")

    if not id_suela:
        raise ValueError("Debe seleccionar una suela.")

    if not color or not color.strip():
        raise ValueError("Debe indicar el color del pedido.")

    try:
        cantidad = int(cantidad)
        id_cliente = int(id_cliente)
        id_suela = int(id_suela)
    except (TypeError, ValueError):
        raise ValueError("Los datos del pedido no son válidos.")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    return pedido_repository.crear_pedido(
        id_cliente,
        id_suela,
        color.strip(),
        cantidad
    )


def cambiar_estado_pedido(id_pedido, nuevo_estado):
    if not id_pedido:
        raise ValueError("Debe seleccionar un pedido.")

    if nuevo_estado not in ("Pendiente", "Entregado"):
        raise ValueError("El estado seleccionado no es válido.")

    return pedido_repository.actualizar_estado(
        int(id_pedido),
        nuevo_estado
    )
