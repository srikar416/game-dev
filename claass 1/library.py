# #1. **Add a book** to our library.
# 2. **Delete a book** from the library.
# 3. **Show info** of all books in the library.

# We will have three types of books:

# - **Book (Parent Class)** – has title & author.
# - **EBook (Child Class)** – can also be downloaded.
# - **AudioBook (Child Class)** – can also play audio samples.

# All books should be stored in a **list** (our digital catalog).

# ---

# ### Requirements

# 1. **Book (Parent class)**
#     - Attributes: `title`, `author`
#     - Method: `show_info()`
# 2. **EBook (Child class)**
#     - Inherits from Book
#     - Method: `download()`
# 3. **AudioBook (Child class)**
#     - Inherits from Book
#     - Method: `play_sample()`
# 4. **Library** (manages a collection of books using a `list`)
#     - Method: `add_book(book)`
#     - Method: `remove_book(title)`
#     - Method: `show_all_books()`
class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        print("An object is created for a book")
    def show_info(self):
        print(f"This books title is {self.title} and the author is {self.author}")
class EBook(Book):
    def __init__(self, Book):
        pass
    def download(self):
        print(f"Downloading EBook: {self.title}")
class AudioBook(Book):
    def play_sample(self):
        print(f"Playing sample from: {self.title}")
class Library:        
        def __init__(self):
            self.books=[]
        def add_book(self, book):
            self.books.append(book)
            print(f"Added: {book.title}")
        def remove_book(self, title):
            for book in self.books:
                if book.title== title:
                    self.books.remove(book)
            print(f"{title} does not exist in the library")
        def show_all_books(self):
            for book in self.books:
                book.show_info()
b1= Book("Harry Potter", "JK Rowling")
b2=EBook("The kite runner", "Khaled Husseini")
b3=AudioBook("Pyschology of money", "Morgan Housel")
lib=Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.remove_book("The kite runner")
lib.show_all_books()

