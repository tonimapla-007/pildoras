"""
calculadora
"""
from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

operacion = ""

reset_pantalla = False

resultado = 0

# ****************************** pantalla****************************************

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# *********************************pulsaciones teclado*******************************

# al repetir un numero a saliendo por pantalla con el anterior concatenado


def numeroPulsado(num):

    global operacion
    global reset_pantalla

    if reset_pantalla != False:

        numeroPantalla.set(num)
        reset_pantalla = False

    else:
        numeroPantalla.set(numeroPantalla.get() + num)


# ******************************funcion suma**************************************

def suma(num):
    global operacion

    global resultado

    global reset_pantalla

    resultado += int(num)

    operacion = "suma"

    reset_pantalla = True

    numeroPantalla.set(resultado+int(numeroPantalla.get()))

# funcion el resultado*************************************************************


def el_resultado():

    global resultado

    numeroPantalla.set(resultado+int(numeroPantalla.get()))

    resultado = 0

# *******************************fila2********************************************


boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

# *******************************fila3********************************************

boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="X", width=3)
botonMult.grid(row=3, column=4)

# *******************************fila4********************************************

boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)

# *******************************fila5********************************************

boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=3,
                   command=lambda: numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command=lambda: el_resultado())
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text="+", width=3,
                  command=lambda: suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)


raiz.mainloop()
