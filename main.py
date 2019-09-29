import threading
import tkinter as tk
from tkinter import *
from Gui import Gui
from Sensor import Sensor 
from conexion import conexion



root=Tk()
#app = Gui(root)
#app.startGui()

gui=Gui(root)
conexion=conexion(gui)


try:
    start_new_thread(gui.startGui, ())
    start_new_thread(conexion.start, ())
except Exception as ex:
    print("Error: unable to start thread. ex: {}".format(ex))

while conexion.is_ended():
    pass


