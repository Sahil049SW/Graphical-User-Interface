from tkinter import *

window=Tk()
window.title("My GUI App")
window.geometry("500x400")
welcomeMsg=Label(window,text="Hello World..!!")
welcomeMsg.pack()
def exitFun():
    window.destroy()

def addFun():
    f1=float(FirstNummberEntry.get())
    f2=float(SecondNummberEntry.get())
    Reasult=f1+f2
    reasult_label.config(text=f'Result : {Reasult}')

    
def SubFun():
    f1=float(FirstNummberEntry.get())
    f2=float(SecondNummberEntry.get())
    Reasult=f1-f2
    reasult_label.config(text=f'Result : {Reasult}')
def Mulfun():
    f1=float(FirstNummberEntry.get())
    f2=float(SecondNummberEntry.get())
    Reasult=f1*f2
    reasult_label.config(text=f'Result : {Reasult}')
def divFun():
    f1=float(FirstNummberEntry.get())
    f2=float(SecondNummberEntry.get())
    Reasult=f1/f2
    reasult_label.config(text=f'Result : {Reasult}')



f1=Frame(window)
FirstNummber=Label(f1,text="Enter First Number: ")
FirstNummber.pack(side=LEFT)
FirstNummberEntry=Entry(f1)
FirstNummberEntry.pack(side=RIGHT)
f1.pack()


f2=Frame(window)
SecondNummber=Label(f2,text="Enter Second Number: ")
SecondNummber.pack(side=LEFT)
SecondNummberEntry=Entry(f2)
SecondNummberEntry.pack(side=LEFT)
f2.pack()


f3=Frame(window)
AddBtn=Button(f3,text='Add',bg='green', command=addFun)
AddBtn.pack(side=LEFT)
exitBtn=Button(f3,text='exit',bg='red', command=exitFun)
exitBtn.pack(side=RIGHT)
f3.pack()


f4=Frame(window)
subBtn=Button(f4,text='substrate',bg='yellow',command=SubFun)
subBtn.pack(side=LEFT)
MulBtn=Button(f4,text='multiplate',bg='grey',command=Mulfun)
MulBtn.pack(side=RIGHT)
divBtn=Button(f4,text='divide',bg='purple',command=divFun)
divBtn.pack(side=LEFT)
f4.pack()
reasult_label=Label(window,text='Reasult')
reasult_label.pack()


window.mainloop()