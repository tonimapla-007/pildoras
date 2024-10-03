"""
ventanas emergentes 2
"""
from tkinter import *
from tkinter import filedialog

root = Tk()


def abreFichero():

    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(
        ("Ficheros de excel", "*.xlsx"), ("ficheros de texto", "*.txt"), ("todos los ficheros", "*.*")))

    print(fichero)


Button(root, text="Abrir fichero",
       command=abreFichero).pack()  # devuelve el path


root.mainloop()
