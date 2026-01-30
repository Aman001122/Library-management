from datetime import date, timedelta
from data import books
from members import members
from fine_calculator import calculate_fine
def check_fine(book_id, member_id):
    for record in issued_books:
        if record["book_id"] == book_id and record["member_id"] == member_id:
            return calculate_fine(record["due_date"])
    return None

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


def return_book(book_id, member_id):
    for record in issued_books:
        if record["book_id"] == book_id and record["member_id"] == member_id:
            fine = calculate_fine(record["due_date"])

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
