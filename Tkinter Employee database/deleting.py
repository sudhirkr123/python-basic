from moduleFunc import search_employee_name,delete
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def delete_data(win):
    win.title("Delete Data")
    win.geometry("1050x340")
    win.iconbitmap("D:\\sudhir\\basic python\\Tkinter Employee database\\icon\\delete.ico")
    win.resizable(False,False)
    Label(win,text="Delete Employee Data",bg="yellow",font=("calibri",25)).pack()

    # tree =ttk.Treeview(win, column=("Employee ID", "Name", "Contact","Department","Email"),show='headings',height=5)

    def search():
        name=name_info.get()
        data=search_employee_name(name)
    
        if name=="":
            # win.destroy()
            messagebox.showerror("Error","please enter name")
        
        elif len(data)<=0:
            messagebox.showerror("Error","Records not found")
            tree=ttk.Treeview(win, column=("Employee ID", "Name", "Contact","Department","Email"),show='headings',height=5) # .place(x=60,y=100)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Records not founds")
            tree.place(x=20,y=130)
            '''

            m=Label(win,
                  text="Records not found",
                      font="20",
                  fg="#f72036")
            m.place(x=20,y=200)
        
            '''
        
        else:
        
            tree=ttk.Treeview(win, column=("Employee ID", "Name", "Contact","Department","Email"),show='headings',height=5) # .place(x=60,y=100)
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
            def select_item(a):
                y=tree.item(tree.selection())
                emp=(y['values'][0])
                value=str(emp)
                def delete1():
                    messagebox.showinfo(title="Delete",message="Employee data delete successfuly")
                    delete(value)
                
                btn=Button(win,text="Delete",font="30",bd=3,command=delete1).place(x=500,y=270)

            tree.bind('<ButtonRelease-1>',select_item)

    Label(win,text="Name:",font="20").place(x=30,y=60)
    name_info=StringVar()
    name=Entry(win,font="30",bd=3,textvariable=name_info)
    name.place(x=80,y=60)

    # sumbit button
    btn=Button(win,text="Search",font="30",bd=3,command=search).place(x=280,y=55)

    Label(win,text="Search Data",font=("Bodoni MT Black",20)).place(x=25,y=100)



    win.mainloop()


