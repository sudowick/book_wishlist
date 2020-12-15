from .database_connection import DatabaseConnection


def create_table():
    with DatabaseConnection('data.db') as cursor:
        #cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(title text,author text,read integer)')


def insert_book(title, author):
    with DatabaseConnection('data.db') as cursor:
        #cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?,0)', (title, author))


def display():
    with DatabaseConnection('data.db') as cursor:
        #cursor = connection.cursor()
        cursor.execute('SELECT * from books ORDER BY read')
        data = [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
        return data

def mark_read(title):
    with DatabaseConnection('data.db') as cursor:
        #cursor = connection.cursor()
        cursor.execute('Update books SET read = 1 WHERE title = ?', (title,))


def delete(title):
    with DatabaseConnection('data.db') as cursor:
        #cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE title = ?', (title,))
