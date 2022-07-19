num=int(input("Enter your Number:"))
rem=0
temp=num
result=0

# find the number of digits
digit=0
while num>0:
    num=num//10
    digit=digit+1
print(digit)
num=temp

    
#code for armstrong number
while num>0:
    rem=num%10
    result=result+(rem**digit)
    num=num//10

print("Number of cube:",result)

if result==temp:
    print("your Number is Armstrong Number")
else:
    print("your Number is not Armstrong Number")
    
