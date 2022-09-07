from tkinter import *
win=Tk()
win.title("Master")
win.iconbitmap('anroid.ico')
#win.geometry('600*300')
win.maxsize(width=600,height=300)
win.minsize(width=600,height=300)


# function
def func():
    x=var.get()
    print(x)
    lbl.config(text=x)



lbl=Label(win,text="user Name:")
#lbl.pack()  # pack func
# lbl.grid(row=3,column=3)  # grid functon woring row & column
lbl.place(x=10,y=10)  # y mens top to bottom  x means left  to right



lbl=Label(win,text="nothing",bg="red",fg="white")
lbl.place(x=40,y=120) 

# entry
var = StringVar()
ent=Entry(win,bg="red",fg="white",bd=5,textvariable=var)
ent.place(x=80,y=10)


#button
btn= Button(win,text="Submit",bg='green',command=func)
btn.place(x=10,y=80)

 
win.mainloop()
