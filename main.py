from _thread import start_new_thread
from gui import Gui
from conexion import Conexion

gui = Gui()
print("que miedo")
conexion = Conexion(gui)


try:
    start_new_thread(gui.startGui, ())
    start_new_thread(gui.run, ())
    start_new_thread(conexion.start, ())
except Exception as ex:
    print("Error: unable to start thread. ex: {}".format(ex))

while True:#conexion.is_ended():
    pass


