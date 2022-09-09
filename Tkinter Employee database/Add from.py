
from csvHandler import append_employeeDetails 
from tkinter import *
from tkinter import ttk,messagebox



win=Tk()
win.title('Add Employee Data')
win.geometry("400x400")
win.resizable(False,False)

def submit():
    emp=emp_info.get()
    name=name_info.get()
    contact=contact_info.get()
    dept=dept_info.get()
    email=email_info.get()


    

    # validate data
    if emp=="":
        messagebox.showerror("Error","Please emp_id")
    elif name=="":
        messagebox.showerror("Error","please enter name")
    elif contact=="" and len(contact) not in 10:
        messagebox.showerror("Error","please enter contact")
        
    elif dept=="":
        messagebox.showerror("Error","please enter dept")
    elif email=="":
        messagebox.showerror("Error","please enter email")

    else:
        Label(win,
              text="Employee data added successfuly",
              font="20",
              fg="green").place(x=110,y=265)
        append_employeeDetails(emp,name,contact,dept,email)

        
    









# label
Label(text="Add Employee Data",bg="grey",font=("calibri",25)).pack()
Label(text="Employee Id:",font="20").place(x=30,y=70)
Label(text="Name:",font="20").place(x=30,y=110)
Label(text="Contact:",font="20").place(x=30,y=150)
Label(text="Dept:",font="20").place(x=30,y=190)
Label(text="Email:",font="20").place(x=30,y=230)



# entry



emp_info=StringVar()
name_info=StringVar()
contact_info=StringVar()
dept_info=StringVar()
email_info=StringVar()

emp_id=Entry(win,font="10",bd=4,textvariable=emp_info)
emp_id.place(x=130,y=70)
name=Entry(win,font="10",bd=4,textvariable=name_info)
name.place(x=130,y=110)
contact=Entry(win,font="10",bd=4,textvariable=contact_info)
contact.place(x=130,y=150)
Dept=Entry(win,font="10",bd=4,textvariable=dept_info)
Dept.place(x=130,y=190)
Email=Entry(win,font="10",bd=4,textvariable=email_info)
Email.place(x=130,y=230)

# sumbit button
btn=Button(win,text="Submit",font="30",command=submit).place(x=180,y=290)
#btn.pack()

win.mainloop()







