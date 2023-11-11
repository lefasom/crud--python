import os
from flask import Flask, render_template
from dotenv import load_dotenv

from config.mongodb import mongo
from routes.rutas import rutas

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo.init_app(app)


@app.route("/")
def Home():
    cursor = mongo.db.lista.find()
    listas = list(cursor)  # Convierte el cursor a una lista
    return render_template('index.html', listas=listas)


@app.route("/galery")
def Galery():
    ruta_carpeta = "src/static/video"
    archivos = os.listdir(ruta_carpeta)
    videos = [
        archivo for archivo in archivos if archivo.endswith((".mp4", ".avi", ".mkv"))
    ]
    print("videos", videos)

    return render_template("galery.html", mensaje="Fullmetal Alchemist", videos=videos)


app.register_blueprint(rutas, url_prefix="/rutas")
if __name__ == "__main__":
    app.run(debug=True)
