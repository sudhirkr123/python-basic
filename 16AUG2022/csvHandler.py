
# adding book

def adding_book():
    book_detail=[]
    name=input("Enter book Name:")
    book_id=input("Enter book id:")
    author=input("Enter book Author:")
    category=input("Enter book category:")
    status=input("Enter book status:")
    book_detail=[name,book_id,author,category,status]
    length=len(book_detail)
    file=open('bookData.csv','a')
    for i in range(length):
        file.write(book_detail[i])
        if i!=length-1:
            file.write(',')
    file.write('\n')
    file.close()
    print('Add successfully:')



'''
# searching book
def searching_book():
    file=open('bookData.csv','r')
    book_detail=file.readlines()
    #print(book_detail)
    file.close()
    length=len(book_detail)
    #print(length)
    # code for searching book
    book_list_split=[]
    for i in range(1,length):
        book_list_split.append(book_detail[i].split(","))
    #print(book_list_split)


    # input you want to search.
    search_book=input("Enter book name you want to search:")


    #Search book
    length1=len(book_list_split)
    search_store=[]
    for i in range(length1): 
        if search_book.lower()==book_list_split[i][0]:
            search_store.append(book_list_split[i])

    if len(search_store)>0:
        for i in search_store:
            print(i)
    else:
        print('not found')

searching_book()


'''

