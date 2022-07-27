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
        read_file1[x]=read_file1[x].split('\n')
        read_file1[x]=read_file1[x][0]
    print('paragraph: ',read_file1)
   
 
    
Number_of_occurrences()
