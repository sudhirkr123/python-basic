from Edit_form import Edit
from searching_form import searching
from deleting import delete_data
from Add_form import Adding1 
from displaying import display
from tkinter import *
from tkinter import ttk,messagebox
win=Tk()
win.title('Acufore Employee data')
win.geometry("620x200")
win.iconbitmap("D:\\sudhir\\basic python\\Tkinter Employee database\\icon\\acufore logo.ico")
win.resizable(False,False)
win['background']='pink'
#state= DISABLED
#top=Toplevel()


def display1():
    #global btn4
    
    #btn1[state] = 'disabled'
    display_btn['state'] = 'disabled'
    add_btn['state'] = 'disabled'
    search_btn['state'] = 'disabled'
    edit_btn['state'] = 'disabled'
    delete_btn['state'] = 'disabled'
    top=Toplevel()
    
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            top.destroy()
            add_btn['state'] = 'normal'
            search_btn['state'] = 'normal'
            edit_btn['state'] = 'normal'
            delete_btn['state'] = 'normal'
            display_btn['state'] = 'normal'
            
    display(top)
    top.protocol("WM_DELETE_WINDOW", on_closing)
    
       
def adding1():
    #btn4["state"] = DISABLED
    add_btn['state'] = 'disabled'
    display_btn['state'] = 'disabled'
    search_btn['state'] = 'disabled'
    edit_btn['state'] = 'disabled'
    delete_btn['state'] = 'disabled'
    
    top=Toplevel()

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            top.destroy()
            add_btn['state'] = 'normal'
            display_btn['state'] = 'normal'
            search_btn['state'] = 'normal'
            edit_btn['state'] = 'normal'
            delete_btn['state'] = 'normal'

          
    
    top.protocol("WM_DELETE_WINDOW", on_closing)
    Adding1(top)
    
    
    
    


def search1():
    search_btn['state'] = 'disabled'
    display_btn['state'] = 'disabled'
    add_btn['state'] = 'disabled'
    edit_btn['state'] = 'disabled'
    delete_btn['state'] = 'disabled'

    
    top=Toplevel()
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            top.destroy()
            add_btn['state'] = 'normal'
            display_btn['state'] = 'normal'
            edit_btn['state'] = 'normal'
            delete_btn['state'] = 'normal'
            search_btn['state'] = 'normal'
            
    
    top.protocol("WM_DELETE_WINDOW", on_closing)
    searching(top)
    
    

def edit1():
    edit_btn['state'] = 'normal'
    display_btn['state'] = 'disabled'
    search_btn['state'] = 'disabled'
    add_btn['state'] = 'disabled'
    delete_btn['state'] = 'disabled'
    top=Toplevel()
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            top.destroy()
            add_btn['state'] = 'normal'
            search_btn['state'] = 'normal'
            display_btn['state'] = 'normal'
            delete_btn['state'] = 'normal'
            edit_btn['state'] = 'normal'

            
    
    top.protocol("WM_DELETE_WINDOW", on_closing)
    Edit(top)
    
    

    
    
                                                                    

def delete1():
    delete_btn['state'] = 'disabled'
    display_btn['state'] = 'disabled'
    search_btn['state'] = 'disabled'
    add_btn['state'] = 'disabled'
    edit_btn['state'] = 'disabled'
    top=Toplevel()
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            top.destroy()
            delete_btn['state'] = 'normal'
            add_btn['state'] = 'normal'
            search_btn['state'] = 'normal'
            edit_btn['state'] = 'normal'
            display_btn['state'] = 'normal'
      
    

    
    top.protocol("WM_DELETE_WINDOW", on_closing)
    delete_data(top)


Label(win,text="Acufore Employee Database",bg="pink",font=("calibri",25)).pack()



display_btn=Button(win,text="Display",font="30",bd=3,command=display1,height= 1, width=10)
display_btn.place(x=30,y=100)


add_btn=Button(win,text="Add records",font="30",bd=3,command=adding1,height= 1, width=10)
add_btn.place(x=140,y=100)


search_btn=Button(win,text="Search",font="30",bd=3,command=search1,height= 1, width=10)
search_btn.place(x=250,y=100)


edit_btn=Button(win,text="Edit",font="30",bd=3,command=edit1,height= 1, width=10)
edit_btn.place(x=360,y=100)



delete_btn=Button(win,text="Delete",font="30",bd=3,command=delete1,height= 1, width=10)
delete_btn.place(x=470,y=100)

footer =Frame(win, height=30)
Label(footer,text="© 2020-22 Acufore India Pvt.Ltd. All Rights Reserved").pack()
footer.pack(fill='both', side='bottom')



def on_closing():
        if messagebox.askokcancel("Exit", "Do you want to Exit?"):
            win.destroy()




win.protocol("WM_DELETE_WINDOW", on_closing)

win.mainloop()
