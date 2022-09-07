from cvsHandler import readlines_employeeDetails,write_database


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


def check_edit_person():
    #print('1.Edit by Name\n2.Edit by Employee id')
    option=True
    #option=input("Enter option:")
    while True:
        option=input("Enter your option:")
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
                    for i in range(len(All_data)):
                        if check_name[0][1] in All_data[i][1]: 
                            return All_data[i][0],All_data[i][1],All_data[i][2],All_data[i][3],All_data[i][4],i               
            else:    
                for indx,line in enumerate(check_name):
                    print(indx+1,'.',' , '.join(line))

                confrm=input('Enter employee_id you want to edit:')
                All_data=list_split()
                for i in range(len(All_data)):
                    if confrm in All_data[i][0]:
                        return All_data[i][0],All_data[i][1],All_data[i][2],All_data[i][3],All_data[i][4],i
                else:
                    print('Enter worng emplyee_id')
                    
        elif option=='2':
            employee_id=input('Enter employee_id:')
            check_id=search_by_employee_id(employee_id)
            All_data=list_split()
            for i in range(len(All_data)):
                if employee_id in All_data[i][0]:               
                    return All_data[i][0],All_data[i][1],All_data[i][2],All_data[i][3],All_data[i][4],i   
            else:
                print('Worng Employee_id')
        else:
            print('Invalid option')





def store_edit_Func(obj,pos):
    All_data=list_split()          
    All_data[pos][0]=obj.employee_id
    All_data[pos][1]=obj.name
    All_data[pos][2]=obj.contact   
    All_data[pos][3]=obj.dept
    All_data[pos][4]=obj.email_id
    list1=['Employee id','Name','Contact','Dept','Email id\n']
    All_data.insert(0,list1)
    write_database(All_data)
    print('Edit sucessfully')







def delete_employee():
    option=''
    #option=input("Enter option:")
    while True:
        option=input("Enter your option:")
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
                confrm=input('Do you want to deleted(y/n):')
                if confrm.lower()=='y':
                    All_data=list_split()
                    for i in range(len(All_data)):
                        if check_name[0][1] in All_data[i][1]:
                            return i
                        break
                            
            else:    
                for indx,line in enumerate(check_name):
                    print(indx+1,'.',' , '.join(line))

                confrm=input('Enter employee_id you want to delete:')
                All_data=list_split()
                for i in range(len(All_data)):
                    if confrm in All_data[i][0]:
                        return i
                else:
                    print('Enter worng emplyee_id')
                    
        elif option=='2':
            employee_id=input('Enter employee_id:')
            check_id=search_by_employee_id(employee_id)
            All_data=list_split()
            for i in range(len(All_data)):
                if employee_id in All_data[i][0]:               
                    return i   
            else:
                print('Worng Employee_id')
        else:
            print('Invalid option')





