from cvsHandler import readlines_employeeDetails

def search_by_name(search_by_name):
    data_list= readlines_employeeDetails()

    for indx,line in enumerate(data_list):    
        line =line.replace('\n', '')
        data_list[indx] =line

    # code spliting each word
    employeeDetails_split=[]
    for i in range(1,len(data_list)):
        employeeDetails_split.append(data_list[i].split(","))

    length1=len(employeeDetails_split)
    search_store=[]
    for i in range(length1): 
        if search_by_name.lower() in employeeDetails_split[i][1].lower():
            search_store.append(employeeDetails_split[i])
    if len(search_store)>0:
        for indx,line in enumerate(search_store):
            print(indx+1,'.',' , '.join(line))        
    else:
        print('not found')
        
            
#search_by_name('raju')
    
def search_by_employee_id(search_by_employee_id):
    data_list= readlines_employeeDetails()

    for indx,line in enumerate(data_list):    
        line =line.replace('\n', '')
        data_list[indx] =line

    # code spliting each word
    employeeDetails_split=[]
    for i in range(1,len(data_list)):
        employeeDetails_split.append(data_list[i].split(","))

    length1=len(employeeDetails_split)
    search_store=[]
    for i in range(length1): 
        if search_by_employee_id in employeeDetails_split[i][0]:
            search_store.append(employeeDetails_split[i])
    if len(search_store)>0:
        for indx,line in enumerate(search_store):
            print(indx+1,'.',' , '.join(line))        
    else:
        print('not found')


def searching():
    print('1.search by Name\n2.Search by employee_id')
    option=input('Enter option:')
    if option=='1':
        name=input('Enter name:')
        search_by_name(name)
    elif option=='2':
        employee_id=input('Enter employee_id:')
        search_by_employee_id(employee_id)
        
    else:
        print('Invalid option')
    


searching()    


