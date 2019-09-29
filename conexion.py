from Gui import Gui
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


MQTT_REMOTE_SERVER="10.1.0.181"
MQTT_PATH_SEND= "iotSound"
MQTT_PATH_RECV="iot"
USER="iotbroker"
PASS="iotbroker"
#topic = "iotDevice"

class conexion:
    
    def __init__(self, gui):
        self.gui=self.gui
        self.flag=True
        self.client = self.mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(USER,PASS)
        self.client.connect(MQTT_REMOTE_SERVER,1883,60)
        print("connected")

    @staticmethod
    def sendSound(sound):
        try:
            publish.single(MQTT_PATH_SEND,"Sound:"+ sound,hostname= MQTT_REMOTE_SERVER,
                            auth={'username':USER,'password':PASS})
           
        except Exception as ex:
            print("Error in sendSound(). ex: {}".format(ex))

    def on_connect(self, client, userdata, flags, rc):
            print("External Comm: connected with result code " + str(rc))
            client.subscribe(MQTT_PATH_RECV)


    def start(self):
        print("looping")
        self.client.loop_forever()
       

    def on_message(self, client, userdata, msg):
        #print("%s %s" % (msg.topic, msg.payload))
        #result = msg.payload.decode("ascii")
        #self.result=input("Ingrese estado")
        #print("Estado",str(self.result))
        print("Conexion")
        result="on"
        if self.result == "on":
            print("conexion",self.getState)
            self.gui.setState(True)
            print("Iniciando")
        
        else:
            self.gui.setState(False)
            print("Apagando")
       
    def end_program (self):
        self.flag =False

    def is_ended (self):
        self.flag=True






 
    