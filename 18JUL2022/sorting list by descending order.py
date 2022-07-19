# take a empty list
list1=[]
#take list length
length=int(input("Enter your list length:"))

# input number to store in list
for i in range(length):
    number=int(input("Enter your Number:"))
    list1.append(number)

print("your list Number")
print(list1)

#findig length of list
for i in range(length):
    for j in range(length-i-1):
        if list1[j]<list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]

print("Sorting list by Descending order")
print(list1)
