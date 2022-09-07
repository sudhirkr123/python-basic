import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title('ADD GUI')
'''
fm=Frame(win)
fm.pack(fill=BOTH)
Button(fm,text="Button1",fg="red").pack()
Button(fm,text="Button2",fg="blue").pack()
Button(fm,text="Button3",fg="yellow").pack(side=LEFT)
'''
# create labels
name_lable=ttk.Label(win,text="Enter your name:")
name_lable.grid(row=0,column=0,sticky=tk.W)

contact_lable=ttk.Label(win,text="Enter your contact:")
contact_lable.grid(row=1,column=0,sticky=tk.W)

Email_lable=ttk.Label(win,text="Enter your Email:")
Email_lable.grid(row=3,column=0,sticky=tk.W)

Dept_lable=ttk.Label(win,text="Enter your Dept:")
Dept_lable.grid(row=4,column=0,sticky=tk.W)

# create entry box
name_var = tk.string()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
'''
contact_var=tk.stringVar()
contact_entrybox=ttk.Entry(win,width=16,textvariable=contact_var)
contact_entrybox.grid(row=1,column=1)

Email_var=tk.stringVar()
Email_entrybox=ttk.Entry(win,width=16,textvariable=Email_var)
Email_entrybox.grid(row=2,column=1)

dep_var=tk.stringVar()
dept_entrybox=ttk.Entry(win,width=16,textvariable=dept_var)
dept_entrybox.grid(row=3,column=1)
'''




win.mainloop()
