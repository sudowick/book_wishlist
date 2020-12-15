from utils import database

menu = """
a - Add a book
l - List all books
r - Mark a book as read
d - Remove a book from list
q - QUIT
Enter Your Choice -----
"""


def user_menu():
    database.create_table()
    ch = input(menu).lower()

    while ch != 'q':
        if ch == 'a':
            add_book()
        elif ch == 'l':
            display()
        elif ch == 'r':
            read()
        elif ch == 'd':
            delete()
        elif ch == 'q':
            exit()
        ch = input(menu).lower()


def add_book():
    name = input('Enter the new book name: ').upper()
    author = input('Enter the new book author: ').upper()
    database.insert_book(name, author)


def display():
    for book in database.display():
        read = "YES"
        if not book['read']:
            read = "NO"
        print(f'{book["title"]} by {book["author"]}, Read :{read}')
        print()


def read():
    title = input('Enter name of book to mark it read ---').upper()
    database.mark_read(title)


def delete():
    title = input('Enter name of book to Delete ---').upper()
    database.delete(title)


user_menu()
