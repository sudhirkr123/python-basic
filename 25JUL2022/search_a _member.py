
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

search_a_member()


'''
# take one variable to store search items
result=[]
for i in range(length1):
    if search_name==list1[i][0]:
        #print(list1[i])
        result.append(list1[i])
    #print(result)
length_result=len(result)

if length_result>0:
    for i in result:
        print(i)
else:
    print('Not Found')
'''
