from gui import Gui
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

MQTT_REMOTE_SERVER="192.168.43.64"
#MQTT_REMOTE_SERVER="127.0.0.1"
MQTT_PATH_SEND= "iotSound"
MQTT_PATH_RECV="iot"
USER="iotbroker"
PASS="iotbroker"

#topic = "iotDevice"

class Conexion:
    
    def __init__(self,gui):
        self.gui = gui
	#gui.setState(True)
        self.flag = True
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(USER,PASS)
        self.client.connect(MQTT_REMOTE_SERVER,1883,60)
        print("connected")

    def on_connect(self, client, userdata, flags, rc):
            print("External Comm: connected with result code " + str(rc))
            client.subscribe(MQTT_PATH_RECV)


    def start(self):
        print("looping")
        self.client.loop_forever()
       

    def on_message(self, client, userdata, msg):
        print("Ha llegado un mensaje !!!")
        print("conexion ",self.gui.getState())
       	self.gui.setState(True)
        print("conexion despues", self.gui.getState())
        print("Iniciando")
        
        #else:
         #   self.gui.setState(False)
          #  print("Apagando")
       
    def end_program (self):
        self.flag =False

    def is_ended (self):
        self.flag = True






 
    
