#input two Number
a=int(input("Enter your first Number:"))
b=int(input("Enter your second Number:"))

print("Before Swapping two number")
print("a=",a)
print("b=",b)

# code for swapping without using Third variable
#a,b=b,a


# code for Swapping use for Third variable
temp=a
a=b
b=temp

print("After Swapping")
print("a=",a)
print("b=",b)
