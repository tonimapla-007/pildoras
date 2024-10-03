from tkinter import *

raiz = Tk()  # variable de trabajo

raiz.title("Ventana de pruebas")

# hacemos que no se pueda redimensionar la ventana 0,0 o si 1,1
raiz.resizable(1, 1)

raiz.iconbitmap("avion.ico")  # cambiamos el icono

raiz.geometry("650x350")  # cambio de tamaño

raiz.config(bg="blue")  # cambio color de fondo

raiz.mainloop()  # bucle general infinito
