
file=open('user.c','r')
read_file=file.readlines()
#read_file1=file.readlines()
#print(read_file)
file.close()

# find out opening braces
opening_count=0
opening_line=[]
for indx,line in enumerate(read_file):
    for indx1,line1 in enumerate(line):
        if '{'in line1:
            opening_count=opening_count+1
            opening_line.append(indx)
       
                
print('opening braces:',opening_count)
print('opening line no:',opening_line)


# find out closing braces
closing_count=0
closing_line=[]
for indx,line in enumerate(read_file):
    for indx1,line1 in enumerate(line):
        if '}'in line1:
            closing_count=closing_count+1
            closing_line.append(indx)
       
                
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
        














































