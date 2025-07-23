from tkinter import *
from tkinter import messagebox
ventana=Tk()
ventana.title("ejercicio")
ventana.geometry("400x400")
ventana.config(bd=24)
def sumar():
    try:
        resultado.set(float(numero1.get())+ float(numero2.get()))
    except:
        messagebox.showerror("Error","Introduce bien los datos")
        numero1.set("")
        numero2.set("")

def restar():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
        mostrarResultado()
    except:
        messagebox.showwerror("Error","Introducce bien los datos ")
        numero1.set("")
        numero2.set("")

def multiplicar():
    try:
         resultado.set(float(numero1.get()) * float(numero2.get()))
         mostrarResultado()
    except:
        messagebox.showwerror("Error","Introducce bien los datos ")
        numero1.set("")
        numero2.set("")

def dividir():
    try:
        resultado.set(float(numero1.get())/float(numero2.get()))
        mostrarRsulatdo()
    except:
        messagebox.showwerror("Error","Introducce bien los datos ")
        numero1.set("")
        numero2.set("")

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

Button(marco,text="sumar",command=sumar).pack(side="left",fill=X, expand=YES)
Button(marco,text="restar",command=restar).pack(side="left",fill=X, expand=YES)
Button(marco,text="dividir",command=dividir).pack(side="left",fill=X, expand=YES)
Button(marco,text="multiplicar",command=multiplicar).pack(side="left",fill=X, expand=YES)
ventana.mainloop()