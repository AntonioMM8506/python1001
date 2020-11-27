from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/json", methods=["GET"])
def ejemplo_json():
    contenido = {"id":1, "nombre": "Juan", "apelldio": "some"}
    segundo = {"id":2, "nombre": "Antonio", "apelldio": "Maldonado"}
    lista = [contenido, segundo]
    return jsonify(lista)

@app.route("/", methods=["GET"])
def hola_mundo_con_flask():
    return "hola mundo"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")