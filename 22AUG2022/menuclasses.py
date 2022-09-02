from menuFunc import search_by_name,search_by_employee_id,list_split,delete_employee,check_edit_person,list_cleaning,check_employee_id,store_edit_Func
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
        
    
    def searching(self):
        print('1.Search by Name\n2.Search by Employee id')
        option=input("Enter option:")   
        if option=='1':
            name=input('Enter name:')
            check_name=search_by_name(name)
            if len(check_name)>0:
                for indx,line in enumerate(check_name):
                    print(indx+1,'.',' , '.join(line))        
            else:
                print('not found')
        elif option=='2':
            employee_id=input('Enter employee_id:') 
            check_id=search_by_employee_id(employee_id)  
            if len(check_id)>0:
                for indx,line in enumerate(check_id):
                    print(indx+1,'.',' , '.join(line))
            else:
                print('not found')
        else:
            print('Invalid option')


    def display(self):
        data=list_cleaning()
        print('Employee_id ,Name ,Contact ,Dept ,Email')
        print('-------------------------------------------------')
        for indx,line in enumerate(data):
            print(indx+1,'.',' , '.join(line))




    def editing(self):
        print('Edit menu option')
        choice=''
        while True:
            print("\na)Employee id:",self.employee_id)
            print("b)Name :",self.name)
            print("c)Contact:",self.contact)
            print("d)Dept:",self.dept)
            print("e)Email:",self.email_id)
            print("f)Exit:")
            choice=input("\nEnter your option:")
            if choice.lower()=='a':
                self.employee_id=input("Enter Employee id:")
            
            elif choice.lower()=='b':
                self.name=input("Enter Name:")
                
            elif choice.lower()=='c':
                self.contact=input("Enter contact:")
            
            elif choice.lower()=='d':
                self.dept=input("Enter Dept:")

                   
            elif choice.lower()=='e':
                self.email_id=input("Enter Email:")+'\n'
                
            elif choice.lower()=='f':
                return
        
            else:
                print('[ERROR] Invalid option.')


                    
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
        print('1.Edit by Name\n2.Edit by Employee id')
        #option=input("Enter your option:")
        obj.employee_id, obj.name,obj.contact,obj.dept, obj.email_id, pos = check_edit_person()
        obj.editing()
        store_edit_Func(obj, pos)
        
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
        #Display
        obj.display()
        
    elif choice== 6:
        print('---Thank you---')
        break
    
    else:
        print('Invalid option')
