import sys
import requests
import serial
import time
from datetime import datetime, timedelta 
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QTimer

try:
    from prueba import Ui_MainWindow
except ImportError:
    print("ERROR CRÍTICO: No se encontró el archivo 'prueba.py'.")
    print("Asegúrate de que 'prueba.py' y este archivo estén en la MISMA CARPETA.")
    sys.exit()

class MainWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.arduino_port = "COM3"  
        self.arduino = None
        self.conectar_arduino()

        self.alarma_estado = 0

        self.ui.btn_luces_on.clicked.connect(self.prender_luz)
        self.ui.btn_luces_off.clicked.connect(self.apagar_luz)
        self.ui.btn_vent_on.clicked.connect(self.prender_vent)
        self.ui.btn_vent_off.clicked.connect(self.apagar_vent)
        self.ui.btn_alarma_on.clicked.connect(self.prender_alarma)
        self.ui.btn_alarma_off.clicked.connect(self.apagar_alarma)

        self.timer = QTimer(self)
        self.timer.setInterval(10000) 
        self.timer.timeout.connect(self.actualizar_sistema)
        self.timer.start()
        
        print("Sistema iniciado correctamente.")
        self.actualizar_sistema()

    def conectar_arduino(self):
        try:
            self.arduino = serial.Serial(self.arduino_port, 9600, timeout=1)
            time.sleep(2)
            print(f"Conectado a Arduino en {self.arduino_port}")
        except:
            print(f"No se pudo conectar a {self.arduino_port}. Modo Simulación.")

    def enviar_comando(self, mensaje, es_comando=True):
        """Envía datos al Arduino si está conectado."""
        if self.arduino:
            try:
                if es_comando:
                    self.arduino.write(f"{mensaje}\n".encode())
                else:
                    self.arduino.write(mensaje.encode())
            except:
                print("Error enviando datos (Arduino desconectado)")
        else:
            print(f"[SIMULACIÓN] Enviando: {mensaje}")

    def actualizar_sistema(self):
        temp, dia, hora = self.obtener_clima()
        
        if temp is None: 
            return

        try:
            self.ui.lcd_temperatura.display(temp)
            self.ui.label_ciclo.setText("Día" if dia == 1 else "Noche")
        except AttributeError: pass

        mensaje_lcd = f"TEMP:{temp};DIA:{dia};HORA:{hora};ALR:{self.alarma_estado}\n"
        self.enviar_comando(mensaje_lcd, es_comando=False)

        try:
            modo_auto = self.ui.check_automatico.isChecked()
        except AttributeError:
            modo_auto = False 
            print("Aviso: No se encontró el checkbox 'check_automatico' en prueba.py")

        if modo_auto:
            print(f"--- MODO AUTO (T: {temp}°C) ---")
            
            if temp > 28:
                print(">> Calor: Ventilador ON")
                self.prender_vent()
            else:
                print(">> Temp OK: Ventilador OFF")
                self.apagar_vent()

            if dia == 1:
                print(">> Es de día: Luz OFF")
                self.apagar_luz()
        else:
            print("--- MODO MANUAL ---")

    def obtener_clima(self):
        try:
            url = "https://api.open-meteo.com/v1/forecast?latitude=-31.4201&longitude=-64.1888&current_weather=true"
            resp = requests.get(url, timeout=5).json()
            
            temp = resp["current_weather"]["temperature"]
            dia = resp["current_weather"]["is_day"]
            
            hora_utc_str = resp["current_weather"]["time"] 
            fecha_hora_utc = datetime.strptime(hora_utc_str, "%Y-%m-%dT%H:%M")
            fecha_hora_arg = fecha_hora_utc - timedelta(hours=3)
            
            hora_final = fecha_hora_arg.strftime("%H:%M")
            
            return temp, dia, hora_final
        except:
            print("Error de conexión con API Clima")
            return None, None, None

    def prender_luz(self):
        self.enviar_comando("LED:ON")
        try: self.ui.label_luces_estado.setText("Prendidas")
        except: pass

    def apagar_luz(self):
        self.enviar_comando("LED:OFF")
        try: self.ui.label_luces_estado.setText("Apagadas")
        except: pass

    def prender_vent(self):
        self.enviar_comando("SERVO:ON")
        try: self.ui.label_vent_estado.setText("Prendidos")
        except: pass

    def apagar_vent(self):
        self.enviar_comando("SERVO:OFF")
        try: self.ui.label_vent_estado.setText("Apagados")
        except: pass

    def prender_alarma(self):
        self.enviar_comando("BUZZER:ON")
        self.alarma_estado = 1
        try: self.ui.label_alarma_estado.setText("Activada")
        except: pass

    def apagar_alarma(self):
        self.enviar_comando("BUZZER:OFF")
        self.alarma_estado = 0
        try: self.ui.label_alarma_estado.setText("Desactivada")
        except: pass

    def closeEvent(self, event):
        if self.arduino:
            self.arduino.close()
        event.accept()

if _name_ == "_main_":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())