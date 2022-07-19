#take a list
list1=[]
length=int(input("Enter your list length to Insert number:"))
for i in range(length):
    number=int(input("Enter your Number"))
    list1.append(number)

print("your list Number")
print(list1)
    

#code for sort the List in accending order
for i in range(length):
    for j in range(length-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            
print("Sort your list for Ascending order")
print(list1)
