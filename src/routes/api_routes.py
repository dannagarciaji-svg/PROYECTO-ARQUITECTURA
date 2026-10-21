from flask import Blueprint, jsonify
from services import suela_service, cliente_service

# Creamos el Blueprint con un prefijo '/api' para no chocar con las rutas web
api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/suelas", methods=["GET"])
def obtener_suelas_api():
    try:
        # Llamamos al servicio que ya construiste
        suelas_crud = suela_service.listar_suelas()
        
        # Formateamos las tuplas a diccionarios (JSON)
        suelas_json = []
        for s in suelas_crud:
            suelas_json.append({
                "id_suela": s[0],
                "referencia": s[1],
                "talla": s[2],
                "stock_disponible": s[3],
                "precio_unidad": float(s[4]),
                "color": s[5]
            })
            
        return jsonify({"status": "success", "data": suelas_json}), 200
    except Exception as error:
        return jsonify({"status": "error", "message": str(error)}), 500

@api_bp.route("/clientes", methods=["GET"])
def obtener_clientes_api():
    try:
        clientes_crud = cliente_service.listar_clientes()
        
        clientes_json = []
        for c in clientes_crud:
            clientes_json.append({
                "id_cliente": c[0],
                "nombre_empresa": c[1],
                "nit": c[2],
                "telefono": c[3] if c[3] else "No asignado"
            })
            
        return jsonify({"status": "success", "data": clientes_json}), 200
    except Exception as error:
        return jsonify({"status": "error", "message": str(error)}), 500
        