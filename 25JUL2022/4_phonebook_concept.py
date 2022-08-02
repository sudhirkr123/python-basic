# create a file
try:   
    file=open("phone_records.csv","x")
    print("new file created Successfuly")
except FileExistsError:
        print("file already present")

# Create menu
print("------------Welcome to Menu------------\n")
print("a)Add a new member\nb)Modify a member\nc)Search a member\nd)Delete a member\ne)Exist")
#choice=input("\nEnter your Choice:")
choice=True
while choice:
    choice=input("\nEnter your Choice:")
    if choice=='a' or choice=='A':
        print("Add the new records")
    elif choice=='b' or choice=='B':
        print("Modify a Member")
    elif choice=='c' or choice=='C':
        print("Search a member")
    elif choice=='d' or choice=='D':
        print('Delete a member')
    elif choice=='e' or choice=='E':
        print('---bye bye---')
        break
    else:
        print('Invalid option')

