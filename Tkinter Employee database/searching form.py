from searching function import search_employee_name
from tkinter import *

win=Tk()
win.title('Searching Employee Data')
win.geometry("400x400")

def submit():
    name=name_info.get()
    search_employee_name(name)
    
         
Label(text="Name:",font="20").place(x=30,y=40)
name_info=StringVar()
name=Entry(win,font="30",bd=3,textvariable=name_info)
name.place(x=80,y=40)

# sumbit button
btn=Button(win,text="Submit",font="30",bd=3,command=submit).place(x=280,y=35)
#btn.pack()


win.mainloop()







'''
from tkinter import *
root =Tk()

def search():
    pass
root.title('Searching Employee Data')
heading=Frame(root)
frame=Frame(root)
result=(root)
Label(heading,
      text="Search Employee Data",
      pady=20,
      font=("Times" ,30, "bold")).pack(side=TOP)
Label(frame,text="search Here:").pack(side=LEFT)
Label(result,
      text="Search results:",
      pady=1,
      font=("Arial",17)).pack(side=LEFT)

input_box=Entry(frame,width=50)

input_box.focus_set()

query=""
text=Text(root,font=("Robot",13),padx=55,pady=10)

button=Button(frame,text="search",command=search)
button.pack(side=RIGHT)
heading.pack()
frame.pack(side=TOP)
result.pack(side=TOP,fill=BOTH,pady=20,padx=50)
text.pack()
root.mainloop()
'''
