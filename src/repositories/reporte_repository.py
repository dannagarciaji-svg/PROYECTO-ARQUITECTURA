from config import CONN_STR
import pyodbc


def obtener_resumen_clientes():
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT
                C.nombre_empresa,
                SUM(D.cantidad_pares),
                COUNT(DISTINCT P.id_pedido)
            FROM Clientes C
            LEFT JOIN Pedidos P
                ON C.id_cliente = P.id_cliente
            LEFT JOIN DetallePedidos D
                ON P.id_pedido = D.id_pedido
            GROUP BY C.nombre_empresa
        """)
        return cursor.fetchall()
    finally:
        conexion.close()