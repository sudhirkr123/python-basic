from menuFunc import search_by_name,search_by_employee_id,list_cleaning,list_split,editing_menu,check_employee_id
from cvsHandler import write_database,append_employeeDetails

class Employee:
    def __init__(self,emp_id= '',name= '',contact= '',dept= '',email_id= ''):
        self.employee_id=emp_id
        self.name=name
        self.contact=contact
        self.dept=dept
        self.email_id=email_id
        
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
                         while True:
                             data=editing_menu(All_data[i])
                             if data=='Exit':
                                 break
                             All_data[i]=data   
                         break
                     list1=['Employee id','Name','Contact','Dept','Email id\n']
                     All_data.insert(0,list1)
                     write_database(All_data)
                     print('Edit sucessfully')
                
                 else:
                     print('worng Employee id')
    
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
obj.editing()
