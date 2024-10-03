from tkinter import *

raiz = Tk()  # variable de trabajo

raiz.title("Ventana de pruebas")

# hacemos que no se pueda redimensionar la ventana 0,0 o si 1,1
# raiz.resizable(1, 1)

raiz.iconbitmap("avion.ico")  # cambiamos el icono

# raiz.geometry("650x350")  # cambio de tamaño

raiz.config(bg="blue")  # cambio color de fondo

miFrame = Frame()

# el frame se expande 'y' , para todas direcciones 'booth'
# miFrame.pack(fill='y', expand='True')

# empaquetamos el frame, queda dentro de la raiz, lo posicionamos al n,s,e,o
miFrame.pack(side='left', anchor="n")

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)       # tamaño del borde

miFrame.config(relief="groove")  # caracteristicas del borde

miFrame.config(cursor="hand2")  # camiamos el cursor

raiz.mainloop()  # bucle general infinito

# todo lo concerniente a la raiz es aplicable al frame y viceversa
# DOCUMENTACION https://docs.python.org/3/library/tk.html
