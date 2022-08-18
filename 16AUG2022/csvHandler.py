
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

    

def write_database(book_list_split):
    file=open('bookData.csv','w')
    for indx,line in enumerate(book_list_split):
        for indx1,word in enumerate(line):
            file.write(word)
            if '\n' not in word:
                file.write(",")
    file.close()



def read_database():
    file=open('bookData.csv','r')
    book_detail=file.read()
    file.close()


