from menuFunc import search_by_name,search_by_employee_id,list_cleaning,list_split,editing_menu,check_employee_id
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




    def deleting(self):
        print('1.Delete by Name\n2.Delete by Employee id')
        option=input("Enter option:")
        if option=='1':
            name=input('Enter name:')
            check_name=search_by_name(name)
            
            if len(check_name)==0:
                print('Record not found')
                
            elif len(check_name)==1:
                for indx,line in enumerate(check_name):
                    print(indx+1,'.',' , '.join(line))

                #confirmation ask to user
                confrm=input('Do you want to delete(y/n):')
                if confrm.lower()=='y':
                    All_data=list_split()
                    #print(All_data)
                    
                    for i in range(len(All_data)):
                         if check_name[0][1] in All_data[i][1]:
                             All_data.pop(i)
                             break
                    #print(All_data)
                    list1=['Employee id','Name','Contact','Dept','Email id\n']
                    All_data.insert(0,list1)
                    write_database(All_data)
                    print('Delete sucessfully')
                    
            else:
                 for indx,line in enumerate(check_name):
                    print(indx+1,'.',' , '.join(line))

                 confrm=input('Enter employee_id:')
                 All_data=list_split()
                 for i in range(len(All_data)):
                     if confrm in All_data[i][0]:
                          All_data.pop(i)
                          list1=['Employee id','Name','Contact','Dept','Email id\n']
                          All_data.insert(0,list1)
                          write_database(All_data)
                          print('Delete sucessfully')
                          break
                 else:
                    print('worng Employee_id')
    
        elif option=='2':
            employee_id=input('Enter employee_id:')
            check_id=search_by_employee_id(employee_id)
            All_data=list_split()
            for i in range(len(All_data)):
                if employee_id in All_data[i][0]:
                    All_data.pop(i)
                    list1=['Employee id','Name','Contact','Dept','Email id\n']
                    All_data.insert(0,list1)
                    write_database(All_data)
                    print('Delete sucessfully')
                    break
            else:
                print('Worng Employee_id')
            
        else:
            print('Invalid option')



    def display(self):
        data=list_cleaning()
        print('Employee_id ,Name ,Contact ,Dept ,Email')
        print('-------------------------------------------------')
        for indx,line in enumerate(data):
            print(indx+1,'.',' , '.join(line))




    def editing(self):
        print('1.Edit by Name\n2.Edit by Employee id')
        option=input("Enter option:")
        if option=='1':
            name=input('Enter name:')
            check_name=search_by_name(name)
            #print(check_name)
            
            if len(check_name)==0:
                print('Record not found')
                
            elif len(check_name)==1:
                for indx,line in enumerate(check_name):
                    print(indx+1,'.',' , '.join(line))

                #confirmation ask to user
                confrm=input('Do you want to edit(y/n):')
                if confrm.lower()=='y':
                    All_data=list_split()
                    #print(All_data)
                    
                    for i in range(len(All_data)):
                         if check_name[0][1] in All_data[i][1]:
                             
                            while True:
                                data=editing_menu(All_data[i])
                                if data=='Exit':
                                    break
                                All_data[i]=data
                            break
                                
                    #print(All_data)
                    list1=['Employee id','Name','Contact','Dept','Email id\n']
                    All_data.insert(0,list1)
                    write_database(All_data)
                    print('Edit sucessfully')
                    
            else:
                 for indx,line in enumerate(check_name):
                    print(indx+1,'.',' , '.join(line))

                 confrm=input('Enter employee_id you want to edit:')
                 All_data=list_split()
                 for i in range(len(All_data)):
                     if confrm in All_data[i][0]: 
                        data=editing_menu(All_data[i])
                        All_data[i]=data
                        list1=['Employee id','Name','Contact','Dept','Email id\n']
                        All_data.insert(0,list1)
                        write_database(All_data)
                        print('Edit sucessfully')
                        break
                 else:
                    print('worng Employee_id')
    
        elif option=='2':
            employee_id=input('Enter employee_id:')
            check_id=search_by_employee_id(employee_id)
            All_data=list_split()
            for i in range(len(All_data)):
                if employee_id in All_data[i][0]:
                    data=editing_menu(All_data[i])
                    All_data[i]=data
                    list1=['Employee id','Name','Contact','Dept','Email id\n']
                    All_data.insert(0,list1)
                    write_database(All_data)
                    print('Edit sucessfully')
                    break
            else:
                print('Worng Employee_id')
            
        else:
            print('Invalid option')

        
        
    
            
                    



                    
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
        obj.editing()
            
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


