"""
Programa:
-ventana
-tamaño fijo
-no redimencionable
-un menu (Inicio, Añadir, Informacion, Salir)
-diferentes pantallas
-formulario para añadir productos
-guardar datos (temporalmente)
-mostrar datos listados en la pantalla Home
-opcion de salir
"""

from tkinter import *

#Definicion de ventana
ventana = Tk()

#Confiruaciones de ventana
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter")
ventana.resizable(0, 0)

#Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio")
menu_superior.add_command(label="Añadir")
menu_superior.add_command(label="Informacion")
menu_superior.add_command(label="Salir", command=ventana.quit)

#Cargar menu
ventana.config(menu=menu_superior)




#Funcion de carga de la ventana
ventana.mainloop()