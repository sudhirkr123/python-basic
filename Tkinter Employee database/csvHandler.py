def append_employeeDetails(emp,name,contact,dept,email):
    file=open('employee.csv','a')
    file.write(emp + ',')
    file.write(name +',')
    file.write(contact +',')
    file.write(dept +',')
    file.write(email+'\n')
    file.close()


def readlines_employeeDetails(): 
    #read the csv file and cheak id available or not
    file=open('employee.csv','r')
    employee_Details=file.readlines()
    file.close()
    return employee_Details

def write_database(employee_list):
    file=open('employee.csv','w')
    for indx,line in enumerate(employee_list):
        for indx1,word in enumerate(line):
            file.write(word)
            if '\n' not in word:
                file.write(",")
    file.close()

