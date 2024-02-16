from tkinter import *
from tkinter import messagebox as mb
root=Tk()
root.config(bg="lightgreen")
def action():
    try:
        Weight=float(Weightentry.get())
        Height=float(Heightentry.get())
        BMI=Weight/(Height**2)
        mb.showinfo("BMI",f"{BMI:.4f}")
        Weightentry.delete(0,END)
        Heightentry.delete(0,END)
    except:
        mb.showerror("Error",'Enter valid value')
   
root.geometry('250x250')
root.minsize(250,200)
root.maxsize(500,500)

root.title('BMI Calculator')
Height=Label(root,text="Enter Height(in m)")
Weight=Label(root,text="Enter Weight(in Kg)")

Height.grid(row=2,column=0,padx=5,pady=5,sticky='W')#tk.w
Weight.grid(row=3,column=0,padx=5,pady=5)


Heightentry=Entry(root)
Weightentry=Entry(root)

Heightentry.grid(row=2,column=2,padx=5,pady=5)
Weightentry.grid(row=3,column=2,padx=5,pady=5)
submit=Button(root,text="SUBMIT",bg="black",fg="white",command=action)
submit.grid(row=5,column=2,padx=5,pady=5)
root.mainloop()