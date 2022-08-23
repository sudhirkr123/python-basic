
def append_employeeDetails(obj1):
    file=open('employee.csv','a')
    file.write(obj1.employee_id + ',')
    file.write(obj1.name +',')
    file.write(obj1.contact +',')
    file.write(obj1.dept+',')
    file.write(obj1.email_id+'\n')
    file.close()


def readlines_employeeDetails(): 
    #read the csv file and cheak id available or not
    file=open('employee.csv','r')
    employee_Details=file.readlines()
    file.close()
    return employee_Details

