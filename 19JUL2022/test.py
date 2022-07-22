'''
#read the file
reading_file = open("d:\\sample.txt", "r")
new_file_content = ""
for line in reading_file:
    stripped_line = line.strip()
    new_line = stripped_line.replace("india", "nd")
    new_file_content += new_line +"\n"
reading_file.close()

writing_file = open("d:\\sample.txt", "w")
writing_file.write(new_file_content)
writing_file.close()
'''


list1=['name','kumar','pfgh\n']

'''
list3=list1[:2]
print(list3)
list2=[]
list2=list1[-1]
print(list2)

del list1[-1]

m=list3.append(list2)
'''

print(list1[-1].split('\n')[0], type(list1[-1].split('\n')[0]))
print()
list1[-1] = list1[-1].split('\n')
print(list1)
list1[-1] = list1[-1][0]
print(list1)
