from flask import Blueprint, render_template

from services import material_service

material_bp = Blueprint("materiales", __name__)


@material_bp.route("/materiales")
def listar_materiales():
    materiales = material_service.listar_materiales()
    return render_template(
        "index.html",
        seccion="suelas",
        materiales=materiales
    )