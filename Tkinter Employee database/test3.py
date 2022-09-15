from tkinter import *
from tkinter import ttk

root = Tk()  
tv = ttk.Treeview()
tv = ttk.Treeview(height=5)

def Application():
    def select_item(a):   # added self and a (event)
        test_str_library = tv.item(tv.selection())# gets all the values of the selected row
        print ('The test_str = ', type(test_str_library), test_str_library,  '\n')  # prints a dictionay of the selected row
        item = tv.selection()[0] # which row did you click on
        print ('item clicked ', item) # variable that represents the row you clicked on
        print (tv.item(item)['values'][0]) # prints the first value of the values (the id value)   
        # create Treeview 
    
    tv['columns'] = ('id', 'name', 'contact', 'dept', 'email')
    tv.heading("#0", text='Time', anchor='w')
    tv.column("#0", stretch=NO, width=5, anchor="w")
    tv.heading('id', text='ID')
    tv.column('id', anchor='center', width=70)
    tv.heading('name', text='Name')
    tv.column('name', anchor='center', width=70)
    tv.heading('contact', text='Contact')
    tv.column('contact', anchor='center', width=70)
    tv.heading('dept', text='Dept')
    tv.column('dept', anchor='center', width=70)
    tv.heading('email', text='Email')
    tv.column('email', anchor='center', width=100)
        
    tv.bind('<ButtonRelease-1>', select_item) 
    tv.grid(row=1, column=0, columnspan=5, padx=3, pady=3)
    streeview = tv

        
    ttk.Style().configure("Treeview", font= ('', 8), background="#383838", 
    foreground="white", fieldbackground="yellow")


    data=[['124', 'Raju kumar', '9523614264', 'computer Science', 'Raju@gmail.com '], ['456', 'Ramod kumar', '9097564534', 'computer science', 'ramod@gmail.com'], ['345', 'Sudhir kumar', '5002237851', 'cs', 'sudhir@gmail.com'], ['666', 'Suraj kumar', '7277423455', 'maths', 'suraj@gmail.com'], ['124', 'Rahul kumar', '7857585944', 'Maths', 'rahul@gmail.com'], ['1234', 'sintu kumar', '7788885885', 'computer science', 'sintu123@gmail.com'], ['126', 'Pintu kumar', '8842646780', 'Physics', 'pinu123@gmail.com'], ['678', 'sudhir kumar', '8003458582', 'computer science', 'sudhir@gmail.com']]
    for i in range(0,len(data)):
        tv.insert("","end",text = i,values = (data[i][0],data[i][1],data[i][2], data[i][3], data[i][4]))
        
        
    

root.mainloop()
