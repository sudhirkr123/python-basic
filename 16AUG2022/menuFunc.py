from csvHandler import readlines_database,append_database,write_database



# display all data 
def display_data():
    data_list= readlines_database()
    for i in data_list:
        print(i)


#display_data()
#-------------------------------- completed displaying--------------------------------------------------


        

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
    
#----------------completed checking book_id------------------------------------------------------


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
       
#--------------------------completed adding---------------------------------




# searching book
def searching_book():
    data_list= readlines_database()

    for indx,line in enumerate(data_list):    
        line =line.replace('\n', '')
        data_list[indx] =line

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
        print('sno ,Name , Book ID, Author, Category, Status')
        print('--------------------------------------------------------')
        for indx,line in enumerate(search_store):
            print(indx+1,'.',' , '.join(line))        
    else:
        print('not found')
        
#searching_book()



        
#----------------------completed searching---------------------------------

#deleting_book()
def deleting_books():
    delete=input("Enter book you want to delete:")
    data_list= readlines_database()
    book_list_split=[]
    for i in range(1,len(data_list)):
        book_list_split.append(data_list[i].split(","))

    length1=len(book_list_split)
    #print(book_list_split)
    search_store=[]
    for i in range(length1): 
        if delete.lower()in book_list_split[i][0]:
            search_store.append(book_list_split[i])
    #print(search_store[0][1])


            
    if len(search_store)==0:
        print('not found')



    elif len(search_store)==1:
        # book only one available to conform yes or no
        print('sno ,Name , Book ID, Author, Category, Status')
        print('--------------------------------------------------------')
        for indx,line in enumerate(search_store):
            print(indx+1,'.',' , '.join(line))

        one_book=input("if you to delete book(y/n)")
        
        if one_book=='y':
            for i in range(len(book_list_split)):
                 if search_store[0][1]==book_list_split[i][1]:
                        book_list_split.pop(i)
                        break
            list1=['Name','Book_ID','Author','Category','Status\n']
            book_list_split.insert(0,list1)
            write_database(book_list_split)
            print('deleted sucessfully')

            
    else:

        # multiple book found to conform book id

        print('sno ,Name , Book ID, Author, Category, Status')
        print('--------------------------------------------------------')
        for indx,line in enumerate(search_store):
            print(indx+1,'.',' , '.join(line))
        book_id=input("Enter your book_id to confirm delete:")

        for i in range(len(book_list_split)):
            if book_id==book_list_split[i][1]:
                book_list_split.pop(i)
                break
        list1=['Name','Book_ID','Author','Category','Status\n']
        #append_database(list1)
        book_list_split.insert(0,list1)
        write_database(book_list_split)
        print('deleted sucessfully')





#deleting_books()

#-----------------completed deleting function--------------------------


def editing_book():
    editing=input("Enter book name you want to modify:")
    data_list= readlines_database()
    book_list_split=[]
    for i in range(1,len(data_list)):
        book_list_split.append(data_list[i].split(","))

    length1=len(book_list_split)
    #print(book_list_split)
    search_store=[]
    for i in range(length1): 
        if editing.lower()in book_list_split[i][0]:
            search_store.append(book_list_split[i])
    #print(search_store)

    if len(search_store)==0:
        print('not found')

    elif len(search_store)==1:
             print('only one search')
    
    else:
        print('two or more')
    
editing_book()








'''

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



