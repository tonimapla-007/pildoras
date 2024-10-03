from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

# miLabel = Label(miFrame, text="Hola alumnos de Python",
#               fg="red", font=("Comic Sans ms", 18))
# miLabel.pack()

miImagen = PhotoImage(file="avion.png")
# posicionamos el texto 'x' desde la izquierda, 'y' desde arriva
# situamos el Label en las coordenadas 'e' y 'n'
Label(miFrame, image=miImagen).place(x=100, y=200)

# otra forma de situar el Label es:
# Label(miFrame, text="Hola alumnos de Python").place(x=100, y=200)

root.mainloop()
