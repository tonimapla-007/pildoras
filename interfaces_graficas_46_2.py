from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)  # creamos el primer frame
miFrame.pack()

minombre = StringVar()

# cuadroTexto.place(x=100, y=100)        #colocamos el cueadro en las coordenadas fijadas

# esta linea pone un nombre en el cuadroNombre el texto
cuadroNombre = Entry(miFrame, textvariable=minombre)
# preparamos una rejilla con grid() para situar los whitges     #introducido en la funcion codigoBoton
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="right")

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

# barra de desplazamiento para el campo de texto
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

# sticky alinea el nombre al n,s,e,o puntos cardinales
nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

DireccionLabel = Label(miFrame, text="Direccion:")
DireccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)


def codigoBoton():
    minombre.set("Juan")


botonEnvio = Button(miFrame, text="Enviar",
                    command=codigoBoton)  # boton en frame
botonEnvio.grid(row=5, column=1)
# botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)         #boton en raiz
# botonEnvio.pack()


raiz.mainloop()
