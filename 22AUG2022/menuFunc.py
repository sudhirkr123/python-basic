from cvsHandler import readlines_employeeDetails


# list cleaning
def list_cleaning():
    data_list= readlines_employeeDetails()
    for indx,line in enumerate(data_list):    
        line =line.replace('\n', '')
        data_list[indx] =line    
    employee_list=[]
    for i in range(1,len(data_list)):
        employee_list.append(data_list[i].split(','))
    return employee_list

def list_split():
    data_list=readlines_employeeDetails()
    employee_list=[]
    for i in range(1,len(data_list)):
        employee_list.append(data_list[i].split(','))
    return employee_list
    


# search by name
def search_by_name(search_by_name):
    Data_list=list_cleaning()
    search_store=[]
    for i in range(len(Data_list)): 
        if search_by_name.lower() in Data_list[i][1].lower():
            search_store.append(Data_list[i])
    return search_store
    


        
# search by employee_id    
def search_by_employee_id(employee_id):
    Data_list=list_cleaning()
    search_store=[]
    for i in range(len(Data_list)): 
        if employee_id in Data_list[i][0]:
            search_store.append(Data_list[i])
    return search_store
    
   

  
# check_employee_id
def check_employee_id(employee_id):
    data_list= readlines_employeeDetails()
    employee_list=[]
    for i in range(0,len(data_list)):
        employee_list.append(data_list[i].split(','))
    for i in range(len(employee_list)):
        if employee_id in employee_list[i][0]:
            return True



def editing_menu(employee_list):
    print("a)Employee_id\nb)Name\nc)Contact\nd)Dept\ne)Email")
    choice=True
    while choice:
        choice=input("\nEnter your option:")
        if choice.lower()=='a':
            emp_id=input("Enter_Employee_id:")
            employee_list[0]=emp_id
            return employee_list
        
        elif choice.lower()=='b':
            name=input("Enter Name:")
            employee_list[1]=name
            return employee_list
        
        elif choice.lower()=='c':
            contact=input("Enter Contact:")
            book_list_split[2]=contact
            return employee_list
        
        elif choice.lower()=='d':
            dept=input("Enter Dept:")
            employee_list[3]=dept
            return employee_list
        elif choice.lower()=='e':
            mail=input("Enter Email:")
            employee_list[4]=mail+'\n'
            return employee_list   
        else:
            print('Invalid option')

#editing_menu(list1)
#print(check_employee_id())    
