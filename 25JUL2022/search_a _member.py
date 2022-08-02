file=open("phone_records.csv","r")
dict1=file.readlines()
print(dict1)
#search=input("Enter name you want to search:")
file.close()
length=len(dict1)
print(length)
list1=[]
for i in range(0,length):
    print(dict1[i])
    for j in range(0,i):
        list1.append(dict1[j].split(","))
print(list1)

search_name=input("Enter your name you want to search:")
length=len(list1)
for i in list1:
    for j in i:
        if search_name==j:
            print(j)
        else:
            print('Not found')
























'''
# importing the csv library
import csv

# opening the csv file
with open('phone_record.csv') as csv_file:
    # reading the csv file using DictReader
    csv_reader = csv.DictReader(csv_file)
    # converting the file to dictionary
    # by first converting to list
    # and then converting the list to dict
    dict_from_csv = dict(list(csv_reader)[0])

    # making a list from the keys of the dict
    list_of_column_names = list(dict_from_csv.keys())

    # displaying the list of column names
    print("List of column names : ",list_of_column_names)

'''
