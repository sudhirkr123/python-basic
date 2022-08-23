from menuFunc import search_by_name,search_by_employee_id

class Employee:
    def __init__(self,emp_id= '',name= '',contact= '',dept= '',email_id= ''):
        self.employee_id=emp_id
        self.name=name
        self.contact=contact
        self.dept=dept
        self.email_id=email_id
        
    def adding(self,employee_id,name,contact,dept,email_id):
        self.employee_id=employee_id
        self.name=name
        self.contact=contact
        self.dept=dept
        self.email_id=email_id
        

    def searching(self):
        print('1.search by Name\n2.Search by employee_id')
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

obj=Employee()

obj.searching()
