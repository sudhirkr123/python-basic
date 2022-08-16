import csvHandler as control

# Create menu Libraries
print("------------Welcome to Libraries Book------------\n")
print("a)Adding\nb)searching\nc)editing\nd)deleting books\ne)Exist")
choice=True
while choice:
    choice=input("\nEnter your Choice:")
    if choice.lower()=='a':
        # adding
        control.adding_book()
        
    elif choice.lower()=='b':
        # searching
        print('Searching')

           
    elif choice.lower=='c':
         # editing
         print('editing')

         
    elif choice.lower()=='d':
        # delete
        print('delete')

        
    elif choice.lower()=='e':
        print('---bye bye---')
        break
    
    else:
        print('Invalid option')
