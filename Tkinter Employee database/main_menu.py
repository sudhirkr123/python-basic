from Edit_form import Edit
from searching_form import searching
from deleting import delete_data
from Add_form import Adding1 
from displaying import display
from tkinter import *
from tkinter import ttk
win=Tk()
win.title('AcuforeEmployee data')
win.geometry("520x200")
win.iconbitmap("D:\\sudhir\\basic python\\Tkinter Employee database\\icon\\acufore logo.ico")
win.resizable(False,False)
#state= DISABLED
#top=Toplevel()

def display1():
    #global btn4
    
    #btn1[state] = 'disabled'
    add_btn['state'] = 'disabled'
    search_btn['state'] = 'disabled'
    edit_btn['state'] = 'disabled'
    delete_btn['state'] = 'disabled'
    
    '''
    btn4["state"] = DISABLED
    btn3["state"] = DISABLED
    btn2["state"] = DISABLED
    btn1["state"] = DISABLED
    '''
    top=Toplevel()
    display(top)

    
    
   

def adding1():
    #btn4["state"] = DISABLED
    display_btn['state'] = 'disabled'
    search_btn['state'] = 'disabled'
    edit_btn['state'] = 'disabled'
    delete_btn['state'] = 'disabled'
    
    top=Toplevel()
    Adding1(top)
    #add_btn['state'] = 'disabled'


def search1():
    display_btn['state'] = 'disabled'
    add_btn['state'] = 'disabled'
    edit_btn['state'] = 'disabled'
    delete_btn['state'] = 'disabled'
    
    top=Toplevel()
    searching(top)
    

def edit1():
    display_btn['state'] = 'disabled'
    search_btn['state'] = 'disabled'
    add_btn['state'] = 'disabled'
    delete_btn['state'] = 'disabled'
    top=Toplevel()
    Edit(top)
                                                                    

def delete1():
    display_btn['state'] = 'disabled'
    search_btn['state'] = 'disabled'
    add_btn['state'] = 'disabled'
    edit_btn['state'] = 'disabled'
    top=Toplevel()
    delete_data(top)



Label(win,text="Acufore Employee Details",bg="grey",font=("calibri",25)).pack()



display_btn=Button(win,text="Display",font="30",bd=3,command=display1,state='normal')
display_btn.place(x=40,y=100)

add_btn=Button(win,text="Add records",font="30",bd=3,command=adding1)
add_btn.place(x=120,y=100)

search_btn=Button(win,text="Search",font="30",bd=3,command=search1)
search_btn.place(x=235,y=100)

edit_btn=Button(win,text="Edit",font="30",bd=3,command=edit1)
edit_btn.place(x=315,y=100)

delete_btn=Button(text="Delete",font="30",bd=3,command=delete1)
delete_btn.place(x=370,y=100)

win.mainloop()
