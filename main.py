import os
from books import add_book, view_books
from members import add_member, view_members
from issue_book import issue_book
from return_book import return_book
from reports import issued_books_report, members_report

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def success(msg):
    print("✔", msg)

def error(msg):
    print("✖", msg)

def print_table(headers, rows):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, item in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(item)))

    def line():
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

    def print_row(row):
        print("| " + " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))) + " |")

    line()
    print_row(headers)
    line()
    for row in rows:
        print_row(row)
    line()

while True:
    clear()
    print("=" * 60)
    print("📚 LIBRARY MANAGEMENT & FINE CALCULATION SYSTEM 📚".center(60))
    print("=" * 60)

    print("""
1. 📚 Add Book
2. 📚 View Books
3. 👤 Add Member
4. 👤 View Members
5. 📤 Issue Book
6. 📥 Return Book
7. 📊 Issued Books Report
8. 📊 Members Report
9. ❌ Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book(
            input("Book ID: "),
            input("Title: "),
            input("Author: "),
            int(input("Quantity: "))
        )
        success("Book added successfully")
        pause()

    elif choice == "2":
        books = view_books()
        if books:
            print_table(
                ["ID", "Title", "Author", "Quantity"],
                [[b["id"], b["title"], b["author"], b["quantity"]] for b in books]
            )
        else:
            error("No books available")
        pause()

    elif choice == "3":
        add_member(input("Member ID: "), input("Name: "))
        success("Member added successfully")
        pause()

    elif choice == "4":
        members = view_members()
        if members:
            print_table(
                ["ID", "Name", "Issued Books", "Fine"],
                [[m["id"], m["name"], ",".join(m["issued_books"]), m["fine"]] for m in members]
            )
        else:
            error("No members registered")
        pause()

    elif choice == "5":
        if issue_book(input("Book ID: "), input("Member ID: ")):
            success("Book issued successfully (Due in 7 days)")
        else:
            error("Issue failed (check IDs or quantity)")
        pause()

    elif choice == "6":
        fine = return_book(input("Book ID: "), input("Member ID: "))
        if fine is None:
            error("Invalid return request")
        elif fine == 0:
            success("Book returned on time. No fine.")
        else:
            print("⚠ Late return — Fine: ₹", fine)
        pause()

    elif choice == "7":
        issued = issued_books_report()
        if issued:
            print_table(
                ["Book ID", "Member ID", "Due Date"],
                [[i["book_id"], i["member_id"], i["due_date"].strftime("%d-%b-%Y")] for i in issued]
            )
        else:
            error("No issued books")
        pause()

    elif choice == "8":
        members = members_report()
        if members:
            print_table(
                ["ID", "Name", "Issued Books", "Fine"],
                [[m["id"], m["name"], ",".join(m["issued_books"]), m["fine"]] for m in members]
            )
        else:
            error("No members")
        pause()

    elif choice == "9":
        break
