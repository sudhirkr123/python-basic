from tkinter import *
from tkinter import ttk
win = Tk()
frame1=Frame(win,width=300,highlightbackground="red",highlightthicknes=5)
frame1.grid(row=0,column=0,pady=20,ipadx=20,ipady=20)

li=Label(frame1,text="Enter any name:",fg="blue",font=(16))
li.grid(row=0,column=0,padx=10,pady=10)
textbox=Entry(frame1,fg='blue',font=(16))
textbox.grid(row=0,column=1)
button1=Button(frame1,text="Search",fg='blue',font=(16))
button1.grid(row=0,column=5,sticky=W)



win.mainloop()
