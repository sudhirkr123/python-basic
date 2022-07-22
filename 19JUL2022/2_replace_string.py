# take a list
list1=['name','Acufore','India','pvt','lmt']
print(list1)
word=input("Enter your word you should change:")
length=len(list1)

for i in range(0,length):
    if list1[i]==word:
        replace=input("Enter your word")
        list1[i]=replace
        print("replace successfuly")
        break
else:
        print("not found")
print(list1)
    
