import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

MQTT_REMOTE_SERVER="192.168.30.84"
MQTT_PATH_SEND= "iotSound"
MQTT_PATH_RECV="iot"
USER="iotbroker"
PASS="iotbroker"
#topic = "iotDevice"

class conexion:
    def __init__(self):
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

     def onConnect(self, client, userdata, flags, rc):
            print("External Comm: connected with result code " + str(rc))
            client.subscribe(MQTT_PATH_RECV)


    def start(self):
        print("looping")
        self.client.loop_forever()
       

    def onMessage(self, client, userdata, msg):
        print("%s %s" % (msg.topic, msg.payload))
        result = msg.payload.decode("ascii")

        if result == "on":
            print("Iniciando")
        
        else result =="off":
            print("Apagando")

           
        



 
    