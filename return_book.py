from datetime import date
from data import books
from members import members
from issue_book import issued_books

FINE_PER_DAY = 2

def return_book(book_id, member_id):
    for record in issued_books:
        if record["book_id"] == book_id and record["member_id"] == member_id:
            late_days = (date.today() - record["due_date"]).days
            fine = late_days * FINE_PER_DAY if late_days > 0 else 0

            for book in books:
                if book["id"] == book_id:
                    book["quantity"] += 1

            for member in members:
                if member["id"] == member_id:
                    member["issued_books"].remove(book_id)
                    member["fine"] += fine

            issued_books.remove(record)
            return fine
    return None
