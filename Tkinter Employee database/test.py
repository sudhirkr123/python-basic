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

frame1=Frame(win,width=100,highlightbackground="red",highlightthicknes=5)
frame1.grid(row=0,column=0,pady=20,ipadx=20,ipady=20)

li=Label(frame1,text="Enter any name:",fg="blue",font=(16))
li.grid(row=0,column=0,padx=10,pady=10)
textbox=Entry(frame1,fg='blue',font=(16))
textbox.grid(row=0,column=1)
button1=Button(frame1,text="submit",fg='blue',font=(16))
button1.grid(row=0,column=5,sticky=W).pack(x=30,y=20)



win.mainloop()
