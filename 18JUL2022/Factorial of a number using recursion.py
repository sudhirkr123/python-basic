#using recursion method
def factorial_recursion(num):
    if num==0:
        return 1
    else:
        return num*factorial_recursion(num-1)


num=int(input("Enter your Number to find Factorials:"))

# Cheak number is negative or Positive
if num<0:
    print("your Number is negative")
else:
    print(factorial_recursion(num))
