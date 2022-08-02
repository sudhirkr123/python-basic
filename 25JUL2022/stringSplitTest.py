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
string="java is good programming language"
num=10
s=""
length=len(string)
print(length)
for i in range(length-1,length-1-num,-1):
    s=s+string[i]
print(s)
'''

