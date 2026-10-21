from config import CONN_STR
import pyodbc


# =========================
# CONSULTAR SUELAS
# =========================

def obtener_suelas():
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_suela, referencia, talla,
                   stock_disponible, precio_unidad, color
            FROM Suelas
        """)
        return cursor.fetchall()
    finally:
        conexion.close()


# =========================
# CREAR SUELAS
# =========================

def crear_suela(referencia, talla, color, id_material, precio, stock):
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Suelas
                (referencia, talla, color, id_material,
                 precio_unidad, stock_disponible)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (referencia, talla, color, id_material, precio, stock))
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


# =========================
# ACTUALIZAR STOCK
# =========================

def actualizar_stock(id_suela, nuevo_stock):
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Suelas
            SET stock_disponible = ?
            WHERE id_suela = ?
        """, (nuevo_stock, id_suela))
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


# =========================
# GESTIÓN DE COLORES (ADAPTADA A LA TABLA SUELAS)
# =========================

def obtener_colores():
    # Extrae los colores únicos que ya están registrados en el inventario de suelas
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT DISTINCT ROW_NUMBER() OVER(ORDER BY color) AS id_color, color AS nombre_color
            FROM Suelas
        """)
        return cursor.fetchall()
    finally:
        conexion.close()


def crear_color(nombre_color):
    nombre_color = nombre_color.strip().capitalize()

    if not nombre_color:
        raise ValueError("El nombre del color no puede estar vacío.")

    # Como los colores se guardan directo en suelas, aseguramos que el color sea válido
    return True


def actualizar_color(id_color, nuevo_nombre):
    nuevo_nombre = nuevo_nombre.strip().capitalize()

    if not nuevo_nombre:
        raise ValueError("El nombre del color no puede estar vacío.")

    return True


def eliminar_color(id_color):
    return True