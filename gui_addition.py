from tkinter import *
from tkinter import messagebox as mb
def action():
    try:
        num1=float(firstvalue.get())
        num2=float(secondsvalue.get())
        result=num1+num2
        mb.showinfo("Result",f"The sum is :{result}")
    except:
        mb.showerror("Error","Enter valid number")

    
root=Tk()
root.geometry('500x500')
root.minsize(250,250)
root.maxsize(500,500)
a=Label(root,text="Welcome To Calculate me")
a.grid(row=0,column=2)
first=Label(root,text="Enter first number")
second=Label(root,text="Enter second number")
first.grid(row=2,column=0)
second.grid(row=3,column=0)
firstvalue=StringVar()
secondsvalue=StringVar()


firstentry=Entry(root,textvariable=firstvalue)
secondsentry=Entry(root,textvariable=secondsvalue)
firstentry.grid(row=2,column=2)
secondsentry.grid(row=3,column=2)

submit=Button(root,text="SUBMIT",bg="black",fg="white",command=action)
submit.grid(row=7,column=2)
root.mainloop()