
def add_record():
    
    name=input("Enter your Name:")
    mobile_no=input("Enter your Mobile_No:")
    age=input("Enter your Age:")
    email_id=input("Enter your Email_id:")
    list1=[name,mobile_no,age,email_id]
    length=len(list1)
    file=open("phone_records.csv","a")
    for i in range(length):
        file.write(list1[i])
        if i!=length-1:
            file.write(',')
    file.write('\n')
    file.close()
    print('Add successfully:')

add_record()
