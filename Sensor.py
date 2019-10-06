import time
import Adafruit_ADS1x15

class Sensor:

    def __init__(self):
        print ("Iniciando sensor")
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.GAIN = 1

    def sensor(self):
        #self.value= 10
        self.value = self.adc.read_adc(0, gain=self.GAIN)
        #self.value = int(input("Ingrese un numero"))
        #self.value=bytes([3])
	#print("sonido",self.value)
        return self.value

    
