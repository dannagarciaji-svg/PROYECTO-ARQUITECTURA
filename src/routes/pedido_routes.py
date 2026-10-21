
from flask import Blueprint, request, redirect, url_for, flash

from services import pedido_service

pedido_bp = Blueprint("pedidos", __name__)


@pedido_bp.route("/crear_pedido", methods=["POST"])
def crear_pedido():
    try:
        id_cliente = request.form.get("id_cliente", "")
        id_suela = request.form.get("id_suela", "")
        color = request.form.get("color", "")
        cantidad = request.form.get("cantidad", "")

        pedido_service.registrar_pedido(
            id_cliente, id_suela, color, cantidad
        )

        flash("Pedido creado correctamente.", "success")

    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("mostrar_seccion", nombre_seccion="pedidos"))


@pedido_bp.route("/actualizar_estado_pedido", methods=["POST"])
def actualizar_estado_pedido():
    try:
        id_pedido = request.form.get("id_pedido", "")
        nuevo_estado = request.form.get("estado", "")

        pedido_service.cambiar_estado_pedido(
            id_pedido, nuevo_estado
        )

        flash("Estado del pedido actualizado correctamente.", "success")

    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("mostrar_seccion", nombre_seccion="pedidos"))
