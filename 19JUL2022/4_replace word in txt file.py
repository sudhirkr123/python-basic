userFile = r'D:\sudhir\basic python\19JUL2022\sample2.txt'

f1=open(userFile,'r')
m=f1.read()
print(m)
f1.close()
# take two word input
replace=input("enter text that will replace:")
word=input("Enter text to be replaced:")
#convert string into list
temp=m.split(' ')

#print(temp)
for i in range(0,len(temp)):
    if temp[i]==replace:
        temp[i]=word
# print(temp)
# convert list into string and store k variable       
k=' '.join(temp)

'''
f2=open(r'D:\sudhir\basic python\19JUL2022\sample.txt','w')
print(k, type(k))
f2.write("python is programming.")
f2.close
'''

with open(userFile,'w') as f2:
    print(k)
    f2.write(k)

