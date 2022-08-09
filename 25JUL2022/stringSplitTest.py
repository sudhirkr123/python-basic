file=open('user.c','r')
read_file=file.readlines()
#read_file1=file.readlines()
#print(read_file)
file.close()
list1=[]
for i in read_file:
    if '//' not in i:
        print(i)


'''

for indx,line in enumerate(read_file):
    for indx1,line1 in enumerate(line):
        if '//' not in i:
            print(line1)

'''











    


'''
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
            print('For the { in line',opening_line[i],'there is not closing brace')
    else:
        for i in range(0,len(closing_line)-len(opening_line)):
            print('for the } in line',closing_line[i],'is not opening brace')
        


'''









'''
# count opening brace
count_opening=0
for i in read_file:
   if '{' in i:
       count_opening=count_opening+1
print('opening brace:',count_opening)

# count closing brace
count_closing=0
for i in read_file:
    if '}' in i:
        count_closing=count_closing+1
print('closing brace:',count_closing)


# compare opening and closing 
if count_opening==count_closing:
    print('program is ok')  # true part
    
else:
    opening_count=0
    list1=[]
    for indx,line in enumerate(read_file):
        for indx1,line1 in enumerate(line):
            if '{'in line1:
               opening_count=opening_count+1
               list1.append(indx)
       
                
    print(opening_count)
    print(list1)
















file=open('user.c','r')
read_file=file.readlines()
#print(read_file)
file.close()
# count opening brace
count_opening=0
for indx,line in enumerate(read_file):
    if '{' in line:
        count_opening=count_opening+1
        
print(count_opening)



list1=[]
for i in read_file:
    list1.append(i.split(','))
print(list1)

# find the opening braces
count_opening=0
for i in list1:
    for j in i:
        for k in j:
            if '{' in k:
                count_opening=count_opening+1
          
print('opening braces:',count_opening)

# find the closing braces
list2=[]
count_closing=0
for i in range(len(list1)):
    for j in range(0,i):
        for k in range(0,j):
            if '}' in k[j]:
                count_closing=count_closing+1
        
          
print('closing braces:',count_closing)
print(list2)









count_opening=0
for i in read_file:
   if '{' in i:
       count_opening=count_opening+1
print('opening brace:',count_opening)

# count closing brace
count_closing=0
for i in read_file:
    if '}' in i:
        count_closing=count_closing+1
print('closing brace:',count_closing)
'''






























'''
stringlist = [ 'hello', '"WORD"', 'okay' ]
#m=stringlist[1].split('"')
m=stringlist[1].replace('"','')
print(m)

string='"ram"'
print(string)
m=string.replace('"','')
print(m)

'''

'''
def Display_last_line(file,number):
    f=open(file,"r")
    m=f.readlines()
    print(m)
    f.close()
    length=len(m)
    print(length)
    for i in range(length-number,length,1):
        print(m[i])

file="textFile1.txt"
number=5
Display_last_line("textFile1.txt",2)
'''
'''
def Display_last_byte(file_location,byte):
    f=open(file_location,"r")
    string=f.read()
    #print(string)
    length=len(string)
    last_byte=""
    for i in range(length-byte,length+1,1):
        last_byte=last_byte+string[i]

        
    #print(last_byte)
    #reverse the string
    #result=""
    #for i in range(len(last_byte)-1,-1,-1):
     #   result=result+last_byte[i]
    #print(result)
                   




Display_last_byte("file.txt",5)
'''

'''
string="java is good programming language"
num=10
s=""
length=len(string)
print(length)
for i in range(length-1,length-1-num,-1):
    s=s+string[i]
print(s)
'''

