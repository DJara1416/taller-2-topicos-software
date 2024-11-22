from flask import Flask, Blueprint, jsonify, render_template
import socket
from pokeneas import obtener_pokenea_aleatorio

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a Pokeneas"

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

# Registrar el blueprint en la aplicación Flask
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
