# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"'{self.title}' :Successfully borrowed ."
        else:
            return f"Sorry, '{self.title}' is already borrowed."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"Thank you for returning '{self.title}'."
        else:
            return f"'{self.title}' was not borrowed."
# Library class 
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            return "No books available in the library."
        book_list = []
        for book in self.books:
            availability = "Available" if book.is_available else "Not Available"
            book_list.append(f"'{book.title}' by {book.author} - {availability}")
        return "\n".join(book_list)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            return book.borrow()
        else:
            return f"Sorry, we couldn't find a book with the title '{title}'."

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            return book.return_book()
        else:
            return f"Sorry, we couldn't find a book with the title '{title}'."
        
# Function that displays menu
def display_menu():
    print("\nLibrary Menu:")
    print("1. View all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")