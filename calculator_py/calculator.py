
import math
from tkinter  import *
from tkinter import ttk
import math


root = Tk()
root.title("calculator")
root.geometry("+500+80")

estilos = ttk.Style()
estilos.configure ('mainframe.TFrame',background='#CECECE')
estilos.theme_use('clam')
mainframe = ttk.Frame(root,style="mainframe.TFrame")
mainframe.grid(column=0,row=0)


#estilos labels
estilos_label_1 = ttk.Style()
estilos_label_1.configure('Label1.TLabel', font="arial 15", anchor="E")

estilos_label_2 = ttk.Style()
estilos_label_2.configure('Label2.TLabel', font = "arial 15", anchor="E")
#generando widget  col 0 fil0

#entrada de texto
entrada1= StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable =entrada1 , style="Label1.TLabel")
label_entrada1.grid(column=0,row=0, columnspan=4, sticky=(W,E))

#entrada de texto
entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable = entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0,row=1,columnspan=4, sticky=(W,E))

#estilos de los btones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('botones_numeros.TButton', font="arial 32", width=5, background="#CECECE", relief="flat")
estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('botones_borrar.TButton', font="arial 32", width=5, background="#CECECE", relief="flat")
estilos_botones_borrar.map('botones_borrar.TButton', foreground =[('active','#FF0000')],background=[('active','#858585')])
estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('botones_restantes.TButton', font="arial 32", width=5, background="#CECECE", relief="flat")
#creando botones
button0 = ttk.Button(mainframe, text="0",style='botones_numeros.TButton')
button1 = ttk.Button(mainframe, text="1",style='botones_numeros.TButton')
button2 = ttk.Button(mainframe, text="2",style='botones_numeros.TButton')
button3 = ttk.Button(mainframe, text="3",style='botones_numeros.TButton')
button4 = ttk.Button(mainframe, text="4",style='botones_numeros.TButton')
button5 = ttk.Button(mainframe, text="5",style='botones_numeros.TButton')
button6 = ttk.Button(mainframe, text="6",style='botones_numeros.TButton')
button7 = ttk.Button(mainframe, text="7",style='botones_numeros.TButton')
button8 = ttk.Button(mainframe, text="8",style='botones_numeros.TButton')
button9 = ttk.Button(mainframe, text="9",style='botones_numeros.TButton')
button10 = ttk.Button(mainframe, text="10",style='botones_numeros.TButton')

#botones operaciones
button_borrar = ttk.Button(mainframe, text="<--",style='botones_borrar.TButton')
button_borrar_todo = ttk.Button(mainframe,text="C",style='botones_borrar.TButton')
button_parentesis1 = ttk.Button(mainframe,text="(",style='botones_restantes.TButton')
button_parentesis2 = ttk.Button(mainframe,text=")",style='botones_restantes.TButton')
button_punto = ttk.Button(mainframe,text=".",style='botones_restantes.TButton')
button_igual = ttk.Button(mainframe,text="=",style='botones_restantes.TButton')

button_division = ttk.Button(mainframe,text="/",style='botones_restantes.TButton')
button_multiplicacion = ttk.Button(mainframe,text="x",style='botones_restantes.TButton')
button_resta = ttk.Button(mainframe,text="-",style='botones_restantes.TButton')
button_suma = ttk.Button(mainframe,text="+",style='botones_restantes.TButton')
button_raiz_cuadrada = ttk.Button(mainframe,text="√",style='botones_restantes.TButton')


#colocando botones en pantalla
button_parentesis1.grid(column=0, row=2)
button_parentesis2.grid(column=1, row=2)
button_borrar_todo.grid(column=2, row=2)
button_borrar.grid(column=3, row=2)

button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)
button_division.grid(column=3, row=3)
button4.grid(column=0, row=4)
button5.grid(column=1, row=4)
button6.grid(column=2, row=4)
button_multiplicacion.grid(column=3, row=4)

button1.grid(column=0, row=5)
button2.grid(column=1, row=5)
button3.grid(column=2, row=5)
button_suma.grid(column=3, row=5)

button0.grid(column=0, row=6, columnspan=2,sticky=(W,E))
button_punto.grid(column=2, row=6)
button_resta.grid(column=3, row=6)

button_igual.grid(column=0, row=7,columnspan=3,sticky=(W,E))
button_raiz_cuadrada.grid(column=3, row=7)

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10 ,padx=1, pady=1)


#nn
root.mainloop()
