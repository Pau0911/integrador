import tkinter as tk
from tkinter import *
#from conexion import conexion

from Sensor import Sensor
import time
import threading



class Gui(threading.Thread,Tk):

    root=None

    def __init__(self,root,*args,**kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.state= True
        self.root=root
        self.sensor=Sensor()
        #self.conexion=conexion()
        threading.Thread.__init__(self)
        self.run()
        #inicializacion del hilo
    #metodostate

    def amarillo(self):
        
        self.root.title('NIVEL DE SONIDO')
        self.panel = Label(self.root, anchor="center")
        self.panel.grid(row=10, columnspan=20)
        self.root.configure(background="yellow")
        self.root.attributes('-fullscreen', True)
        self.startGui()
       

    def setState(self):
        return self.state


    def getState(self):
        self.state


    def rojo(self):
       
        self.root.title('NIVEL DE SONIDO')
        self.panel = Label(self.root, anchor="center")
        self.panel.grid(row=10, columnspan=20)
        self.root.configure(background="red")
        self.root.attributes('-fullscreen', True)
        self.startGui()
        
       
    def run(self):
       
        while True:
            time.sleep(1)
            self.value =self.sensor.sensor()
            print (self.value)
            #state
            print(self.getState())
            if(self.getState()==True):
                if self.value >= 40:
                    print("Hola")
                    self.conexion.sendSound(value)
                    self.rojo()
            
                else:
                    self.amarillo()
                    self.conexion.sendSound(value)
            else:
                print("Dispositivo apagado")


    def startGui(self):
        self.update_idletasks()
        self.update()
    
        
        
   
    #def set_state(q_state):
        #msg = q_state.get()
        #if (msg == 0):
            #self.amarillo()
        #else:
            #self.rojo()
    
    #def run(qstate):
        #self.root.after(0, self.set)
        

#root=Tk()
#app = Gui(root)
#LABEL = Label(root, text="Hello, world!")
#LABEL.pack()
#app.startGui()
#prueba=Gui()
#prueba.rojo()
#prueba.amarillo()


