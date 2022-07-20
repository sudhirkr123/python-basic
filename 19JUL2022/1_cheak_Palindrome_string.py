# Take input string
string=input("Enter your string:")
rev=""
length=len(string)
# code for reverse the string
for i in range(length-1,-1,-1):
    rev=rev+string[i]
    
#cheak palindrome string
if rev==string:
    print("your word is palindrome")
else:
    print("your word is not polindrome")
