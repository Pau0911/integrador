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
        while True:
            time.sleep(1)
            self.value = self.sensor.sensor()
            print (self.value)
            #state
            print(self.getState())
            if(self.getState()==True):
                if self.value >= 1000:
                    print("Hola")
                    sendSound(self.value)
                    self.rojo()
                else:
                    self.amarillo()
                    sendSound(self.value)
            else:
                print("Dispositivo apagado")


    def startGui(self):
        self.root = Tk()
        self.root.title('NIVEL DE SONIDO')
        self.panel = Label(self.root, anchor="center")
        self.panel.grid(row=10, columnspan=20)
        self.root.attributes('-fullscreen', True)
        mainloop()
