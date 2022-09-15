from tkinter import *
from tkinter import ttk

class Application(Frame):
    
    def __init__(self, master):
        """ Initialize the Frame"""
        #print(master)
        ttk.Frame.__init__(self, master)
        self.root=master
 
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        
        # create Treeview widget to hold values in a table
        self.tv = ttk.Treeview(self.root)    

        # create Treeview 
        self.tv = ttk.Treeview(self,  height=5)
        self.tv['columns'] = ('id', 'name', 'contact', 'dept', 'email')
        self.tv.heading("#0", text='Time', anchor='w')
        self.tv.column("#0", stretch=NO, width=5, anchor="w")
        self.tv.heading('id', text='ID')
        self.tv.column('id', anchor='center', width=120)
        self.tv.heading('name', text='Name')
        self.tv.column('name', anchor='center', width=120)
        self.tv.heading('contact', text='Contact')
        self.tv.column('contact', anchor='center', width=120)
        self.tv.heading('dept', text='Dept')
        self.tv.column('dept', anchor='center', width=120)
        self.tv.heading('email', text='Email')
        self.tv.column('email', anchor='center', width=120)
        
        self.tv.bind('<ButtonRelease-1>', self.select_item) 
        self.tv.grid(row=1, column=0, columnspan=5, padx=3, pady=3)
        self.treeview = self.tv

        
        ttk.Style().configure("Treeview", font= ('', 8), background="#383838", 
        foreground="white", fieldbackground="yellow")


        data=[['124', 'Raju kumar', '9523614264', 'computer Science', 'Raju@gmail.com '], ['456', 'Ramod kumar', '9097564534', 'computer science', 'ramod@gmail.com'], ['345', 'Sudhir kumar', '5002237851', 'cs', 'sudhir@gmail.com'], ['666', 'Suraj kumar', '7277423455', 'maths', 'suraj@gmail.com'], ['124', 'Rahul kumar', '7857585944', 'Maths', 'rahul@gmail.com'], ['1234', 'sintu kumar', '7788885885', 'computer science', 'sintu123@gmail.com'], ['126', 'Pintu kumar', '8842646780', 'Physics', 'pinu123@gmail.com'], ['678', 'sudhir kumar', '8003458582', 'computer science', 'sudhir@gmail.com']]
        for i in range(0,len(data)):
            self.tv.insert("","end",text = i,values = (data[i][0],data[i][1],data[i][2], data[i][3], data[i][4]))
        
        
    def select_item(self, a):   # added self and a (event)
        test_str_library = self.tv.item(self.tv.selection())# gets all the values of the selected row
        #print ('The test_str = ', type(test_str_library), test_str_library,  '\n')  # prints a dictionay of the selected row
        item = self.tv.selection()[0] # which row did you click on
        #print ('item clicked ', item) # variable that represents the row you clicked on
        print (self.tv.item(item)['values'][0])# prints the first value of the values (the id value)
        print(self.tv.item(item)['values'][1])
        print(self.tv.item(item)['values'][2])
        print(self.tv.item(item)['values'][3])
        print(self.tv.item(item)['values'][4])


        
root = Tk()
app = Application(root)

root.mainloop()
