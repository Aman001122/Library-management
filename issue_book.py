from datetime import date, timedelta
from data import books
from members import members

issued_books = []

def issue_book(book_id, member_id):
    for book in books:
        if book["id"] == book_id and book["quantity"] > 0:
            for member in members:
                if member["id"] == member_id:
                    due_date = date.today() + timedelta(days=7)

                    issued_books.append({
                        "book_id": book_id,
                        "member_id": member_id,
                        "due_date": due_date
                    })

                    member["issued_books"].append(book_id)
                    book["quantity"] -= 1
                    return True
    return False
