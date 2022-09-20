from Edit_form import Edit
from searching_form import searching
from deleting import delete_data
from Add_form import Adding1 
from displaying import display
from tkinter import *
from tkinter import ttk
win=Tk()
win.title('Main menu')
#win.maxsize(width=720,height=400)
#win.minsize(width=500,height=300)
win.geometry("520x200")
win.resizable(False,False)
#top=Toplevel()
def display1():
    top=Toplevel()
    display(top)

def adding1():
    top=Toplevel()
    Adding1(top)


def search1():
    top=Toplevel()
    searching(top)
    

def edit1():
    top=Toplevel()
    Edit(top)
   


def delete1():
    top=Toplevel()
    delete_data(top)

Label(win,text=" Main menu",bg="grey",font=("calibri",25)).pack()

btn=Button(win,text="Display",font="30",bd=3,command=display1).place(x=40,y=100)
btn=Button(win,text="Add records",font="30",bd=3,command=adding1).place(x=120,y=100)
btn=Button(win,text="Search",font="30",bd=3,command=search1).place(x=235,y=100)
btn=Button(win,text="Edit",font="30",bd=3,command=edit1).place(x=315,y=100)
btn=Button(win,text="Delete",font="30",bd=3,command=delete1).place(x=370,y=100)
win.mainloop()
