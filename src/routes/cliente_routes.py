
from flask import Blueprint, request, redirect, url_for, flash

from services import cliente_service

cliente_bp = Blueprint("clientes", __name__)


@cliente_bp.route("/crear_cliente", methods=["POST"])
def crear_cliente():
    try:
        nombre = request.form.get("nombre", "")
        nit = request.form.get("nit", "")
        telefono = request.form.get("telefono", "")

        cliente_service.registrar_cliente(nombre, nit, telefono)
        flash("Cliente creado correctamente.", "success")
    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("inicio"))


@cliente_bp.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    try:
        id_cliente = request.form.get("id_cliente")
        nombre = request.form.get("nombre", "")
        nit = request.form.get("nit", "")
        telefono = request.form.get("telefono", "")

        cliente_service.modificar_cliente(id_cliente, nombre, nit, telefono)
        flash("Cliente actualizado correctamente.", "success")
    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("inicio"))


@cliente_bp.route("/eliminar_cliente", methods=["POST"])
def eliminar_cliente():
    try:
        id_cliente = request.form.get("id_cliente")
        cliente_service.borrar_cliente(id_cliente)
        flash("Cliente eliminado correctamente.", "success")
    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("inicio"))
