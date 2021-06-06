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

#Variables
name_data=StringVar()
price_data = IntVar()




#Definir campos de pantalla (INICIO)}
home_label = Label(ventana, text="Inicio")

#Definir campos de pantalla (AGREGAR)}
add_label = Label(ventana, text="Agregar productos")

#Campos del formulario (ADD)
add_name_label = Label(ventana, text="Nombre del producto:")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text="Precio del producto:")
add_price_entry = Entry(ventana, textvariable=price_data)

add_description_label = Label(ventana, text="Descripcion: ")
add_description_entry = Text(ventana)

boton = Button(ventana, text="Guardar")

add_separator = Label(ventana)

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
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)
    cleanScreen("home")
  

def add():
    #Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=90,
        pady=20
    )
    add_label.grid(row=0, column=0,columnspan=4)
    cleanScreen("add")

    #Campos del formulario
    add_name_label.grid(row=1,column=0, padx=5, pady=5)
    add_name_entry.grid(row=1,column=1, padx=5, pady=5,sticky=W)

    add_price_label.grid(row=2,column=0, padx=5, pady=5)
    add_price_entry.grid(row=2,column=1, padx=5, pady=5,sticky=W)

    add_description_label.grid(row=3,column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3,column=1, padx=5, pady=5,sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4, column=1)

    boton.grid(row=5,column=1, sticky=NW)
    boton.config(
        padx=15,
        bg="black",
        fg="green",

    )


def info():
    #Encabezado
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=160,
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