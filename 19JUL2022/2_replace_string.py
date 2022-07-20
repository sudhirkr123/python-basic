# take a list
list1=['name','Acufore','India','pvt','lmt']
print(list1)
word=input("Enter string you want to change string:")
replace=input("Enter any word:")
length=len(list1)

for i in range(0,length):
    if list1[i]==word:
        list1[i]=replace
print(list1)
    
