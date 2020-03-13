from tkinter import *
import time, random
from random import randint
global color, banderaApuesta

'''
1 para NEGRO
2 para ROJO
'''
banderaApuesta = 0
color = None

def apostarNegro():
	global banderaApuesta

	b1.config(state=NORMAL)
	apuestaTexto.set("Apuesta a: NEGRO")
	banderaApuesta = 1

def apostarRojo():
	b1.config(state=NORMAL)
	aux = apuestaTexto.get()
	apuestaTexto.set("Apuesta a: ROJO")
	banderaApuesta = 2

def tirar():
	global color

	a = randint(0,36)
	if(a%2==0):
		if(a>10 and a<20):
			l1.config(bg="red")
			color = "red"
		elif(a>28 and a<36):
			l1.config(bg="red")
			color = "red"
		else:
			l1.config(bg="black")
			color = "black"
	else:
		if(a>9 and a<19):
			l1.config(bg="black")
			color = "black"
		elif(a>27 and a<37):
			l1.config(bg="black")
			color = "black"
		else:
			l1.config(bg="red")
			color = "red"
	if(a==0):
		l1.config(bg="green")
		color = "green"
	ruletaTexto.set(a)

	if(color=="black" and banderaApuesta==1):
		apuestaTexto.set("Gano!!!")

	b1.config(state=DISABLED)

ventana = Tk()
ventana.geometry("500x200")

ruletaTexto = StringVar()
ruletaTexto.set("0")
apuestaTexto = StringVar()
apuestaTexto.set("Apuesta a: ")
textoEstado = StringVar()

frameArriba = Frame(ventana, width=100, height=100)
frame1 = Frame(ventana, width=100, height=100)
frame2 = Frame(ventana, width=100, height=100)

lArriba = Label(frameArriba, textvariable=textoEstado, width=1, height=1, bg="white")
lArriba.pack(fill=BOTH, expand=1)

l1 = Label(frame1, textvariable=ruletaTexto, width=1, height=2, font=("Arial", 50, "bold"), bg="green", fg="white")
b1 = Button(frame1, text="TIRAR", command=tirar, width=1, height=1, state=DISABLED)
l1.pack(fill=BOTH, expand=1)
b1.pack(fill=BOTH, expand=1)

l2 = Label(frame2, textvariable=apuestaTexto, width=1, height=1, font=("Arial", 20), bg="white")
b2 = Button(frame2, text="NEGRO", command=apostarNegro, width=1, height=1)
b3 = Button(frame2, text="ROJO", command=apostarRojo, width=1, height=1)
l2.pack(fill=BOTH, expand=1)
b2.pack(fill=BOTH, expand=1, side=LEFT)
b3.pack(fill=BOTH, expand=1, side=LEFT)

frameArriba.pack(fill=BOTH, expand=1)
frame1.pack(fill=BOTH, expand=1, side=LEFT)
frame2.pack(fill=BOTH, expand=1, side=LEFT)

ventana.mainloop()