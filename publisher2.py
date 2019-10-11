import paho.mqtt.publish as publish
import time
MQTT_REMOTE_SERVER="192.168.43.64"

#MQTT_REMOTE_SERVER="127.0.0.1"
MQTT_PATH_SEND= "iotCritic"
MQTT_PATH_RECV="iot"
USER="iotbroker"
PASS="iotbroker"

ahora = time.strftime("%c")

def sendSound2(sound):
    try:
        publish.single(MQTT_PATH_SEND, "c"+str(sound), hostname= MQTT_REMOTE_SERVER,
                       auth={'username':USER,'password':PASS})
        
    except Exception as ex:
        print("Error in sendSound(). ex: {}".format(ex))
