from tkinter import *
from tkinter import messagebox
ventana=Tk()
ventana.title("ejercicio")
ventana.geometry("400x400")
ventana.config(bd=24)


numero1=StringVar()
numero2=StringVar()
resultado=StringVar()
numero1.set("")
numero2.set("")
#crear marco 
marco=Frame(ventana,width=250,heigh=200)
marco.config(padx=15,
             pady=15,
             bd=5,
             )
marco.pack(side=TOP,anchor=CENTER)
marco.pack_propagate(False)

Label(marco,text="primer numero:").pack()
Entry(marco,textvariable=numero1,justify="center").pack()
Label(marco,text="segundo numero:").pack()
Entry(marco,textvariable=numero2,justify="center").pack()

ventana.mainloop()