from flask import Flask, jsonify, request
import random

app = Flask(__name__)

SIMULATION = True

state = {
    "luces": False,
    "ventilador": False,
    "alarma": False,
    "temperatura": 22,
    "esNoche": False
}

def leer_datos():
    if SIMULATION:
        state["temperatura"] = random.randint(20, 35)
        state["esNoche"] = random.choice([True, False])
    return state

@app.get("/get_estado")
def get_estado():
    datos = leer_datos()
    return jsonify(datos)

@app.post("/set_luces")
def set_luces():
    data = request.json
    state["luces"] = data["value"]
    return jsonify({"ok": True, "luces": state["luces"]})

@app.post("/set_ventilador")
def set_ventilador():
    data = request.json
    state["ventilador"] = data["value"]
    return jsonify({"ok": True, "ventilador": state["ventilador"]})

@app.post("/set_alarma")
def set_alarma():
    data = request.json
    state["alarma"] = data["value"]
    return jsonify({"ok": True, "alarma": state["alarma"]})

if __name__ == "__main__":
    app.run(debug=True)
