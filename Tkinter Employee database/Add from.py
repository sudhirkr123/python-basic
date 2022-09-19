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

    # Checking text box 
    if emp=="":
        messagebox.showerror("Error","Please emp id")
    elif name=="":
        messagebox.showerror("Error","please enter name")
    elif contact=="":
        messagebox.showerror("Error","please enter contact")

    elif len(contact)!=10: # or contact[0]!='6' or contact[0]!='7' or contact[0]!='8' or contact[0]!='9':
        messagebox.showerror("Error","worng contact")
    elif dept=="":
        messagebox.showerror("Error","please enter dept")
    elif email=="":
        messagebox.showerror("Error","please enter email")

    else:
        messagebox.showinfo(title="Added",message="Employee data added successfuly")
        
        '''
        Label(win,
              text="Employee data added successfuly",
              font="20",
              fg="green")
        place(x=110,y=265)
        '''
        append_employeeDetails(emp,name,contact,dept,email)

# clean the text box
def clear():
    emp_id.delete(0,END)
    name.delete(0,END)
    contact.delete(0,END)
    dept.delete(0,END)
    email.delete(0,END)
    

        
    
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
dept=Entry(win,font="10",bd=4,textvariable=dept_info)
dept.place(x=130,y=190)
email=Entry(win,font="10",bd=4,textvariable=email_info)
email.place(x=130,y=230)
# sumbit button
btn=Button(win,text="Submit",font="30",command=submit).place(x=150,y=290)
btn=Button(win,text="Clear",font="30",command=clear).place(x=230,y=290)

win.mainloop()

