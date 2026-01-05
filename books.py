from data import books

def add_book(book_id, title, author, quantity):
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    })

def view_books():
    return books
