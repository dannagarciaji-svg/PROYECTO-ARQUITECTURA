
from config import CONN_STR
import pyodbc


def obtener_clientes():
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_cliente, nombre_empresa, nit, telefono_celular
            FROM Clientes
        """)
        return cursor.fetchall()
    finally:
        conexion.close()


def crear_cliente(nombre, nit, telefono):
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            INSERT INTO Clientes (nombre_empresa, nit, telefono_celular)
            VALUES (?, ?, ?)
            """,
            (nombre, nit, telefono)
        )
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def actualizar_cliente(id_cliente, nombre, nit, telefono):
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            UPDATE Clientes
            SET nombre_empresa = ?, nit = ?, telefono_celular = ?
            WHERE id_cliente = ?
            """,
            (nombre, nit, telefono, id_cliente)
        )
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def eliminar_cliente(id_cliente):
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM Clientes WHERE id_cliente = ?",
            (id_cliente,)
        )
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
