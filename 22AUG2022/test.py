from cvsHandler import append_employeeDetails
from test import searching


class Employee:
    def __init__(self,employee_id,name,contact,dept,email_id):
        self.employee_id=employee_id
        self.name=name
        self.contact=contact
        self.dept=dept
        self.email_id=email_id
        
employee_id=input('Enter your emplyee_id:')
name=input('Enter name:')
contact=input('Enter contact:')
dept=input('Enter dept:')
email_id=input('Enter email_id:')



obj1=Employee(employee_id,name,contact,dept,email_id)
append_employeeDetails(obj1)
searching()


