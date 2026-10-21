from repositories import suela_repository


# =========================
# CONSULTAR SUELAS Y COLORES
# =========================

def listar_suelas():
    return suela_repository.obtener_suelas()


def listar_colores():
    return suela_repository.obtener_colores()


# =========================
# REGISTRAR SUELAS
# =========================

def registrar_suela(referencia, talla, color, id_material, precio, stock):
    if not referencia or not referencia.strip():
        raise ValueError("La referencia es obligatoria.")

    if not color or not color.strip():
        raise ValueError("El color es obligatorio.")

    try:
        talla = int(talla)
        id_material = int(id_material)
        precio = float(precio)
        stock = int(stock)
    except (TypeError, ValueError):
        raise ValueError(
            "La talla, el material, el precio y el stock deben ser válidos."
        )

    if talla <= 0:
        raise ValueError("La talla debe ser mayor que cero.")

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    if stock < 0:
        raise ValueError("El stock no puede ser negativo.")

    return suela_repository.crear_suela(
        referencia.strip(),
        talla,
        color.strip(),
        id_material,
        precio,
        stock
    )


# =========================
# ACTUALIZAR STOCK
# =========================

def modificar_stock(id_suela, nuevo_stock):
    try:
        id_suela = int(id_suela)
        nuevo_stock = int(nuevo_stock)
    except (TypeError, ValueError):
        raise ValueError("El identificador y el stock deben ser válidos.")

    if nuevo_stock < 0:
        raise ValueError("El stock no puede ser negativo.")

    return suela_repository.actualizar_stock(id_suela, nuevo_stock)


# =========================
# CRUD DE COLORES
# =========================

def registrar_color(nombre_color):
    if not nombre_color or not nombre_color.strip():
        raise ValueError("El nombre del color es obligatorio.")

    return suela_repository.crear_color(nombre_color)


def modificar_color(id_color, nuevo_nombre):
    try:
        id_color = int(id_color)
    except (TypeError, ValueError):
        raise ValueError("El identificador del color no es válido.")

    if not nuevo_nombre or not nuevo_nombre.strip():
        raise ValueError("El nombre del color es obligatorio.")

    return suela_repository.actualizar_color(id_color, nuevo_nombre)


def borrar_color(id_color):
    try:
        id_color = int(id_color)
    except (TypeError, ValueError):
        raise ValueError("El identificador del color no es válido.")

    return suela_repository.eliminar_color(id_color)