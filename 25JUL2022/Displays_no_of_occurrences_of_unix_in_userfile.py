# grep cammond

# grep-v->this prints out all the lines that do not matches the pattern,
# grep[option] pattern[filesname]

# grep[option] pattern[filesname]
# Enter your command,
user=input("Enter your commmand:")
user1=user
m1=user1.split(' ')

#check user command 
if m1[0]=='grep':
    if m1[1]=='-v':
        if m1[2]=='"unix"':
            if m1[3]=='textFile1.txt' or m1[3]=='textFile2.txt':

                # call the function
                
                print('run to -v function')
            else:
                print('file not found')
        else:
            print('pattern not found')
    elif m1[1]=='-w':
        
        if m1[2]=='"unix"':
            
            if m1[3]=='textFile1.txt' or m1[3]=='textFile2.txt':
                # call function
                Number_of_occurrences()
                print('run to -w function')
                
            else:
                print('file not found')
        else:
            print('pattern not found')
    else:
        print('invalid option')
else:
    print('invalid command')



def Number_of_occurrences():
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

    
    
    length=len(temp1)
    
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
          
    

















