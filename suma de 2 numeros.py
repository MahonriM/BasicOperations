from tkinter import *
def suma():
    try:
        _num1 = int(val1.get())
        _num2 = int(val2.get())
        s = _num1 + _num2
        lbl3.configure(text=s)
    except:
        lbl3.configure(text="Ha ocurrido un error")
def resta():
    try:
        _num1 = int(val1.get())
        _num2 = int(val2.get())
        s = _num1 - _num2
        lbl3.configure(text=s)
    except:
        lbl3.configure(text="Ha ocurrido un error")
def multi():
    try:
        _num1 =int(val1.get())
        _num2=int(val2.get())
        s =_num1*_num2
        lbl3.configure(text="La multiplicacion es {0}".format(s))
    except:
        lbl3.configure(text="Ha ocurrido un error")
#Suma Especial con .__add__
def espsum():
    _num1=int(val1.get())
    _num2=int(val2.get())
    s=_num1.__add__(_num2)
    lbl3.configure(text="La suma es {0}".format(s))
def div():
    _num1=int(val1.get())
    _num2=int(val2.get())
    s=_num1.__truediv__(_num2)
    lbl3.configure(text="La division es {0}".format(s))
vtn=Tk()
vtn.title("Operaciones basicas")
fr=Frame(vtn)
fr.grid(column=0,row=0,padx=(100,100),pady=(50,50))
fr.columnconfigure(0,weight=2)
fr.rowconfigure(0,weight=2)
lbl3=Label(fr)
lbl3.grid(column=3,row=4)
lbl=Label(fr,text="Ingresa un numero")
lbl.grid(column=2,row=2,sticky=(W,E))
lbl1=Label(fr,text="Ingresa otro numero")
lbl1.grid(column=2,row=3,sticky=(W,E))
btn=Button(fr,text="Sumar",command=espsum)
btn.grid(column=4,row=4)
num1=""
num2=""
val1=Entry(fr,width=10,textvariable=num1)
val1.grid(column=3,row=2)
val2=Entry(fr,width=10,textvariable=num2)
val2.grid(column=3,row=3)
btn1=Button(fr,text="Resta",command=resta)
btn1.grid(column=4,row=5)
btn2=Button(fr,text="Multiplicacion",command=multi)
btn2.grid(column=4,row=6)
btn3=Button(fr,text="Division",command=div)
btn3.grid(column=4,row=7)
fr.mainloop()