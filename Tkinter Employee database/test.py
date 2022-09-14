













from tkinter import *
from tkinter import ttk


win = Tk()
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

        def update():

            emp_in=emp.get()
            print(emp_in)
            name_in=name.get()
    
            contact_in=contact.get()
            dept_in=dept.get()
            email_in=email.get()

        # sumbit button
        btn=Button(win,text="Updated",font="30",command=update).place(x=150,y=500)


Edit_form()

win.mainloop()



show='headings',
ttk.Treeview












'''
import re
def isvalid(num):
    pattern=re.compile('(0|91)?[-\s]?[6-9]\d{9}')
    return pattern.match(num)


num=input('enter the number:')
if isvalid(num):
    if len(num)==10:
        print("valid mobile number")
    else:
        print('invalid mobile number')
else:
    print('Invalid mobile number')
'''


'''
# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()
def search():
    tree = ttk.Treeview(win, column=("emp id", "Name", "contact","Dept","Email"), show='headings', height=5) # .place(x=60,y=100)

    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="emp id")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="contact")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Dept")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Email")

    data=[['124', 'Raju kumar', '9523614264', 'computer Science', 'Raju@gmail.com '],['456', 'Ramod kumar', '9097564534', 'computer science', 'ramod@gmail.com'],['345', 'Sudhir kumar', '5002237851', 'cs', 'sudhir@gmail.com']]
    # Insert the data in Treeview widget
    for i in range(len(data)):
        tree.insert('', 'end', text="1", values=(data[i][0],data[i][1], data[i][2],data[i][3],data[i][4]))
    tree.place(x=30,y=80)



# Set the size of the tkinter window
win.geometry("700x350")
'''
'''
Label(text="Name:",font="20").place(x=30,y=40)
name_info=StringVar()
name=Entry(win,font="30",bd=3,textvariable=name_info)
name.place(x=80,y=40)
'''
# sumbit button
#btn=Button(win,text="Search",font="30",bd=3,command=search).place(x=280,y=35)


# Create an object of Style widget
#style = ttk.Style()
#style.theme_use('clam')

# Add a Treeview widget
'''
frame1=Frame(win,width=500,highlightbackground="red",highlightthicknes=5)
frame1.grid(row=0,column=10,pady=20,ipadx=20,ipady=20)


Label(text="Name:",font="20").place(x=30,y=110)
emp_id=Entry(win,font="10",bd=4,textvariable=emp_info)
emp_id.place(x=130,y=70)
'''























'''
li=Label(frame1,text="Enter Emp id:",fg="blue",font=(16))
li.grid(row=0,column=0,padx=10,pady=10)

textbox=Entry(frame1,fg='blue',font=(16))
textbox.grid(row=0,column=1)

#lii=Label(frame1,text="Enter Name:",fg="blue",font=(16))
#lii.grid(row=0,column=2,padx=10,pady=10)

#textbox=Entry(frame1,fg='blue',font=(16))
#textbox.grid(row=0,column=1)




button1=Button(frame1,text="Search",fg='blue',font=(16))
button1.grid(row=0,column=3)
'''

'''
win.mainloop()
'''


'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#connection for phpmyadmin


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("Student Registration System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

def add():
    pass

label = Label(root, text="Student Registration System (CRUD MATRIX)", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

studidLabel = Label(root, text="Stud ID", font=('Arial', 15))
fnameLabel = Label(root, text="Firstame", font=('Arial', 15))
lnameLabel = Label(root, text="Lastame", font=('Arial', 15))
addressLabel = Label(root, text="Address", font=('Arial', 15))
phoneLabel = Label(root, text="Phone", font=('Arial', 15))

studidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
fnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
lnameLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
addressLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
phoneLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

studidEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
fnameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
lnameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
addressEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
phoneEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

studidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
fnameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
lnameEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
addressEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
phoneEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("Stud ID","Firstname","Lastname","Address","Phone")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Stud ID", anchor=W, width=170)
my_tree.column("Firstname", anchor=W, width=150)
my_tree.column("Lastname", anchor=W, width=150)
my_tree.column("Address", anchor=W, width=165)
my_tree.column("Phone", anchor=W, width=150)

my_tree.heading("Stud ID", text="Student ID", anchor=W)
my_tree.heading("Firstname", text="Firstname", anchor=W)
my_tree.heading("Lastname", text="Lastname", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading("Phone", text="Phone", anchor=W)

refreshTable()

root.mainloop()


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Inventory System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)
storeName = "Inventory System"



titleLabel = Label(root, text=storeName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

idLabel = Label(root, text="ID", font=('Arial bold', 15))
nameLabel = Label(root, text="Name", font=('Arial bold', 15))
priceLabel = Label(root, text="Price", font=('Arial bold', 15))
quantityLabel = Label(root, text="Quantity", font=('Arial bold', 15))
idLabel.grid(row=1, column=0, padx=10, pady=10)
nameLabel.grid(row=2, column=0, padx=10, pady=10)
priceLabel.grid(row=3, column=0, padx=10, pady=10)
quantityLabel.grid(row=4, column=0, padx=10, pady=10)

entryId = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryName = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryPrice = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryQuantity = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryId.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryName.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryPrice.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryQuantity.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=insert_data)
buttonEnter.grid(row=5, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
buttonUpdate.grid(row=5, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
buttonDelete.grid(row=5, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("ID", "Name", "Price", "Quantity")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=100)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("Price", anchor=W, width=150)
my_tree.column("Quantity", anchor=W, width=150)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()
'''


