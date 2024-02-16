from tkinter import *
from tkinter import messagebox as mb
root=Tk()
def action():
    try:
        c=float(avalue.get())
        f=(9/5)*c+32
        mb.showinfo("Celsius to Fehrenheit",f"F={f}")
    except:
         mb.showerror("Error",'Enter valid value')
root.geometry('500x500')
root.minsize(250,250)
root.maxsize(500,500)
root.config(bg='lightgreen')
root.title('Celcius to fehrenheit')
a=Label(root,text="Enter temperature in Celsius:",font="Arial 20 bold")
a.pack()
avalue=StringVar()
aentry=Entry(root,textvariable=avalue)
aentry.pack()
b1=Button(root,text="CONVERT",fg="white",bg="black",command=action)
b1.pack()
root.mainloop()