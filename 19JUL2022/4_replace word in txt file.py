f1=open('D:\sample.txt','r')
word=input("Enter any string:")
replace=input("Enter string you want to replace:")
input_data = f1.read()
f1.close()
for i in range(len(input_data)):
    if input_data[i]==word:
        print(input_data[i])       

# Replace the target string
#input_data = input_data.replace(word,replace)

# Write the output to same file
#f2 = open('D:\sample.txt', 'w')
#f2.write(input_data)
#f2.close()
