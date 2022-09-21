
#Import necessary Library
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
#Create an instance of tkinter window
win= Tk()
#Set the geometry of tkinter window
win.geometry("750x250")
#Define the function to change the value in label widget
def change_text(label):
   label.configure(text= "Hey, I am Label-2", background="gray91")
#Create a Label
label = Label(win, text= "Hey, I am Label-1", font= ('Helvetica15 underline'), background="gray76")
label.pack(pady=20)
#Create a button
btn= ttk.Button(win,text= "Change", command=lambda:change_text(label), state= DISABLED)
btn.pack(pady=10)
win.mainloop()



















'''
import tkinter as tk
my_w = tk.Tk()
my_w.geometry("200x200")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

my_str = tk.StringVar()
l1 = tk.Label(my_w,  textvariable=my_str, width=10 )
l1.grid(row=0,column=1,columnspan=5) 

def show_lan(my_language):
    my_str.set(my_language)

list_languages = ("PHP","Python","HTML","Tkinter")
var = 0


for language in list_languages:
    btn = tk.Button(my_w, text=language, command=lambda lan=language:show_lan(lan))
    btn.grid(row=1,column=var)
    var += 1

root.mainloop()
'''






'''
from tkinter import *

fenster = Tk()
fenster.title("Window")

def switch():
    if b1["state"] == "normal":
        b1["state"] = "disabled"
        b2["text"] = "enable"
    else:
        b1["state"] = "normal"
        b2["text"] = "disable"

#--Buttons
b1 = Button(fenster, text="Button", height=5, width=7)
b1.grid(row=0, column=0)    

b2 = Button(text="disable", command=switch)
b2.grid(row=0, column=1)

fenster.mainloop()
'''


















'''
#Import necessary Library
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile
#Create an instance of tkinter window
win= Tk()
#Set the geometry of tkinter window
win.geometry("750x250")
#Define the function to change the value in label widget
def change_text(label):
   label.configure(text= "Hey, I am Label-2", background="gray91")
#Create a Label
label = Label(win, text= "Hey, I am Label-1", font= ('Helvetica 15 underline'), background="gray76")
label.pack(pady=20)
#Create a button
btn= ttk.Button(win,text= "Change", command=
lambda:change_text(label), state= DISABLED)
btn.pack(pady=10)
win.mainloop()
'''














'''
from tkinter import Tk, Toplevel
from tkinter import *
def main():
    main_window = Tk()
    app = first(main_window)
    main_window.mainloop()


class first:
    def __init__(self, root):
        self.root = root
        self.root.title('First window')

        self.root.geometry('1350x700+0+0')
        frame1 = Frame(self.root, bg='black')
        frame1.place(x=400, y=50, width=400, height=600)
        btn_1 = Button(frame1, command=self.second_window, text='open second window', font=("Times New Roman", 15, 'bold'), bd=3,
                           relief=RIDGE,
                           cursor='hand2', bg='red', fg='white', activeforeground='white', activebackground='red')
        btn_1.place(x=100, y=350, width=220, height=35)

    def second_window(self):
        self.new_window = Toplevel(self.root)
        self.app = second(self.new_window)


class second:
    def __init__(self, root):
        self.root = root
        self.root.title('Second Window')
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')
        frame1 = Frame(self.root, bg='black')
        frame1.place(x=400, y=50, width=400, height=600)
        btn_1 = Button(frame1, command=self.first_window, text='open first window',
                       font=("Times New Roman", 15, 'bold'), bd=3,
                       relief=RIDGE,
                       cursor='hand2', bg='red', fg='white', activeforeground='white', activebackground='red')
        btn_1.place(x=100, y=350, width=220, height=35)

    def first_window(self):
        self.new_window = Toplevel(self.root)
        self.app = first(self.new_window)


if __name__ == '__main__':
    main()

'''
from tkinter import *

class MainView(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        new_popup = Button(self,text = 'Make A Popup!',
            command = lambda: popup()).grid(row=0,column=0)


def popup():
    popup = Toplevel()
    button = Button(popup, text = 'Display something on the command line',
        command = lambda: display_something() & popup.destroy())
    button.pack()

def display_something():
    print('popup ran the command')

def main():
    root = Tk()
    root.title('Eric\'s Archiver')
    app = MainView(root)
    root.mainloop()


if __name__ == '__main__':
    main()


















'''
from tkinter import *
#from tkinter import ttk
win=Tk()
win.title('AcuforeEmployee data')
win.geometry("520x200")
win.iconbitmap("D:\\sudhir\\basic python\\Tkinter Employee database\\icon\\acufore logo.ico")
#win.resizable(False,False)
#top=Toplevel()
def display1():
    pass

def adding1():
    pass


def search1():
    pass

    

def edit1():
    pass
   


def delete1():
    pass
   

Label(win,text="Acufore Employee Details",bg="grey",font=("calibri",25)).pack()



btn=Button(win,text="Display",font="30",bd=3,command=display1).place(x=40,y=100)
btn=Button(win,text="Add records",font="30",bd=3,command=adding1).place(x=120,y=100)
btn=Button(win,text="Search",font="30",bd=3,command=search1).place(x=235,y=100)
btn=Button(win,text="Edit",font="30",bd=3,command=edit1).place(x=315,y=100)
btn=Button(win,text="Delete",font="30",bd=3,command=delete1).place(x=370,y=100)
win.mainloop()

'''














'''
import os
from subprocess import call

import sys


from Tkinter import *
win=Tk()

class HOTEL_MANAGEMENT:
    def __init__(self):
        #root = Tk()
        

        This class configures and populates the toplevel window.
           top is the toplevel containing window.
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        

        root.geometry("963x749+540+110")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")



        self.menubar = Menu(root)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Message6.configure(background="#d9d9d9")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text=WELCOME)
        self.Message6.configure(width=791)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.18, rely=0.17, height=103, width=566)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text=1.CHECK INN)
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_checkinn)

       

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.18, rely=0.33, height=93, width=566)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text=2.SHOW GUEST LIST)
        self.Button3.configure(width=566)
        self.Button3.configure(command=click_list)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.18, rely=0.47, height=93, width=566)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text=3.CHECK OUT)
        self.Button4.configure(width=566)
        self.Button4.configure(command=click_checkout)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.18, rely=0.61, height=103, width=566)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text=4.GET INFO OF ANY GUEST')
        self.Button5.configure(width=566)
        self.Button5.configure(command=click_getinfo)
     

        

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.18, rely=0.77, height=103, width=566)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text=5.EXIT)
        self.Button6.configure(width=566)
        self.Button6.configure(command=quit)
        root.mainloop()


if __name__ == '__main__':
    GUUEST=HOTEL_MANAGEMENT(win)


'''


