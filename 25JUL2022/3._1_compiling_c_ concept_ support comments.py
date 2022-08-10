file=open('user.c','r')
read_file=file.readlines()
#read_file1=file.readlines()
#print(read_file)
file.close()
spliting_list=[]

for i in read_file:
    spliting_list.append(i.split(' '))


# After spliting read_file
# cheak '//' in list line

list1=[]
for indx,line in enumerate(spliting_list):
    for indx,line1 in enumerate(line):        
        #print(line1)
        if '//' in line1: # line1 == '//':
            list1.append(line1.split('//')[0])
            list1.append('\n')
            break
        else:
            list1.append(line1)



fresh_list=' '.join(list1)
print(fresh_list)


'''


opening_count=0
opening_line=[]

for indx1,line1 in enumerate(fresh_list):
    if '{'in line1:
        opening_count=opening_count+1
        opening_line.append(indx1)
       
                
print('opening braces:',opening_count)
print('opening line no:',opening_line)


# find out closing braces
closing_count=0
closing_line=[]

for indx1,line1 in enumerate(fresh_list):
    if '}'in line1:
        closing_count=closing_count+1
        closing_line.append(indx1)
       
                
print('closing braces:',closing_count)
print('closing line no:',closing_line)


if opening_count==closing_count:
    print('program is ok')
else:
    if opening_count>closing_count:
        for i in range(0,len(opening_line)-len(closing_line)):
            print("For the '{' in line",opening_line[i],"there is not '}'")
    else:
        for i in range(0,len(closing_line)-len(opening_line)):
            print("for the '}' in line",closing_line[i],"is not '{'")
        

    
'''
