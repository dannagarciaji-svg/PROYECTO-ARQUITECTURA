
from flask import Blueprint, request, redirect, url_for, flash

from services import suela_service

suela_bp = Blueprint("suelas", __name__)


@suela_bp.route("/crear_suela", methods=["POST"])
def crear_suela():
    try:
        referencia = request.form.get("referencia", "")
        talla = request.form.get("talla", "")
        color = request.form.get("color", "")
        id_material = request.form.get("id_material", "")
        precio = request.form.get("precio", "")
        stock = request.form.get("stock", "")

        suela_service.registrar_suela(
            referencia, talla, color, id_material, precio, stock
        )
        flash("Suela creada correctamente.", "success")

    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("mostrar_seccion", nombre_seccion="suelas"))


@suela_bp.route("/actualizar_stock/<int:id_suela>", methods=["POST"])
def actualizar_stock(id_suela):
    try:
        nuevo_stock = request.form.get("nuevo_stock", "")
        suela_service.modificar_stock(id_suela, nuevo_stock)
        flash("Stock actualizado correctamente.", "success")

    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("mostrar_seccion", nombre_seccion="suelas"))


# =========================
# CRUD DE COLORES
# =========================

@suela_bp.route("/crear_color", methods=["POST"])
def crear_color():
    try:
        nombre_color = request.form.get("nombre_color", "")
        suela_service.registrar_color(nombre_color)
        flash("Color creado correctamente.", "success")

    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("mostrar_seccion", nombre_seccion="suelas"))


@suela_bp.route("/actualizar_color/<int:id_color>", methods=["POST"])
def actualizar_color(id_color):
    try:
        nuevo_nombre = request.form.get("nuevo_nombre", "")
        suela_service.modificar_color(id_color, nuevo_nombre)
        flash("Color actualizado correctamente.", "success")

    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("mostrar_seccion", nombre_seccion="suelas"))


@suela_bp.route("/eliminar_color/<int:id_color>", methods=["POST"])
def eliminar_color(id_color):
    try:
        suela_service.borrar_color(id_color)
        flash("Color eliminado correctamente.", "success")

    except ValueError as error:
        flash(str(error), "error")

    return redirect(url_for("mostrar_seccion", nombre_seccion="suelas"))
