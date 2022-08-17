
# csv handler add,append,write 

def readlines_database(): 
    #read the csv file and cheak id available or not
    file=open('bookData.csv','r')
    book_detail=file.readlines()
    file.close()
    return book_detail
    
  
def append_database(book_add_list):
    file=open('bookData.csv','a')
    length=len(book_add_list)
    for i in range(length):
        file.write(book_add_list[i])
        if i!=length-1:
            file.write(',')
    file.write('\n')
    file.close()
    


def write_database():
    file=open('bookData.csv','w')
    file.write()
    file.close()
    

def read_database():
    file=open('bookData.csv','r')
    book_detail=file.read()
    file.close()


