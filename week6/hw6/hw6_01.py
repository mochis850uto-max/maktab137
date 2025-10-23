class Member:
    def __init__(self, name: str, member_id: int, email: str, books_borrowed: list):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.books_borrowed = books_borrowed

    def borrow_book(self, book):
        self.book = book
        if self.book in self.books_borrowed:
            print(f"Book {self.book} has been borrowed.")
        elif self.book not in self.books_borrowed:
            self.books_borrowed.append(self.book)
    def return_book(self, book):
        self.book = book
        if self.book in self.books_borrowed:
            self.books_borrowed.remove(self.book)
        else:
            print(f"The {self.book} book is not borrowed")
    def show_info(self):
        print(f"Member: {self.member_id}\nMember Name: {self.name}\nEmail: {self.email}\nBooks borrowed by the member: {self.books_borrowed}")
    

class Book:
    total_book = 0
    def __init__(self, title: str, author: str, isbn: int, is_borrowed: bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed
        Book.total_book += 1
    def mark_as_borrowed(self):
        if self.is_borrowed == True:
            print(f"This book is borrowed.")
    def mark_as_returned(self):
        if self.is_borrowed == False:
            print(f"This book was returned.")
    def display_info(self):
        print(f"Title: {self.title}\tAuthor: {self.author}\tIsbn: {self.isbn}\tIs borrowed? {self.is_borrowed}")

class Library:
    def __init__(self, name: str, books: list, members: list):
        self.name = name
        self.books = books
        self.members = members
    def add_book(self, book):
        self.book = book
        if self.book not in self.books:
            self.books.append(self.book)
    def add_member(self, member):
        self.member = member
        if self.member not in self.members:
            self.members.append(self.member)
    def borrow_book(self, member_id, isbn):
        self.member_id = member_id
        self.isbn = isbn
        print(f"The book {self.isbn} was loaned to member {self.member_id}.")
    def return_book(self, member_id, isbn):
        self.member_id = member_id
        self.isbn = isbn
        print(f"The book {self.isbn} returned to the library by member {self.member_id}.")
    def show_all_books(self):
        print(f"List of available books: {self.books}")
    def show_all_members(self):
        print(f"List of library members: {self.members}")

class StudentMember(Member):
    def __init__(self, name, member_id, email, books_borrowed):
        super().__init__(name, member_id, email, books_borrowed)
    def borrow_book(self):
        student_books = []
        for self.book in self.books_borrowed:
            student_books.append(self.book)
            if len(student_books)> 3:
                print(f"student member {self.name} can borrow a maximum of 3 books!")

class TeacherMember(Member):
    def __init__(self, name, member_id, email, books_borrowed):
        super().__init__(name, member_id, email, books_borrowed)
    def borrow_book(self):
        teacher_books = []
        for self.book in self.books_borrowed:
            teacher_books.append(self.book)
            if len(teacher_books)> 5:
                print(f"teacher member {self.name} can borrow up to 5 books.")

member_1 = Member("nima", 21, "nimor58@gmail.com", ["black beauty", "sophies world", "animal farm"])
member_2 = Member("sogand", 13, "sogiji@gmail.com", ["they both die at the end", "animal farm"])
member_1.borrow_book("sophies world")
member_2.borrow_book("pride and prejudice")
member_1.return_book("bright nights")
member_2.return_book("animal farm")
member_1.show_info()
member_2.show_info()
book_1 = Book("animal farm", "George Orwell", 978, True)
book_2 = Book("bright nights", "Fyodor Dostoevsky", 852, False)
book_3 = Book("symphony of the dead", "Abbas Maroufi", 967, False)
book_1.mark_as_borrowed()
book_2.mark_as_borrowed()
book_3.mark_as_borrowed()
book_1.mark_as_returned()
book_2.mark_as_returned()
book_3.mark_as_returned()
book_1.display_info()
book_2.display_info()
book_3.display_info()
library = Library("National Library of Iran", ["black beauty", "sophies world", "animal farm", "they both die at the end", "pride and prejudice", "bright nights"],
                  ["nima", "sogand", "sara", "milad", "nina"])
library.add_book("learning french")
library.add_member("nafas")
library.borrow_book(12, 214)
library.return_book(14, 251)
library.show_all_books()
library.show_all_members()
student = StudentMember("changiz", 18, "chancheng2@gmail.com", ["rebecca", "great gatsbi", "1984", "frankenstein"])
student.borrow_book()
teacher = TeacherMember("karim", 20, "kakokarim@gmail.com", ["animal farm", "alchemist", "rebecca"])
