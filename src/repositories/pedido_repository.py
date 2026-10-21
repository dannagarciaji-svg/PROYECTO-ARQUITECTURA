
from config import CONN_STR
import pyodbc


def obtener_pedidos():
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT P.id_pedido,
                   CONVERT(VARCHAR, P.fecha_pedido, 103),
                   C.nombre_empresa,
                   S.referencia,
                   D.cantidad_pares,
                   D.color_pedido,
                   P.estado
            FROM Pedidos P
            INNER JOIN Clientes C ON P.id_cliente = C.id_cliente
            INNER JOIN DetallePedidos D ON P.id_pedido = D.id_pedido
            INNER JOIN Suelas S ON D.id_suela = S.id_suela
            ORDER BY P.id_pedido DESC
        """)
        return cursor.fetchall()
    finally:
        conexion.close()


def crear_pedido(id_cliente, id_suela, color, cantidad):
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT stock_disponible FROM Suelas WHERE id_suela = ?",
            (id_suela,)
        )
        resultado = cursor.fetchone()

        if resultado is None:
            raise ValueError("La suela seleccionada no existe.")

        stock_actual = resultado[0]

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if stock_actual < cantidad:
            raise ValueError(
                f"Stock insuficiente. Solo quedan {stock_actual} pares."
            )

        cursor.execute(
            """
            UPDATE Suelas
            SET stock_disponible = stock_disponible - ?
            WHERE id_suela = ? AND stock_disponible >= ?
            """,
            (cantidad, id_suela, cantidad)
        )

        if cursor.rowcount != 1:
            raise ValueError("No se pudo descontar el stock disponible.")

        cursor.execute(
            """
            INSERT INTO Pedidos (id_cliente, estado)
            OUTPUT INSERTED.id_pedido
            VALUES (?, 'Pendiente')
            """,
            (id_cliente,)
        )
        id_nuevo_pedido = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO DetallePedidos
                (id_pedido, id_suela, cantidad_pares, color_pedido)
            VALUES (?, ?, ?, ?)
            """,
            (id_nuevo_pedido, id_suela, cantidad, color)
        )

        conexion.commit()
        return id_nuevo_pedido

    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def actualizar_estado(id_pedido, nuevo_estado):
    conexion = pyodbc.connect(CONN_STR)
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE Pedidos SET estado = ? WHERE id_pedido = ?",
            (nuevo_estado, id_pedido)
        )
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
