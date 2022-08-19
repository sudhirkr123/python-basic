from menuFunc import display_data,adding_book,searching_book
from menuFunc import deleting_books,editing_book

print("------------Library Management System------------\n")
print("1.Display\n2.Adding\n3.Searching\n4.Editing\n5.Deleting\n6.Exist")
choice=True
while True:
    choice=int(input("\nEnter your Choice:"))
    if choice== 1:
        # display all data
        display_data()
        
    elif choice== 2:
        # Adding
        adding_book()
      
    elif choice== 3:
        #searching
        searching_book()
        
          
    elif choice== 4:
        editing_book()
              
    elif choice== 5:
        #deleting
        deleting_books()
        
    elif choice== 6:
        print('---bye bye---')
        break
    
    else:
        print('Invalid option')
