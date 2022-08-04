def modify_a_member():
    file=open("phone_records.csv",'r')
    read_data=file.readlines()
    # print the file data.
   
    #for i in read_data:
       # print(i)
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
                    email=input("Enter your mobile no:")
                    list2[3]=add+'\n'        
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

modify_a_member()


















    
