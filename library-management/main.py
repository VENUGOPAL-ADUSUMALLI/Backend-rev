from exceptions import *

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return  f'{self.name}, {self.email}'

class Member(Person):
    def __init__(self, name, email, member_id, borrowed_books=None):
        super().__init__(name, email)
        if borrowed_books is None:
            borrowed_books = []
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
        else:
            raise BookNotAvailableError

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise BookNotFound
        else:
            self.borrowed_books.remove(book)
            book.available = True

    def __str__(self):
        return  (f"member {self.name}, has a member-id {self.member_id}, "
                 f"with {self.email}, borrowed-books {self.borrowed_books}")

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available


    def __str__(self):
        return  f"{self.book_id}, {self.title}, {self.author}, {self.available}"

class Library:
    def __init__(self, books, member):
        self.books = books
        self.member = member

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.member.append(member)

    def show_book(self):
        for each in self.books:
            print(each)

    def show_member(self):
        for each in self.member:
            print(each)

    def find_book_by_id(self, id):
        for each in self.books:
            if each.book_id == id:
                return  True
        return False

    def find_member_id(self, id):
        for each in self.member:
            if each.member_id == id:
                return True
        return  False

person1 = Person("venu", "abc")
member1 = Member('venu', 'abc',"1234", [])
member2 = Member('sai', 'abc',"1234", [])
book = Book("123", "Clean-code", "venu", True)
book2 = Book("23", "oops", "venu", True)

library = Library([], [])
library.add_book(book)
library.add_book(book)
print(library.show_book())
library.add_member(member1)
library.add_member(member2)
print(library.show_member())
# print(book.available)
# print(member1)
print(library.find_book_by_id('123'))
print(library.find_member_id('1234'))
try:
    member1.borrow_book(book)
    member1.borrow_book(book2)
    member1.return_book(book)
    member1.return_book(book2)
except BookNotAvailableError:
    print("Book is unavailable")
except BookNotFound:
    print('Book not Found')

# print(member1)
