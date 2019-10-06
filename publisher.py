import paho.mqtt.publish as publish

#MQTT_REMOTE_SERVER="192.168.34.196"

MQTT_REMOTE_SERVER="127.0.0.1"
MQTT_PATH_SEND= "iotSound"
MQTT_PATH_RECV="iot"
USER="iotbroker"
PASS="iotbroker"

def sendSound(sound):
    try:
        publish.single(MQTT_PATH_SEND, str(sound), hostname= MQTT_REMOTE_SERVER,
                       auth={'username':USER,'password':PASS})
        
    except Exception as ex:
        print("Error in sendSound(). ex: {}".format(ex))
        
    



 
    
