from flask import Blueprint, jsonify, render_template
import socket
from pokeneas import obtener_pokenea_aleatorio

# Crear un blueprint para las rutas
routes = Blueprint('routes', __name__)

@routes.route('/pokenea_json', methods=['GET'])
def pokenea_json():
    pokenea = obtener_pokenea_aleatorio()
    contenedor_id = socket.gethostname()
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": contenedor_id
    }
    return jsonify(response)

@routes.route('/pokenea_imagen', methods=['GET'])
def pokenea_imagen():
    pokenea = obtener_pokenea_aleatorio()
    contenedor_id = socket.gethostname()
    return render_template('pokenea.html', pokenea=pokenea, contenedor_id=contenedor_id)
