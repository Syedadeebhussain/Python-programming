from tkinter import *
from tkinter import messagebox as mb
root=Tk()
def action():
    #mb.showinfo('Greeting','hello,'+msgentry.get())#showerror
    a=int(msgentry.get())
    c=0
    if a==1:
        mb.showinfo("Greeting","Neither composite nor prime")
        
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        mb.showinfo('ans','a prime number')
    else:
        mb.showinfo('ans','not a prime number')

root.geometry('250x250')
root.minsize(200,200)
root.maxsize(250,250)
root.title('Greeting message box')
root.config(bg='skyblue')
msg=Label(root,text="Enter your name",bg='black',fg='white',font="Arial 15 bold")
msg.pack(padx=5,pady=5)
msgentry=Entry(root)
msgentry.pack(padx=5,pady=5)
bt=Button(root,text='SUBMIT',command=action)
bt.pack(padx=5,pady=5)
root.mainloop()