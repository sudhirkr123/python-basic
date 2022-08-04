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
    print(list1)
    delete_item=input("Enter your name you want to delete:")

    for i in range(len(list1)):
         if delete_item==list1[i][0]:
              list1.pop(i)
              break
    print("after delete:",list1)

    file=open("phone_records.csv",'w')
    # access list of list item one by one

    for i in list1:
         for j in i:
              file.write(j)
              if '\n' not in j:
                   file.write(",")
    file.close()

    print("Delete successfully")

delete_a_member()
