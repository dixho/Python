import sys
from tkinter import *

def hacer_click():
 try:
  _valor = int(entrada_texto.get())
  if _valor == 1:
    etiqueta.config(text="Pin Correcto")
 except ValueError:
  etiqueta.config(text="Introduzca PIN")
  if _valor != 1:
      etiqueta.config(text="Pin Incorrecto")

app = Tk()
app.title("Mi segunda App Grafica")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Valor")
etiqueta.grid(column=2, row=2, sticky=(W,E))

boton = Button(vp, text="OK!", command=hacer_click)
boton.grid(column=1, row=1)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)

app.mainloop()
