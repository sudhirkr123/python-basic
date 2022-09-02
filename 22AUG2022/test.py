from menuFunc import search_by_name,search_by_employee_id,list_split,check_employee_id,delete_employee
from cvsHandler import write_database,append_employeeDetails

class Employee:
    def __init__(self,emp_id= '',name= '',contact= '',dept= '',email_id= ''):
        self.employee_id=emp_id
        self.name=name
        self.contact=contact
        self.dept=dept
        self.email_id=email_id

     
    def adding(self,emp_id):
        self.employee_id= emp_id
        self.name= input('Enter name:')
        self.contact= input('Enter contact no:')
        self.dept= input('Enter dept:')
        self.email_id= input('Enter email:')





        
       
obj=Employee()

print('Employee Contact Database\n----------------------------------')
print('1.Adding\n2.Searching\n3.Editing\n4.Deleting\n5.Display\n6.Exit')
choice=True
while True:
    choice=int(input("\nEnter your Choice:"))
    if choice== 1:
        new_id=input('check id:')
        check=check_employee_id(new_id)
        if check==True:
            print('Already id is present in data base')
        else:
            obj.adding(new_id)
            append_employeeDetails(obj)
            print('Add new employee details Sucessfully') 
        
    elif choice== 4:
        print('1.Delete by Name\n2.Delete by Employee id')
        pos=delete_employee()
        All_data=list_split()
        All_data.pop(pos)
        list1=['Employee id','Name','Contact','Dept','Email id\n']
        All_data.insert(0,list1)
        write_database(All_data)
        print('Delete sucessfully')


        
              
    elif choice== 5:
        print('---> display')
        #Display
        
    elif choice== 6:
        print('---Thank you---')
        break
    
    else:
        print('Invalid option')









#print(obj.employee_id,obj.name,obj.contact,obj.dept,obj.email_id)




















        
        
    
            
'''
def editing(self):
        print('Edit menu option')
        print("a)Employee id\nb)Name\nc)Contact\nd)Dept\ne)Email\nf)Exit")
        
        choice=''
        while True:
            choice=input("\nEnter your option:")
            if choice.lower()=='a':
                self.employee_id=input("Enter_Employee_id:")
            
            elif choice.lower()=='b':
                self.name=input("Enter Name:")
                
            elif choice.lower()=='c':
                self.dept=input("Enter contact:")
            
            elif choice.lower()=='d':
                self.dept=input("Enter Dept:")
                   
            elif choice.lower()=='e':
                self.email_id=input("Enter Email:")
                
            elif choice.lower()=='f':
                return
        
            else:
                print('Invalid option')

'''
