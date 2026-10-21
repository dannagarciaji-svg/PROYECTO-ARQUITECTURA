
from config import CONN_STR
import pyodbc


def obtener_materiales():
    conexion = pyodbc.connect(CONN_STR)

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_material, tipo_material
            FROM dbo.Materiales
            ORDER BY id_material
        """)

        materiales = cursor.fetchall()
        return materiales

    finally:
        conexion.close()
