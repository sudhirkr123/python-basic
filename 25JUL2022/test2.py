'''
$ grep -o "java" geekfile.txt
Displaying only the matched pattern :
--------------------------------------->
By default, grep displays the entire line which has the matched string.
We can make the grep to display only the matched string by using the -o option.
$ grep -o "java" geekfile.txt



string='java is good programming language java is advance level programming language it is very good security java'
user='java'
words=string.split(" ")
count=0
for word in words:
    if word==user:
        count=count+1       

    
if count>0:
    for i in range(count):
        print(user)
else:
    print('not found')


'''






'''
Displaying the count of number of matches :
--------------------------------------------------->
We can find the number of lines that matches the given string/pattern 
command-->$grep -c "unix" geekfile.txt.

'''



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
    


    

