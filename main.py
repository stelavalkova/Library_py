import myModule as mm

# Creating library instance of Library() class
library = mm.Library()
# Adding books to the library with their autors
library.add_book(mm.Book("The Last Step","Elin Pelin"))
library.add_book(mm.Book("Beloved","Toni Morrison"))
library.add_book(mm.Book("The Castle"," Franz Kafka"))
library.add_book(mm.Book("The Invisible Man","Georgi Gospodinov"))
library.add_book(mm.Book("The Bridge","Petya Dubarova"))


def mainProgram():
    while True:
        mm.display_menu()
        choice = input("Enter your choice: 1 - 4 ")
        
        if choice == '1':
            print(library.list_books())
        
        elif choice == '2':
            title = input("Enter the title of the book you want to borrow: ")
            print(library.borrow_book(title))
        
        elif choice == '3':
            title = input("Enter the title of the book you want to return: ")
            print(library.return_book(title))
        
        elif choice == '4':
            print("Exit")
            break
        
        else:
            print("Invalid choice, please try again.")

mainProgram()
