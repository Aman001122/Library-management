import os
from books import add_book, get_all_books
from members import add_member, get_all_members
from issue_return import issue_book, return_book, check_fine
from reports import issued_books_report, members_report

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def success(msg):
    print("\n✔", msg)

def error(msg):
    print("\n✖", msg)

def header(title):
    print("=" * 70)
    print(title.center(70))
    print("=" * 70)

def print_table(headers, rows):
    widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(str(val)))

    def line():
        print("+" + "+".join("-" * (w + 2) for w in widths) + "+")

    def show(row):
        print("| " + " | ".join(str(row[i]).ljust(widths[i]) for i in range(len(row))) + " |")

    line()
    show(headers)
    line()
    for r in rows:
        show(r)
    line()

while True:
    clear()
    header("📚 LIBRARY MANAGEMENT & FINE CALCULATION SYSTEM 📚")

    print("""
1. 📘 Add Book
2. 📘 View Books
3. 👤 Add Member
4. 👤 View Members
5. 📤 Issue Book
6. 📥 Return Book
7. 📊 Issued Books Report
8. 📊 Members Report
9. 💰 Check Fine
10. ❌ Exit
""")

    choice = input("Enter your choice: ")

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
        books = get_all_books()
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
        members = get_all_members()
        if members:
            print_table(
                ["ID", "Name", "Issued Books", "Fine"],
                [[m["id"], m["name"], ",".join(m["issued_books"]), m["fine"]] for m in members]
            )
        else:
            error("No members found")
        pause()

    elif choice == "5":
        if issue_book(input("Book ID: "), input("Member ID: ")):
            success("Book issued successfully (Due in 7 days)")
        else:
            error("Issue failed (check ID or quantity)")
        pause()

    elif choice == "6":
        fine = return_book(input("Book ID: "), input("Member ID: "))
        if fine is None:
            error("Invalid return request")
        elif fine == 0:
            success("Book returned on time. No fine.")
        else:
            print("\n⚠ Late return")
            print("Fine to be paid: ₹", fine)
        pause()

    elif choice == "7":
        issued = issued_books_report()
        if issued:
            print_table(
                ["Book ID", "Member ID", "Due Date"],
                [[i["book_id"], i["member_id"], i["due_date"]] for i in issued]
            )
        else:
            error("No books currently issued")
        pause()

    elif choice == "8":
        members = members_report()
        if members:
            print_table(
                ["ID", "Name", "Issued Books", "Fine"],
                [[m["id"], m["name"], ",".join(m["issued_books"]), m["fine"]] for m in members]
            )
        else:
            error("No member data")
        pause()

    elif choice == "9":
        fine = check_fine(input("Book ID: "), input("Member ID: "))
        if fine is None:
            error("No such issued book found")
        elif fine == 0:
            success("No fine. Book is returned on time or not yet due.")
        else:
            print("\n💰 Fine to be paid: ₹", fine)
        pause()

    elif choice == "10":
        clear()
        header("Thank You for Using the Library System")
        print("Developed using Python | Modular Console Application".center(70))
        print("=" * 70)
        break

    else:
        error("Invalid choice")
        pause()
