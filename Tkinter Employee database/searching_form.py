from moduleFunc import search_employee_name
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def searching(win):
    #win=Tk()
    win.title('Searching Employee Data')
    #win.maxsize(width=720,height=400)
    #win.minsize(width=500,height=300)
    win.geometry("1080x300")
    win.iconbitmap("D:\\sudhir\\basic python\\Tkinter Employee database\\icon\\search.ico")
    win.resizable(False,False)
   

    def search():
        name=name_info.get()
        data=search_employee_name(name)

        if name=="":
            messagebox.showerror("Error","please enter name")
    
        
        elif len(data)>=1:
            '''
            tree = ttk.Treeview(win,column=("Employee ID", "Name", "Contact","Department","Email"),show='headings',height=8,selectmode='browse')
            tree.place(x=30, y=95)
    
            vsb = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
            vsb.place(x=20+1000+2, y=95, height=170+20)

            tree.configure(yscrollcommand=vsb.set)
            '''
            tree = ttk.Treeview(win, column=("Employee ID", "Name", "Contact","Department","Email"), show='headings', height=5) # .place(x=60,y=100)
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
                tree.insert('','end',text="1",values=(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]))
            tree.place(x=20,y=130)

            
        else:
            messagebox.showerror("Error","Record not found")
            tree = ttk.Treeview(win, column=("Employee ID", "Name", "Contact","Department","Email"), show='headings', height=5) # .place(x=60,y=100)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Record not found")
            tree.place(x=20,y=130)
        

            '''
            Label(win,
                  text="Records not found",
                  font="20",
                  fg="#f72036").place(x=40,y=130)
            '''

         
    Label(win,text="Name:",font="20").place(x=30,y=40)
    name_info=StringVar()
    name=Entry(win,font="30",bd=3,textvariable=name_info)
    name.place(x=80,y=40)

    
    # sumbit button
    btn=Button(win,text="Search",font="30",bd=3,command=search).place(x=280,y=35)
    #frame1 = ttk.LabelFrame(win, text="frame1", width=100, height=50, bd=5)
    Label(win,text="Search Data",font=("Bodoni MT Black",20)).place(x=25,y=90)
    win.mainloop()
