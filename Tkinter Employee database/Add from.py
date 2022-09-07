from tkinter import *
from tkinter import ttk


def add():
    print(emp_info.get())
    print(name_info.get())
    print(contact_info.get())
    print(dept_info.get())
    print(email_info.get())
    
    




win=Tk()
win.title('Add Employee Data')
win.geometry("400x400")

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
btn=Button(win,text="Submit",font="30",command=add).place(x=180,y=290)
#btn.pack()


win.mainloop()



