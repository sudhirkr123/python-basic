'''
file=open('bookData.csv','r')
book_detail=file.readlines()
print(book_detail)
file.close()
for i in range(len(book_detail)):
    print(book_detail[i])
'''

name=input("Enter your name")
rollno=input("Enter your subject")

list1=[name,rollno]
print(list1)
