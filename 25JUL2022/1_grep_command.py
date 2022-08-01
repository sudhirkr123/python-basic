# grep cammond
# create a function to find Number_of_occurrences
'''
Displaying the count of number of matches :
--------------------------------------------------->
We can find the number of lines that matches the given string/pattern 
command-->$grep -c "unix" geekfile.txt.

'''

def Number_of_occurrences(file,pattern):
    file1_location=file
    # read the file1.
    f=open(file1_location,'r')
    read_file1=f.readlines()
    #print(read_file1)
    print()

    # remove the dot,backslash and comma in paragraph
    # list cleaning
    for indx,line in enumerate(read_file1):
        
        line =line.replace('\n', '')
        line =line.replace('.', '')
        line =line.replace(',', '')
        
        read_file1[indx] =line
    #print('paragraph: ',read_file1)

    #convert list of list in each word
    list_of_list=[]
    for i in read_file1:
        list_of_list.append(i.split(" "))
    print()
    print(list_of_list)

    # search in java how many lines existing.
    #count=0
    user=pattern.replace('"','')
    
    list1=[]
    #for each_list in list_of_list:
    for each_list in list_of_list:
        count=0
        #print('--->',each_list)
        for word in each_list:
        #print('====',word)
            if user==word:
                count=count+1
        list1.append(count)
    print()
    print('Number of occurrences Each Line:',list1)
    s=0
    for i in list1:
        if i>0:
            s=s+i
    print()
    print("total Number Of Occurrences:",s)


'''
$ grep -o "java" geekfile.txt
Displaying only the matched pattern :
--------------------------------------->
By default, grep displays the entire line which has the matched string.
We can make the grep to display only the matched string by using the -o option.
$ grep -o "java" geekfile.txt
'''


def Displaying_only_the_matched_pattern(file,pattern): 

    file1_location=file
    # read the file1.
    f=open(file1_location,'r')
    read_file1=f.readlines()
    print(read_file1)
    print()
    # find the length
    length=len(read_file1)
    #print(length, end= '\n\n')
    
    # cleaning the list
    clean_list=[]
    
    # remove the dot,backslash and comma in paragraph
    for indx,line in enumerate(read_file1):
        
        line =line.replace('\n', '')
        line =line.replace('.', '')
        line =line.replace(',', '')
        
        read_file1[indx] =line
   # print('paragraph: ',read_file1)
   # print()
    # convert the word into list formate
    clean_list=[]
    for word in read_file1:
        clean_list=clean_list+word.split(' ')

    #words=string.split(" ")
    user=pattern.replace('"','')
    count=0
    words=clean_list
    #print(words)
    for word in words:
        if word==user:
            count=count+1       

    
    if count>0:
        for i in range(count):
            print(user)
    else:
        print('not found')




# grep-v->this prints out all the lines that do not matches the pattern,
# grep[option] pattern[filesname]

# grep[option] pattern[filesname]
# Enter your command,
import os
user1=input("Enter your commmand:")
m1=user1.split(' ')

#check user command 
if m1[0]=='grep':
    if m1[1]=='-c':
        #if m1[2]=='"user"':
        
        #checking file or not
        file=os.path.isfile(m1[3])
        if file==True:
            # call the function
             Number_of_occurrences(m1[3],m1[2])
        else:
            print('file is not found')

            
    elif m1[1]=='-o':
        
       # if m1[2]=='"user"':
       # checking file or not
        file=os.path.isfile(m1[3])
        if file==True:
            # call the function
             Displaying_only_the_matched_pattern(m1[3],m1[2])
        else:
            print('file is not found')
    
    else:
        print('invalid option')
else:
    print('invalid command')
  
   

