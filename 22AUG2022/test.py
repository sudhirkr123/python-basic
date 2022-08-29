from menuFunc import search_by_name,search_by_employee_id,list_cleaning,list_split,editing_menu,check_employee_id,check_edit_person
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
        
        
    def editing(self,emp_de,pos):
        All_data=list_split()
        while True:
            data=editing_menu(emp_de)
            if data=='Exit':
                break
            All_data[pos]=data
        #print(All_data)
    
        list1=['Employee id','Name','Contact','Dept','Email id\n']
        All_data.insert(0,list1)
        write_database(All_data)
        print('Edit sucessfully')
    
        



        
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
            
    elif choice== 2:
        # Searching
        obj.searching()
      
    elif choice== 3:
        #Editing
        employee_id=check_edit_person()
        emp_de=employee_id[0]
        pos=employee_id[1]
        obj.editing(emp_de,pos)
        
    elif choice== 4:
        
        obj.deleting()
              
    elif choice== 5:
        #Display
        obj.display()
        
    elif choice== 6:
        print('---Thank you---')
        break
    
    else:
        print('Invalid option')




