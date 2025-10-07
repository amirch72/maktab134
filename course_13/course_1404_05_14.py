from datetime import datetime


class Person:
    def __init__(self, username, first_name, last_name, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self._password = password
        self.is_authenticated = False
        self.last_login = None
        self.date_register = datetime.now()
        self.credit = 0

    @property
    def password(self):
        return "***"

    @password.setter
    def password(self, value):
        self._password = f"@{value}$"

    def login(self):
        self.is_authenticated = True
        self.last_login = datetime.now()


current_user = Person("amir1404", "Amir", "Alavi", "@miR1404")
# current_user.login()

# def name(func):
#     def wrapper(argument):
#         pass
#         output =  func(argument)
#         return output
#     return wrapper


# @name
# def test(argument):
#     pass


def login_dec(func):
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return func(*args, **kwargs)
        print("Please login")

    return wrapper


class Book:
    def __init__(self, name, category, id, price):
        self.name = name
        self.uuid = id
        self.category = category
        self.price = price


class Library:
    def __init__(self):
        self.name = "Maktab"
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    @login_dec
    def show_books(self):
        # books_name = []
        # for book in self.books:
        #    books_name.append(book.name)

        books_name = [f"{i.uuid}- {i.name}" for i in self.books]
        print(" , ".join(books_name))

    @login_dec
    def search_book(self, name):
        for book in self.books:
            if book.name == name:
                return book
        return False

    def search_by_category_generator(self, category):
        for book in self.books:
            if book.category == category:
                yield book

    def search_by_category_simple(self, category):
        for book in self.books:
            if book.category == category:
                return book


maktab_lib = Library()
book_1 = Book("Farsi 1", "Amoozeshi", "011", 45000)
book_2 = Book("Riyazi 1", "Amoozeshi", "021", 47000)
book_3 = Book("Farsi 2", "Amoozeshi", "012", 50000)
book_4 = Book("Oloom 2", "Amoozeshi", "032", 32000)

maktab_lib.add_book(book_1)
maktab_lib.add_book(book_2)
maktab_lib.add_book(book_3)
maktab_lib.add_book(book_4)
# print(maktab_lib.name)
# # print(maktab_lib.books)
# print(maktab_lib.show_books())
search_category = maktab_lib.search_by_category_generator("Amoozeshi")
# print("Search by Category: ", search_category)
for i in search_category:
    print(i.name)
    if i.name == "Farsi 1":
        break

print("---------------------------------")

for i in search_category:
    print(i.name)
    

# print("Search by Category: ", maktab_lib.search_by_category_simple("Amoozeshi").name)

# maktab_lib.show_books()
# search_result = maktab_lib.search_book("Farsi 1")
# print(search_result.category if search_result else "Not Found")
