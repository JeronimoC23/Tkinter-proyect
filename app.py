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


creador = "Jeronimo Clinaz"
#Definicion de ventana
ventana = Tk()

#Confiruaciones de ventana
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter")
ventana.resizable(0, 0)


#Definir campos de pantalla (INICIO)}
home_label = Label(ventana, text="Inicio")

#Definir campos de pantalla (AGREGAR)}
add_label = Label(ventana, text="Agregar productos")

#Definir campos de pantalla (INFORMACION)}
info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text=f"Creado por {creador}")
  
#Pantallas
def home():
    #Montar pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)
    cleanScreen("home")
  

def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)
    cleanScreen("add")

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1,column=0)
    cleanScreen("info")


def cleanScreen(screen):
    #Ocultar otras pantallas
    if screen == "home" :
        add_label.grid_remove()
        info_label.grid_remove()
        data_label.grid_remove()
    elif screen == "add":
        info_label.grid_remove()
        data_label.grid_remove()
        home_label.grid_remove()
    elif screen == "info":
        home_label.grid_remove()
        add_label.grid_remove()


  
#Cargar pantalla de inicio
home()


#Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir",command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#Cargar menu
ventana.config(menu=menu_superior)

#Funcion de carga de la ventana
ventana.mainloop()