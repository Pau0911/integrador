from tkinter import * 
from Sensor import Sensor
from publisher import sendSound
import time

class Gui:
    root=None
    def __init__(self):
        self.state = True
        self.sensor=Sensor()
        
    def amarillo(self):
        self.root.configure(background="green")
       
    def rojo(self):
        self.root.configure(background="red")
        
    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state        
    def run(self):
        tiempo=0
        contador=0
        num=15
        while True:
            tiempo=tiempo+1
            if(tiempo<num):
                time.sleep(1)
                self.value = self.sensor.sensor()
                print (self.value)
                #state
                print(self.getState())
                if(self.getState()==True):
                    if self.value >= 1000:
                        contador=contador+1
                        print("Hola")
                        sendSound(self.value)
                        #self.rojo()
                    else:
                        #self.amarillo()
                        sendSound(self.value)
                else:
                    print("Dispositivo apagado")
            elif(tiempo==num):
                tiempo=0
                if(contador>=7):
                    self.rojo()
                    print("Conte mas de 7")
                else:
                    self.amarillo()
                contador=0
    
    def startGui(self):
        self.root = Tk()
        self.root.title('NIVEL DE SONIDO')
        self.panel = Label(self.root, anchor="center")
        self.panel.grid(row=10, columnspan=20)
        self.root.attributes('-fullscreen', True)
        mainloop()
