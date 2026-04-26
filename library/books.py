# library/books.py

books_db = {}

def add_book(book_id, title, author, total_copies):
    books_db[book_id] = {
        'title': title,
        'author': author,
        'total_copies': total_copies,
        'available_copies': total_copies
    }

def get_all_books():
    return books_db

def get_book(book_id):
    return books_db.get(book_id)

def update_available_copies(book_id, delta):
    if book_id in books_db:
        books_db[book_id]['available_copies'] += delta
