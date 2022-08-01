user=input("Enter your commmand:")
user1=user
m1=user1.split(' ')
print(m1)
print(type(m1[2]))
print(type(m1[0]))
m2=m1[0]
m5=m1[3]
print(m5)


'''
import os
m=os.path.isfile('textFile1.txt')
if m==True:
    print('file is there')
else:
    print('file is not found')



$ grep -o "java" geekfile.txt
Displaying only the matched pattern :
--------------------------------------->
By default, grep displays the entire line which has the matched string.
We can make the grep to display only the matched string by using the -o option.
$ grep -o "java" geekfile.txt


def Displaying_only_the_matched_pattern(x): 

    file1_location=x
    # read the file1.
    f=open(file1_location,'r')
    read_file1=f.readlines()
    print(read_file1)
    #print()
    # find the length
    length=len(read_file1)
    #print(length, end= '\n\n')
    
    # cleaning the list
    clean_list=[]
    
    # remove the dot,backslashand comma in paragraph
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
    user="Java"
    count=0
    words=clean_list
    print(words)
    for word in words:
        if word==user:
            count=count+1       

    
    if count>0:
        for i in range(count):
            print(user)
    else:
        print('not found')



x="textfile1.txt"

Displaying_only_the_matched_pattern(x) 

'''





'''
Displaying the count of number of matches :
--------------------------------------------------->
We can find the number of lines that matches the given string/pattern 
command-->$grep -c "unix" geekfile.txt.





file1_location="textFile1.txt"
# read the file1.
f=open(file1_location,'r')
read_file1=f.readlines()
#print(read_file1)
print()

# remove the dot,backslashand comma in paragraph
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
user="Java"
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
print(list1)
s=0
for i in list1:
    if i>0:
         s=s+i
print(user,'is',s,'times')
    






def Number_of_occurrences(x):
    file1_location=x
    # read the file1.
    f=open(file1_location,'r')
    read_file1=f.readlines()
    #print(read_file1)
    #print()
    # find the length
    length=len(read_file1)
    #print(length, end= '\n\n')
    
    # cleaning the list
    clean_list=[]
    
    # remove the dot,backslashand comma in paragraph
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
    
    print(clean_list)
    temp1=clean_list
    
   
    length=len(temp1)
    #print(length)
    
    string=[]
    print('Number of occurences:')
    for i in range(0,length):  
        count = 1;  
        for j in range(i+1,length):  
            if(temp1[i] == (temp1[j])):  
                count = count + 1  
                #Set words[j] to 0 to avoid printing visited word      
                temp1[j] = "0"  
              
        #Displays the duplicate word if count is greater than 1  
        if(count > 1 and temp1[i] != "0"):  
            print(temp1[i])
'''


'''

def Number_of_occurrences(x):
    file1_location=x
    # read the file1.
    f=open(file1_location,'r')
    read_file1=f.readlines()
    #print(read_file1)
    #print()
    # find the length
    length=len(read_file1)
    #print(length, end= '\n\n')
    
    # cleaning the list
    clean_list=[]
    
    # remove the dot,backslashand comma in paragraph
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
    
    print(clean_list)
    temp1=clean_list
    
   
    length=len(temp1)
    #print(length)
    
    string=[]
    print('Number of occurences:')
    for i in range(0,length):  
        count = 1;  
        for j in range(i+1,length):  
            if(temp1[i] == (temp1[j])):  
                count = count + 1  
                #Set words[j] to 0 to avoid printing visited word      
                temp1[j] = "0"  
              
        #Displays the duplicate word if count is greater than 1  
        if(count > 1 and temp1[i] != "0"):  
            print(temp1[i])

def Number_of_occurrences(x):

    file1_location=r'D:\sudhir\basic python\25JUL2022\textFile1.txt'
     # read the file1.
    f=open(file1_location,'r')
    read_file1=f.readlines()
    
    print(read_file1)
    print()
    # remove the last word in \n
    clean_list=[]
    for x in read_file1:
        clean_list.append(x.replace("\n", ""))
    #print(clean_list)

    # Remove . in paragraph
    fresh_list=[]
    for j in clean_list:
        fresh_list.append(x.replace(".", ""))
    #print(fresh_list)
    
    # convert list of lines into string
    listToStr = ' '.join(map(str, fresh_list))
    #print(listToStr)
    
    # convert string into list format

    temp1=listToStr.split(" ")
    print(temp1)

  

    file1_location=r'D:\sudhir\basic python\25JUL2022\textFile1.txt'
    # read the file1.
    f=open(file1_location,'r')
    read_file1=f.readlines()
    #print(read_file1)
    #print()
    # find the length
    length=len(read_file1)
    #print(length, end= '\n\n')
    
    # cleaning the list
    clean_list=[]

    for indx,line in enumerate(read_file1):
        
        line =line.replace('\n', '')
        line =line.replace('.', '')
        line =line.replace(',', '')
        
        read_file1[indx] =line
   # print('paragraph: ',read_file1)
   # print()

    clean_list=[]
    for word in read_file1:
        clean_list=clean_list+word.split(' ')
    
    print(clean_list)
    temp1=clean_list
    
'''

