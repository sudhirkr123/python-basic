
# Read two file items
f1=open(r'D:\sudhir\basic python\19JUL2022\test1.txt','r')
m1=f1.read()
print('list1 items:')
print(m1)
f2=open(r'D:\sudhir\basic python\19JUL2022\test2.txt','r')
m2=f2.read()
print('\nlist2 items:')
print(m2)
f1.close()
f2.close()
# convert string into list format.
temp1=m1.split('\n')
temp2=m2.split('\n')

#compare two items.
common=set(temp1).intersection(temp2)
print('\ncommon items is:')
for i in common:
    print(i)


    


