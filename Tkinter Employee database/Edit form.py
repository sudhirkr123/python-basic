
from searchingFunc import search_employee_name
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


win=Tk()
win.title('Searching Employee Data')
#win.maxsize(width=720,height=400)
#win.minsize(width=500,height=300)
win.geometry("1050x1050")
#win.resizable(False,False)
Label(text="Update Employee Data Form",bg="grey",font=("calibri",25)).pack()



class Edit_form:
    def __init__(self):
        
        Label(text="------Edit From---------",font="20").place(x=60,y=300)
        Label(text="Employee Id:",font="20").place(x=30,y=340)
        Label(text="Name:",font="20").place(x=30,y=370)
        Label(text="Contact:",font="20").place(x=30,y=400)
        Label(text="Dept:",font="20").place(x=30,y=430)
        Label(text="Email:",font="20").place(x=30,y=460)

        # entry
        emp=StringVar()
        name=StringVar()
        contact=StringVar()
        dept=StringVar()
        email=StringVar()

        emp_id=Entry(win,font="10",bd=4,textvariable=emp)
        emp_id.place(x=130,y=340)
        name=Entry(win,font="10",bd=4,textvariable=name)
        name.place(x=130,y=370)
        contact=Entry(win,font="10",bd=4,textvariable=contact)
        contact.place(x=130,y=400)
        dept=Entry(win,font="10",bd=4,textvariable=dept)
        dept.place(x=130,y=430)
        email=Entry(win,font="10",bd=4,textvariable=email)
        email.place(x=130,y=460)
        #btn=Button(win,text="Updated",font="30",command=update).place(x=150,y=500)

        def update():

            emp_in=emp.get()
            print(emp_in)
            name_in=name.get()
    
            contact_in=contact.get()
            dept_in=dept.get()
            email_in=email.get()

         #sumbit button
        btn=Button(win,text="Updated",font="30",command=update).place(x=150,y=500)

def search():
    name=name_info.get()
    data=search_employee_name(name)


    if name=="":
        messagebox.showerror("Error","please enter name")
    
        
    elif len(data)>0:
    
        Edit_form()
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

        tree.bind('<ButtonRelease-1>') 
        treeview =tree

        ttk.Style().configure("Treeview", font= ('', 8), background="#383838", 
        foreground="white", fieldbackground="yellow")

    
        # Insert the data in Treeview widget
        for i in range(len(data)):
            tree.insert('', 'end', text="1", values=(data[i][0],data[i][1], data[i][2],data[i][3],data[i][4]))
            #print(data[i])
        tree.place(x=20,y=150)
        y=tree.item(tree.selection())
        item=tree.selection()
        print(item)

        

        
       
    else:
        Label(win,
              text="Records not found",
              font="20",
              fg="#f72036").place(x=40,y=150)






        




# searching label name
        
Label(text="Name:",font="20").place(x=30,y=60)
name_info=StringVar()
name=Entry(win,font="30",bd=3,textvariable=name_info)
name.place(x=80,y=60)

# sumbit button
btn=Button(win,text="Search",font="30",bd=3,command=search).place(x=280,y=55)

Label(text="Search Data",font=("Bodoni MT Black",20)).place(x=25,y=100)


win.mainloop()
