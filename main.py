import threading

import tkinter as tk
from tkinter import *
from gui import Gui
from test import Sensor 
#from conexion import conexion


   # def __init__(self,*args,**kwargs):
     #   Tk.__init__(self, *args, **kwargs)
       # gui = Gui()
root = Tk()

#root.title('NIVEL DE SONIDO')
#panel = Label(root, anchor="center")
#panel.grid(row=10, columnspan=20)
#root.configure(background="yellow")
#root.attributes('-fullscreen', True)
#mainloop()

gui= Gui(root)
#gui.startGui()


#sensor=Sensor()
#print(sensor.sensor())







#state_q = Queue()
#process = Process(name='w1',target=gui.run, args=(state_q))
#process.start()
#process.join()
