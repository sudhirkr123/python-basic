# create a file
'''
try:   
    file=open("phone_records.csv","x")
    print("new file created Successfuly")
except FileExistsError:
        print("file already present")

'''


# 1.add the records in csv file.

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



   

# 2. code for searching

def search_a_member():
    file=open("phone_records.csv","r")
    read_file1=file.readlines()
    #print(read_file1)
    file.close()

    # Remove last line \n
    for indx,line in enumerate(read_file1):    
        line =line.replace('\n', '')
        read_file1[indx] =line
    #print('paragraph: ',read_file1)
    length=len(read_file1)

    # convert read_file list into list of list each items
    list1=[]
    for i in range(0,length):
        list1.append(read_file1[i].split(","))
    print(list1)


    # input you want to search.
    search_name=input("Enter your name you want to search:")
    #find the length how many list
    length1=len(list1)
    #print(length1)

    # code for searching items
    for i in range(length1): 
        if search_name==list1[i][0]:
            print(list1[i])
            break
    else:
        print('Not Found')







# 3. code for delete a items.
def delete_a_member():
    file=open("phone_records.csv",'r+')
    read_data=file.readlines()
    #print(read_data)
    file.close()
    length=len(read_data)
    # convert read_file list into list of list each items
    list1=[]
    for i in range(0,length):
        list1.append(read_data[i].split(","))
   # print(list1)
    delete_item=input("Enter your name you want to delete:")

    for i in range(len(list1)):
         if delete_item==list1[i][0]:
              list1.pop(i)
              break
    #print("after delete:",list1)

    file=open("phone_records.csv",'w')
    # access list of list item one by one

    for i in list1:
         for j in i:
              file.write(j)
              if '\n' not in j:
                   file.write(",")
    file.close()

    print("Delete successfully")





# 4. modifiy a member
def modify_a_member():
    file=open("phone_records.csv",'r')
    read_data=file.readlines()
    # print the file data.
    #for i in read_data:
        #print(i)
    file.close()


    length=len(read_data)
    # convert read_file list into list of list each items
    list1=[]
    for i in range(0,length):
        list1.append(read_data[i].split(","))


    modify_item=input("Enter your name you want to modify:")
    length1=len(list1)
    for i in range(length1): 
        if modify_item.lower()==list1[i][0].lower():
            list2=list1[i]
            # code for menu
            print("a)modify name\nb)Modify mobile No\nc)modify age\nd)modify email_id")
            choice=True
            while choice:
                
                choice=input("\nEnter your Choice:")
                if choice.lower() == 'a': # choice.upper() == 'A': #choice=='a' or choice=='A':
                    name=input("Enter your name:")
                    list2[0]=name
                    print("modify name successfully")
                    break
                elif choice.lower()=='b':
                    mobile_no=input("Enter your mobile_no:")
                    list2[1]=mobile_no
                    print("Modify mobile no successfully")
                    break
                elif choice.lower()=='c':
                    age=input("Enter your age:")
                    list2[2]=age
                    print("modify age successfully")
                    break
                elif choice.lower()=='d':
                    email=input("Enter your email_id:")
                    list2[3]=email+'\n'        
                    print("modify email successfully")
                    break
                else:
                    print('invaid option')
            
            list1[i]=list2

            # modify data add to main file.
            file=open("phone_records.csv",'w')
            for i in list1:
                 for j in i:
                      file.write(j)
                      if '\n' not in j:
                           file.write(",")
            file.close()
            break
    else:
        print('Not Found')

        

# Create menu
print("------------Welcome to Menu------------\n")
print("a)Add a new member\nb)Modify a member\nc)Search a member\nd)Delete a member\ne)Exist")
#choice=input("\nEnter your Choice:")
choice=True
while choice:
    choice=input("\nEnter your Choice:")
    if choice=='a' or choice=='A':
        # function call for add record
        add_record()       
    elif choice=='b' or choice=='B':
        # function call modify
        modify_a_member()     
    elif choice=='c' or choice=='C':
        # fuction call search
        search_a_member()
    elif choice=='d' or choice=='D':
        # function call delete
        delete_a_member()
    elif choice=='e' or choice=='E':
        print('---bye bye---')
        break
    else:
        print('Invalid option')



