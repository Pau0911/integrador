from tkinter import *
import tkinter as tk

root = Tk() 
def rojo():
  #imagen=PhotoImage(file="nino.png")
  #fondo=PhotoImage(file="nino.png")
  #lblFondo=Label(root,image=imagen)
  #lblFondo.place(x=580,y=500)
  #nameLabel1=Label(root,text="Silencio",font=("Arial Bold",50)).pack()
  nameLabel1 = Label(root, text="SILENCIO", bg="red",font=("Arial Bold",100)) 
  nameLabel1.pack(side="bottom")##Usar grid
 
  root.geometry("300x200")
  root.configure(background="red")
  

def amarillo():
  root.geometry("300x200")
  root.configure(background="yellow")
 
while True: 
      root.quit()
      contador=int(input("Ingrese el numero"))
      print(contador)
      root.title("Nivel de ruido")
      if contador>= 30:
        rojo()
      else:
        amarillo()
root.mainloop()







