from flask import Flask, render_template

from config import SECRET_KEY
from routes.cliente_routes import cliente_bp
from routes.suela_routes import suela_bp
from routes.pedido_routes import pedido_bp
from routes.material_routes import material_bp
from routes.api_routes import api_bp
from services import pagina_service

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.register_blueprint(cliente_bp)
app.register_blueprint(suela_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(material_bp)
app.register_blueprint(api_bp)


@app.route("/")
def inicio():
    datos = pagina_service.obtener_datos_pagina()

    return render_template(
        "index.html",
        seccion="clientes",
        clientes=datos["clientes"],
        suelas=datos["suelas"],
        colores=datos["colores"],
        pedidos=datos["pedidos"],
        materiales=datos["materiales"],
        reporte_clientes=datos["reporte_clientes"],
        kpi_por_pedidos=datos["kpi_por_pedidos"],
        kpi_total_referencias=datos["kpi_total_referencias"],
        kpi_total_pedidos=datos["kpi_total_pedidos"],
        kpi_modulo_reportes=datos["kpi_modulo_reportes"],
    )


@app.route("/seccion/<nombre_seccion>")
def mostrar_seccion(nombre_seccion):
    secciones_validas = [
        "clientes",
        "pedidos",
        "suelas",
        "reportes"
    ]

    if nombre_seccion not in secciones_validas:
        return "Sección no encontrada", 404

    datos = pagina_service.obtener_datos_pagina()

    return render_template(
        "index.html",
        seccion=nombre_seccion,
        clientes=datos["clientes"],
        suelas=datos["suelas"],
        colores=datos["colores"],
        pedidos=datos["pedidos"],
        materiales=datos["materiales"],
        reporte_clientes=datos["reporte_clientes"],
        kpi_por_pedidos=datos["kpi_por_pedidos"],
        kpi_total_referencias=datos["kpi_total_referencias"],
        kpi_total_pedidos=datos["kpi_total_pedidos"],
        kpi_modulo_reportes=datos["kpi_modulo_reportes"],
    )


if __name__ == "__main__":
    app.run(debug=True)