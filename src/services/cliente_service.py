
from repositories import cliente_repository


def listar_clientes():
    return cliente_repository.obtener_clientes()


def registrar_cliente(nombre, nit, telefono):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre de la empresa es obligatorio.")

    if not nit or not nit.strip():
        raise ValueError("El NIT es obligatorio.")

    if not telefono or not telefono.strip():
        raise ValueError("El teléfono es obligatorio.")

    cliente_repository.crear_cliente(
        nombre.strip(),
        nit.strip(),
        telefono.strip()
    )


def modificar_cliente(id_cliente, nombre, nit, telefono):
    if not id_cliente:
        raise ValueError("Debe seleccionar un cliente.")

    if not nombre or not nombre.strip():
        raise ValueError("El nombre de la empresa es obligatorio.")

    if not nit or not nit.strip():
        raise ValueError("El NIT es obligatorio.")

    if not telefono or not telefono.strip():
        raise ValueError("El teléfono es obligatorio.")

    cliente_repository.actualizar_cliente(
        id_cliente,
        nombre.strip(),
        nit.strip(),
        telefono.strip()
    )


def borrar_cliente(id_cliente):
    if not id_cliente:
        raise ValueError("Debe seleccionar un cliente.")

    cliente_repository.eliminar_cliente(id_cliente)
