f1=open('d:\sudhir\basic python\19JUL2022\sample.txt','r')
m=f1.read()
print(m)
f1.close()
# take two word input
word=input("Enter any string:")
replace=input("Enter string you want to replace:")
#convert string into list
temp=m.split(' ')

#print(temp)
for i in range(0,len(temp)):
    if temp[i]==replace:
        temp[i]=word
# print(temp)
# convert list into string and store k variable       
k=' '.join(temp)
print(k)

f1=open('d:\sudhir\basic python\19JUL2022\sample.txt','w')
f1.write(k)
f1.close

