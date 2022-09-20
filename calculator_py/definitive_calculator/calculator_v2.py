from tkinter import *
from unittest import result
i=0
ventana = Tk()
ventana.title("calculadora")


#Entrada
e_texto = Entry(ventana,font = ("Calibri 20"))
e_texto.grid(row =0, column=0, columnspan =4, padx=5, pady=5)

#botones
boton_0 = Button(ventana,text="0", width=5,height=2,command=lambda:click_boton(0))
boton_1 = Button(ventana,text="1", width=5,height=2,command=lambda:click_boton(1))
boton_2 = Button(ventana,text="2", width=5,height=2,command=lambda:click_boton(2))
boton_3 = Button(ventana,text="3", width=5,height=2,command=lambda:click_boton(3))
boton_4 = Button(ventana,text="4", width=5,height=2,command=lambda:click_boton(4))
boton_5 = Button(ventana,text="5", width=5,height=2,command=lambda:click_boton(5))
boton_6 = Button(ventana,text="6", width=5,height=2,command=lambda:click_boton(6))
boton_7 = Button(ventana,text="7", width=5,height=2,command=lambda:click_boton(7))
boton_8 = Button(ventana,text="8", width=5,height=2,command=lambda:click_boton(8))
boton_9 = Button(ventana,text="9", width=5,height=2,command=lambda:click_boton(9))

boton_borrar = Button(ventana,text="AC", width=5,height=2,command=lambda:borrar())
boton_parentesis_1= Button(ventana,text="(", width=5,height=2,command=lambda:click_boton("("))
boton_parentesis_2 = Button(ventana,text=")", width=5,height=2,command=lambda:click_boton(")"))
boton_punto = Button(ventana,text=".", width=5,height=2,command=lambda:click_boton("."))

boton_div = Button(ventana,text="/", width=5,height=2,command=lambda:click_boton("/"))
boton_mult = Button(ventana,text="*", width=5,height=2,command=lambda:click_boton("*"))
boton_sum = Button(ventana,text="+", width=5,height=2,command=lambda:click_boton("+"))
boton_rest = Button(ventana,text="-", width=5,height=2,command=lambda:click_boton("-"))
boton_igual = Button(ventana,text="=", width=5,height=2,command=lambda:operacion())


#agregando botones a pantalla

boton_1.grid(row=4,column=0,padx=5,pady=5)
boton_2.grid(row=4,column=1,padx=5,pady=5)
boton_3.grid(row=4,column=2,padx=5,pady=5)
boton_rest.grid(row=4,column=3,padx=5,pady=5)

boton_4.grid(row=3,column=0,padx=5,pady=5)
boton_5.grid(row=3,column=1,padx=5,pady=5)
boton_6.grid(row=3,column=2,padx=5,pady=5)
boton_sum.grid(row=3,column=3,padx=5,pady=5)

boton_7.grid(row=2,column=0,padx=5,pady=5)
boton_8.grid(row=2,column=1,padx=5,pady=5)
boton_9.grid(row=2,column=2,padx=5,pady=5)
boton_mult.grid(row=2,column=3,padx=5,pady=5)

boton_borrar.grid(row=1,column=0,padx=5,pady=5)
boton_parentesis_1.grid(row=1,column=1,padx=5,pady=5)
boton_parentesis_2.grid(row=1,column=2,padx=5,pady=5)
boton_punto.grid(row=1,column=3,padx=5,pady=5)

boton_0.grid(row=5,column=0,columnspan=2,padx=5,pady=5,sticky=(W))
boton_div.grid(row=5,column=1,padx=5,pady=5)
boton_igual.grid(row=5,column=2,padx=5,pady=5)


#funciones

def click_boton(valor):
    global i
    e_texto.insert(i,valor)
    i += 1

def borrar():
    e_texto.delete(0,END)
    i = 0

def operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i = 0

ventana.mainloop()