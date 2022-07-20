# Read dictionary file
f1=open(r'D:\sudhir\basic python\19JUL2022\dictionary.txt','r+')
m1=f1.read()
print('dictionary items')
print(m1)
f1.close()

# Read user file
f2=open(r'D:\sudhir\basic python\19JUL2022\sample.txt','r')
m2=f2.read()
print('\nuser paragraph:')
print(m2)
f2.close()
#dictionary items convert list format
temp1=m1.split('\n')
print(temp1)
temp2=m2.split(' ')
print(temp2)

