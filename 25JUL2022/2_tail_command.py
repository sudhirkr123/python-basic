'''
 -n num->Prints the last ‘num’ lines instead of last 10 lines.
 num is mandatory to be specified in command otherwise it displays an error.
  ex-$ tail -n 3 state.txt

'''

def Display_last_line(number,file):
    f=open(file,"r")
    m=f.readlines()
    #print(m)
    f.close()
    length=len(m)
    #print(length)
    # type cast
    num=int(number)
    for i in range(length-num,length,1):
        print(m[i])


'''
  -c num -> Prints the last ‘num’ bytes from the file specified.
   Newline count as a single character, so if tail prints out a newline,
   it will count it as a byte.
'''
def Display_last_byte(byte,file_location,):
    f=open(file_location,"r")
    string=f.read()
    #print(string)
    length=len(string)
    # take one string variable to store last byte
    last_byte=""
    # type cast
    number=int(byte)
    for i in range(length-1,length-1-number,-1):
        last_byte=last_byte+string[i]
    #print(last_byte)

        
    #reverse the string
    result=""
    for i in range(len(last_byte)-1,-1,-1):
        result=result+last_byte[i]
    print(result)
    


# Tail command 
import os
user=input("Enter your commmand:")
user1=user
m1=user1.split(' ')

#check user command 
if m1[0]=='tail':
    if m1[1]=='-n':
        #if m1[2]=='"user"':
        
        #checking file or not
        file=os.path.isfile(m1[3])
        if file==True:
            # call the function
            Display_last_line(m1[2],m1[3])       
        else:
            print('file is not found')

            
    elif m1[1]=='-c':
        
       # if m1[2]=='"user"':
       # checking file or not
        file=os.path.isfile(m1[3])
        if file==True:
            # call the function
            Display_last_byte(m1[2],m1[3])
        else:
            print('file is not found')
    
    else:
        print('invalid option')
else:
    print('invalid command')
