from moduleFunc import search_employee_name,delete
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win=Tk()
win.geometry("1050x1050")
win.title('Delete Data')
Label(text='Delete Employee Data',bg="yellow",font=("calibri",25)).pack()



def search():
    name=name_info.get()
    data=search_employee_name(name)
    
    if name=="":
        messagebox.showerror("Error","please enter name")
        
    elif len(data)<0:
        Label(win,
              text="Records not found",
              font="20",
              fg="#f72036").place(x=40,y=150)
        
                    
    else:
        tree =ttk.Treeview(win, column=("Employee ID", "Name", "Contact","Department","Email"),show='headings',height=5) # .place(x=60,y=100)
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
        for i in range(len(data)):
            tree.insert('', 'end', text="1", values=(data[i][0],data[i][1], data[i][2],data[i][3],data[i][4]))
            #print(data[i])
        tree.place(x=20,y=130)


        #btn=Button(win,text="delete",font="30",bd=3,command=delete).place(x=40,y=270)
        
        def select_item(a):
            #item=tree.place(x=20,y=150)
            y=tree.item(tree.selection())
            emp=(y['values'][0])
            value=str(emp)
            #print(type(y['values']))
            btn=Button(win,text="delete",font="30",bd=3,command=delete(value)).place(x=40,y=270)
           
        tree.bind('<ButtonRelease-1>',select_item)



Label(text="Name:",font="20").place(x=30,y=60)
name_info=StringVar()
name=Entry(win,font="30",bd=3,textvariable=name_info)
name.place(x=80,y=60)

# sumbit button
btn=Button(win,text="Search",font="30",bd=3,command=search).place(x=280,y=55)

Label(text="Search Data",font=("Bodoni MT Black",20)).place(x=25,y=100)



win.mainloop()
