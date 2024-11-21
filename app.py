from flask import Flask
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
