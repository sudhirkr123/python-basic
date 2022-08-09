file=open('user.c','r')
read_file=file.readlines()
#read_file1=file.readlines()
#print(read_file)
file.close()


for i in read_file:
    
    if '//' not in i:
        print(i)


'''

#print(len(read_file))
for i in read_file:
    list1.append(i.split(','))
    
#print(list1)


length=len(list1)
print(length)

for i in list1:
    for j in i:
        if j=='//':
            print('i')




for i in range(0,len(read_file)):
    if read_file[i]=='//':
        print(i)
    else:
        print(read_file[i])
'''

'''
        
for i in read_file:
    if '//' not in i:
        print(i)
     
'''



'''
for indx,line in enumerate(read_file):    
    line =line,indx.pop()
    
    read_file[indx] =line
print('paragraph: ',read_file)

'''
'''

for indx,line in enumerate(read_file):
    for indx1,line1 in enumerate(line):
        if '//' not in i:
            print(line1)

'''
