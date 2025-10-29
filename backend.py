import serial
import requests
import time
from datetime import datetime

# ===============================
# CONFIGURACIÓN DEL ARDUINO
# ===============================
arduino = serial.Serial('COM3', 9600, timeout=1)  # Cambiar puerto según tu PC
time.sleep(2)  # Esperar a que el Arduino se inicie

# ===============================
# CONFIGURACIÓN API (Buenos Aires)
# ===============================
API_URL = "https://api.open-meteo.com/v1/forecast?latitude=-34.61&longitude=-58.38&current_weather=true"

# ===============================
# LÓGICA DE CONTROL 🧠
# ===============================
def get_weather_data():
    try:
        response = requests.get(API_URL)
        data = response.json()
        temp = data["current_weather"]["temperature"]
        return temp
    except:
        print("Error obteniendo datos de la API")
        return None

def get_day_cycle():
    hora = datetime.now().hour
    return "DIA" if 8 <= hora <= 20 else "NOCHE"

def send_to_arduino(command):
    try:
        arduino.write((command + "\n").encode())
        print("Enviado:", command)
    except:
        print("Error enviando al Arduino")

# ===============================
# PROGRAMA PRINCIPAL
# ===============================
while True:
    temp = get_weather_data()
    ciclo = get_day_cycle()
    alarma = "OFF"  # En el futuro, lo controlaremos desde Qt
    
    if temp is not None:
        print(f"Temperatura: {temp}°C | Ciclo: {ciclo} | Alarma: {alarma}")

        # ---- CONTROL AUTOMÁTICO ----

        # Ventiladores
        if temp > 28:
            send_to_arduino("VENT_ON")
        else:
            send_to_arduino("VENT_OFF")

        # Luces
        if ciclo == "NOCHE":
            send_to_arduino("LED_ON")
        else:
            send_to_arduino("LED_OFF")

        # Alarma
        if alarma == "ON":
            send_to_arduino("BUZZ_ON")
        else:
            send_to_arduino("BUZZ_OFF")

    time.sleep(5)  # Actualiza cada 5 segundos
