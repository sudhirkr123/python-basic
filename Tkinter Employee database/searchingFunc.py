from csvHandler import readlines_employeeDetails


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
            
             
