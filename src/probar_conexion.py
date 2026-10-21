import pyodbc
from config import CONN_STR

try:
    conexion = pyodbc.connect(CONN_STR, timeout=5)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_cliente, nombre_empresa, nit, telefono_celular
        FROM dbo.Clientes
    """)

    clientes = cursor.fetchall()

    print("Consulta ejecutada correctamente.")
    print("Cantidad de clientes:", len(clientes))

    for cliente in clientes:
        print(cliente)

    conexion.close()

except Exception as error:
    print("Error al consultar clientes:")
    print(error)