import tkinter as tk
from tkinter import *
#from conexion import conexion
from test import Sensor
import time
import threading


class Gui(threading.Thread,Tk):

    root=None

    def __init__(self,root,*args,**kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.root=root
        self.sensor=Sensor()
        threading.Thread.__init__(self)
        self.run()
        #inicializacion del hilo
    

    def amarillo(self):
        
        self.root.title('NIVEL DE SONIDO')
        self.panel = Label(self.root, anchor="center")
        self.panel.grid(row=10, columnspan=20)
        self.root.configure(background="yellow")
        self.root.attributes('-fullscreen', True)
       

    def rojo(self):
       
        self.root.title('NIVEL DE SONIDO')
        self.panel = Label(self.root, anchor="center")
        self.panel.grid(row=10, columnspan=20)
        self.root.configure(background="red")
        self.root.attributes('-fullscreen', True)
        self.startGui()
        
       
    def run(self):
       
        while True:
            time.sleep(5)
            self.value =self.sensor.sensor()
            print (self.value)
            if self.value >= 40:
                print("Hola")
                self.rojo()
            #self.conexion.sendSound(value)
            else:
                self.amarillo()
               # self.startGui()
            #self.conexion.sendSound(value)

    def startGui(self):
        self.mainloop()
    
        
        
   
   
   
    #def set_state(q_state):
        #msg = q_state.get()
        #if (msg == 0):
            #self.amarillo()
        #else:
            #self.rojo()
    
    #def run(qstate):
        #self.root.after(0, self.set)
        

root=Tk()
app = Gui(root)
#LABEL = Label(root, text="Hello, world!")
#LABEL.pack()

app.mainloop()
#prueba=Gui()
#prueba.rojo()
#prueba.amarillo()


