from flask import Flask, render_template, request, redirect, flash, url_for
import pyodbc

app = Flask(__name__)
# Llave obligatoria en Flask para poder usar mensajes flash de éxito/error
app.secret_key = "fabrica_suelas_secreta_2026"

# CADENA DE CONEXIÓN A TU SQL SERVER (Configurada para tu instancia DAVIDP\SQLEXPRESS)
CONN_STR = "Driver={ODBC Driver 17 for SQL Server};Server=DAVIDP\\SQLEXPRESS;Database=FabricaSuelas;Trusted_Connection=yes;"

def obtener_conexion():
    try:
        return pyodbc.connect(CONN_STR)
    except Exception as e:
        print(f"❌ Error crítico de conexión a SQL Server: {e}")
        return None

# 1. RUTA PRINCIPAL: Redirige automáticamente a la sección de clientes
@app.route("/")
def home():
    return redirect("/seccion/clientes")

# 2. RUTA DINÁMICA: Procesamiento de las pestañas y los contadores en tiempo real
@app.route("/seccion/<nombre_seccion>")
def mostrar_seccion(nombre_seccion):
    cn = obtener_conexion()
    if not cn:
        return "<h3>Error de Conexión: No se pudo conectar a SQL Server. Verifica que tu base de datos esté activa.</h3>"
    
    cr = cn.cursor()
    
    # Inicializamos las listas vacías para que el HTML no falle
    pedidos, suelas, clientes, materiales, reporte_pares = [], [], [], [], []
    
    # Inicializamos los contadores reales de las tarjetas en 0
    kpi_por_pedidos = 0
    kpi_total_referencias = 0
    kpi_total_pedidos = 0
    kpi_modulo_reportes = 0
    
    try:
        # ========================================================
        #  CONSULTAS REALES PARA LAS TARJETAS MORADAS (KPIs)
        # ========================================================
        cr.execute("SELECT COUNT(*) FROM Pedidos WHERE estado = 'Pendiente'")
        kpi_por_pedidos = cr.fetchone()[0] or 0

        cr.execute("SELECT COUNT(*) FROM Suelas")
        kpi_total_referencias = cr.fetchone()[0] or 0

        cr.execute("SELECT COUNT(*) FROM Pedidos")
        kpi_total_pedidos = cr.fetchone()[0] or 0

        cr.execute("SELECT COUNT(DISTINCT id_cliente) FROM Pedidos")
        kpi_modulo_reportes = cr.fetchone()[0] or 0
        
        # ========================================================
        #  CARGA DE CATÁLOGOS BÁSICOS
        # ========================================================
        cr.execute("SELECT id_cliente, nombre_empresa, nit, telefono_celular FROM Clientes")
        clientes = cr.fetchall()
        
        cr.execute("SELECT id_suela, referencia, talla, stock_disponible, precio_unidad FROM Suelas")
        suelas = cr.fetchall()
        
        cr.execute("SELECT id_material, tipo_material FROM Materiales")
        materiales = cr.fetchall()

        # Filtrar consultas pesadas según la sección activa
        if nombre_seccion == "pedidos":
            q_pedidos = """
                SELECT P.id_pedido, CONVERT(VARCHAR, P.fecha_pedido, 103), C.nombre_empresa, 
                       S.referencia, D.cantidad_pares, D.color_pedido, P.estado
                FROM Pedidos P 
                INNER JOIN Clientes C ON P.id_cliente = C.id_cliente
                INNER JOIN DetallePedidos D ON P.id_pedido = D.id_pedido 
                INNER JOIN Suelas S ON D.id_suela = S.id_suela
                ORDER BY P.id_pedido DESC
            """
            cr.execute(q_pedidos)
            pedidos = cr.fetchall()
            
        elif nombre_seccion == "reportes":
            q_reporte = """
                SELECT C.nombre_empresa, SUM(D.cantidad_pares), COUNT(P.id_pedido)
                FROM Clientes C
                LEFT JOIN Pedidos P ON C.id_cliente = P.id_cliente
                LEFT JOIN DetallePedidos D ON P.id_pedido = D.id_pedido
                GROUP BY C.nombre_empresa
            """
            cr.execute(q_reporte)
            reporte_pares = cr.fetchall()

    except Exception as e:
        print(f"Error ejecutando consultas SQL: {e}")
    finally:
        cn.close()
        
    return render_template("index.html", 
                           seccion=nombre_seccion, 
                           pedidos=pedidos, 
                           suelas=suelas, 
                           clientes=clientes, 
                           materiales=materiales,
                           reporte_pares=reporte_pares,
                           kpi_por_pedidos=kpi_por_pedidos,
                           kpi_total_referencias=kpi_total_referencias,
                           kpi_total_pedidos=kpi_total_pedidos,
                           kpi_modulo_reportes=kpi_modulo_reportes)

# ========================================================
# OPERACIONES CRUD (PROCESAMIENTO DE FORMULARIOS)
# ========================================================

@app.route("/crear_pedido", methods=["POST"])
def crear_pedido():
    id_cliente = request.form.get("id_cliente")
    id_suela = request.form.get("id_suela")
    color = request.form.get("color")
    cantidad = int(request.form.get("cantidad"))
    
    cn = obtener_conexion()
    cr = cn.cursor()
    try:
        cr.execute("SELECT stock_disponible FROM Suelas WHERE id_suela = ?", (id_suela,))
        stock_actual = cr.fetchone()[0]
        
        if stock_actual < cantidad:
            flash(f"⚠️ Stock insuficiente. Solo quedan {stock_actual} pares.", "error")
            return redirect("/seccion/pedidos")
            
        cr.execute("UPDATE Suelas SET stock_disponible = ? WHERE id_suela = ?", (stock_actual - cantidad, id_suela))
        cr.execute("INSERT INTO Pedidos (id_cliente, estado) OUTPUT INSERTED.id_pedido VALUES (?, 'Pendiente')", (id_cliente,))
        id_nuevo_pedido = cr.fetchone()[0]
        
        cr.execute("INSERT INTO DetallePedidos (id_pedido, id_suela, cantidad_pares, color_pedido) VALUES (?,?,?,?)", 
                   (id_nuevo_pedido, id_suela, cantidad, color))
        cn.commit()
        flash(f"¡Éxito! Pedido #{id_nuevo_pedido} creado correctamente.", "success")
    except Exception as e:
        flash(f"Error en SQL Server: {e}", "error")
    finally:
        cn.close()
    return redirect("/seccion/pedidos")

@app.route("/crear_suela", methods=["POST"])
def crear_suela():
    ref = request.form.get("referencia")
    talla = request.form.get("talla")
    color = request.form.get("color")
    id_mat = request.form.get("id_material")
    precio = request.form.get("precio")
    stock = request.form.get("stock")
    
    cn = obtener_conexion()
    cr = cn.cursor()
    try:
        cr.execute("INSERT INTO Suelas (referencia, talla, color, id_material, precio_unidad, stock_disponible) VALUES (?,?,?,?,?,?)",
                   (ref, talla, color, id_mat, precio, stock))
        cn.commit()
        flash("Suela agregada exitosamente al catálogo.", "success")
    except Exception as e:
        flash(f"Error al insertar producto: {e}", "error")
    finally:
        cn.close()
    return redirect("/seccion/suelas")

@app.route("/crear_cliente", methods=["POST"])
def crear_cliente():
    nombre = request.form.get("nombre")
    nit = request.form.get("nit")
    tel = request.form.get("telefono")
    
    cn = obtener_conexion()
    cr = cn.cursor()
    try:
        cr.execute("INSERT INTO Clientes (nombre_empresa, nit, telefono_celular) VALUES (?,?,?)", (nombre, nit, tel))
        cn.commit()
        flash("Cliente corporativo registrado.", "success")
    except Exception as e:
        flash(f"Error al guardar cliente: {e}", "error")
    finally:
        cn.close()
    return redirect("/seccion/clientes")

# ACTUALIZAR STOCK DINÁMICO DESDE LA URL (Acepta /actualizar_stock/ID)
@app.route("/actualizar_stock/<int:id_suela>", methods=["POST"])
def actualizar_stock_individual(id_suela):
    nuevo_stock = request.form.get("nuevo_stock")
    cn = obtener_conexion()
    if not cn:
        return redirect("/seccion/suelas")
    cr = cn.cursor()
    try:
        cr.execute("UPDATE Suelas SET stock_disponible = ? WHERE id_suela = ?", (nuevo_stock, id_suela))
        cn.commit()
        flash("Inventario actualizado con éxito.", "success")
    except Exception as e:
        flash(f"Error al cambiar stock: {e}", "error")
    finally:
        cn.close()
    return redirect("/seccion/suelas")

# ACTUALIZAR ESTADO DEL PEDIDO (Maneja el select dinámico)
@app.route("/actualizar_estado_pedido", methods=["POST"])
def actualizar_estado_pedido():
    id_pedido = request.form.get("id_pedido")
    nuevo_estado = request.form.get("estado")
    cn = obtener_conexion()
    if not cn:
        return redirect("/seccion/pedidos")
    cr = cn.cursor()
    try:
        cr.execute("UPDATE Pedidos SET estado = ? WHERE id_pedido = ?", (nuevo_estado, id_pedido))
        cn.commit()
        flash(f"Pedido #{id_pedido} actualizado a {nuevo_estado}.", "success")
    except Exception as e:
        flash(f"Error al modificar estado: {e}", "error")
    finally:
        cn.close()
    return redirect("/seccion/pedidos")

# ACTUALIZAR CLIENTES CORPORATIVOS
@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    id_cliente = request.form.get("id_cliente")
    nombre = request.form.get("nombre")
    nit = request.form.get("nit")
    tel = request.form.get("telefono")
    
    cn = obtener_conexion()
    cr = cn.cursor()
    try:
        cr.execute("UPDATE Clientes SET nombre_empresa=?, nit=?, telefono_celular=? WHERE id_cliente=?", (nombre, nit, tel, id_cliente))
        cn.commit()
        flash("Cliente corporativo actualizado con éxito.", "success")
    except Exception as e:
        flash(f"Error al actualizar: {e}", "error")
    finally:
        cn.close()
    return redirect("/seccion/clientes")

# ELIMINAR CLIENTES CORPORATIVOS
@app.route("/eliminar_cliente", methods=["POST"])
def eliminar_cliente():
    id_cliente = request.form.get("id_cliente")
    cn = obtener_conexion()
    cr = cn.cursor()
    try:
        cr.execute("DELETE FROM Clientes WHERE id_cliente=?", (id_cliente,))
        cn.commit()
        flash("Cliente eliminado correctamente de la base de datos.", "success")
    except Exception as e:
        flash(f"No se puede borrar: Este cliente tiene pedidos asociados en el histórico.", "error")
    finally:
        cn.close()
    return redirect("/seccion/clientes")

if __name__ == "__main__":
    app.run(debug=True)


 