from moduleFunc import list_cleaning
from tkinter import *
from tkinter import ttk

win=Tk()
win.title('All Employee Data')
#win.maxsize(width=720,height=400)
#win.minsize(width=500,height=300)
win.geometry("1050x1050")
#win.resizable(False,False)
Label(win,text=" All Employee Data",bg="grey",font=("calibri",25)).pack()

def display():
    tree =ttk.Treeview(win, column=("Employee ID", "Name", "Contact","Department","Email"),show='headings',height=8) # .place(x=60,y=100)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Employee ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Contact")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Department")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Email")

    
    # Insert the data in Treeview widget
    data=list_cleaning()
    for i in range(len(data)):
        tree.insert('', 'end', text="1", values=(data[i][0],data[i][1], data[i][2],data[i][3],data[i][4]))
    tree.place(x=20,y=100)

display()

