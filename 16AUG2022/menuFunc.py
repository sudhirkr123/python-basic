from csvHandler import readlines_database,append_database


# checking book id
def check_id(book_id):
    data_list= readlines_database()  
    # splite book data
    book_list_split=[]
    for i in range(1,len(data_list)):
        book_list_split.append(data_list[i].split(","))
    #print(book_list_split)    
    for i in range(0,len(book_list_split)):
        #if book_id==book_list_split[i][1]:
        if book_id in book_list_split[i][1]:
            return True
            break
    else:
       return False
    


# adding book function
def adding_book():
    input_id=input("Enter book_id:")
    check=check_id(input_id)
    
    if check==True:
        print("book_id already exist")
    else:
        print("book id is available")   
        book_detail=[]
        name=input("Enter book Name:")
        book_id1=input_id
        author=input("Enter book Author:")
        category=input("Enter book category:")
        status=input("Enter book status:")
        # store input book details in list format
        book_add_list=[name,book_id1,author,category,status]
        # add the data in main database
        append_database(book_add_list)
        print("add successfuly")
        

#adding_book()




# searching book
def searching_book():
    data_list= readlines_database()
    # code for searching book
    book_list_split=[]
    for i in range(1,len(data_list)):
        book_list_split.append(data_list[i].split(","))
    
    # input you want to search.
    search_book=input("Enter book name you want to search:")

    #Search book
    length1=len(book_list_split)
    search_store=[]
    for i in range(length1): 
        if search_book.lower()in book_list_split[i][0]:
            search_store.append(book_list_split[i])
    #print(search_store)
    if len(search_store)>0:
        for i in search_store:
            print(i)
    else:
        print('not found')



#deleting_book()
def deleting_books():
    m=searching_book()
    print(m)

deleting_books()





























'''    
    file=open('bookData.csv','r')
    book_detail=file.readlines()
    #print(book_detail)
    file.close()

    # deleting_book
    length= len(book_detail)
    print('\n',book_detail[0],'------------------------------------------------------')
    
    for i in range(1,length):
        print(book_detail[i])
    

    book_name=input("Enter your book name you want to delete:")
    for i in range(1,length):
        if book_name==book_detail[i]:
            print(book_name)

        



        
    



    
    
deleting_books()







# Create menu Libraries
print("------------Welcome to Libraries Book------------\n")
print("a)Adding\nb)searching\nc)editing\nd)deleting books\ne)Exist")
choice=True
while choice:
    choice=input("\nEnter your Choice:")
    if choice.lower()=='a':
        # adding
        control.adding_book()
        
    elif choice.lower()=='b':
        # searching
        print('Searching')

           
    elif choice.lower=='c':
         # editing
         print('editing')

         
    elif choice.lower()=='d':
        # delete
        print('delete')

        
    elif choice.lower()=='e':
        print('---bye bye---')
        break
    
    else:
        print('Invalid option')


'''



