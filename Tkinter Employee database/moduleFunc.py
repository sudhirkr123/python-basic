from csvHandler import readlines_employeeDetails,write_database


def list_split():
    data_list=readlines_employeeDetails()
    employee_list=[]
    for i in range(1,len(data_list)):
        employee_list.append(data_list[i].split(','))
    return employee_list

def list_cleaning():
    data_list= readlines_employeeDetails()
    for indx,line in enumerate(data_list):    
        line =line.replace('\n', '')
        data_list[indx] =line    
    employee_list=[]
    for i in range(1,len(data_list)):
        employee_list.append(data_list[i].split(','))
    return employee_list


def search_employee_name(name):
    Data_list=list_cleaning()
    search_store=[]
    for i in range(1,len(Data_list)): 
        if name.lower() in Data_list[i][1].lower():
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

def Edit(name,list1):
     Data_list=list_cleaning()
     for i in range(len(Data_list)):
         if name in Data_list[i][1]:
             Data_list[i]=list1
             return Data_list
            



def edited(emp,name,contact,dept,email):
    value=[emp,name,contact,dept,email+'\n']
    data_list=list_split()
    for i in range(1,len(data_list)):
        if emp in data_list[i][0]:
            data_list[i]=value
    list1=['emp id','Name','contact','dept','email\n']
    data_list.insert(0,list1)
    write_database(data_list)


def delete(empid):
    data_list=list_split()
    for i in range(len(data_list)):
        #print(type(data_list[i][0]))
        if empid in data_list[i][0]:
            data_list.pop(i)
            break
    list1=['emp id','Name','contact','dept','email\n']
    data_list.insert(0,list1)
    write_database(data_list)


         
