"""
menus
"""
from tkinter import *
from tkinter import messagebox  # libreria para ventanas emergentes

root = Tk()


def InfoAdicional():  # informacion para ventanas emergentes
    messagebox.showinfo("Procesador de Juan",
                        "Procesador de textos version 2018")


def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")


def salirAplicacion():

    # valor = messagebox.askquestion("Salir", "Desea salir de la aplicacion?")
    valor = messagebox.askokcancel("Salir", "Desea salir de la aplicacion?")
    # if valor == "yes":
    if valor == True:
        root.destroy()


def cerrarDocumento():
    valor = messagebox.askretrycancel(
        "Reintentar", "No es posible cerrar. Documento bloqueado.")
    if valor == False:
        root.destroy()


barraMenu = Menu(root)

# damos medidas al frame, creamos el menu barra
root.config(menu=barraMenu, width=300, height=300)


# quitamos la linea discontinua del menu por defecto
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()  # creamos la linea de separacion en el menu
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)


archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
# llamamos funcion para informacion adicional
archivoAyuda.add_command(label="A cerca de", command=InfoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()
