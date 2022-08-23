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


#print(check_employee_id())    
