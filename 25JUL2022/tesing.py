
def Number_of_occurrences(a):
    file1_location=a
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
        #print('-->',indx)
        #for y in line:
          #  print('==>',y)

        '''    
        read_file1[indx]=read_file1[indx].replace('\n', '')
        read_file1[indx]=read_file1[indx].replace('.', '')
        read_file1[indx]=read_file1[indx].replace(',', '')
        '''
        
        line =line.replace('\n', '')
        line =line.replace('.', '')
        line =line.replace(',', '')
        
        read_file1[indx] =line
        #print('message:',read_file1[indx])
        
        '''
        if '\n' in indx or "." in indx:
        line = read_file1[indx].replace('\n', '')
        line = read_file1[indx].replace('.', '')
        line = read_file1[indx].replace(',', '')
        #print('::: ', line)
        '''
   # print('paragraph: ',read_file1)
   # print()

    clean_list=[]
    for word in read_file1:
        clean_list=clean_list+word.split(' ')
    
    print(clean_list)
    temp1=clean_list
    #temp1.lower()

    # code for number of occurences
    length=len(temp1)
    print(length)
    
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
          
    
    

    
    
a='userFile1.txt'    
Number_of_occurrences(r'D:\sudhir\basic python\25JUL2022\')



    
