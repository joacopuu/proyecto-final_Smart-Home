import serial
import requests
import time
from datetime import datetime

arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=-34.61&longitude=-58.38&current_weather=true"

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

while True:
    temp = get_weather_data()
    ciclo = get_day_cycle()
    alarma = "OFF" 
    
    if temp is not None:
        print(f"Temperatura: {temp}°C | Ciclo: {ciclo} | Alarma: {alarma}")

        if temp > 28:
            send_to_arduino("VENT_ON")
        else:
            send_to_arduino("VENT_OFF")

        if ciclo == "NOCHE":
            send_to_arduino("LED_ON")
        else:
            send_to_arduino("LED_OFF")

        if alarma == "ON":
            send_to_arduino("BUZZ_ON")
        else:
            send_to_arduino("BUZZ_OFF")

    time.sleep(5)
