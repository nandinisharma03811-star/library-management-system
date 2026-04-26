# library/menu.py
from . import books
from . import transactions

def display_header(text):
    print("\n" + "=" * 50)
    print(f"{text.center(50)}")
    print("=" * 50)

def add_book_menu():
    display_header("ADD NEW BOOK")
    book_id = input("Enter Book ID: ").strip()
    if not book_id:
        print("Book ID cannot be empty.")
        return
        
    if books.get_book(book_id):
        print("A book with this ID already exists.")
        return
        
    title = input("Enter Book Title: ").strip()
    author = input("Enter Book Author: ").strip()
    
    try:
        total_copies = int(input("Enter Total Copies: ").strip())
        if total_copies <= 0:
            print("Total copies must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Copies must be a number.")
        return
        
    books.add_book(book_id, title, author, total_copies)
    print("-" * 50)
    print(f"Success! Book '{title}' added to the library.")
    print("-" * 50)

def view_all_books_menu():
    display_header("ALL BOOKS")
    all_books = books.get_all_books()
    if not all_books:
        print("No books available in the library.")
        return
        
    print(f"{'ID'.ljust(10)} | {'Title'.ljust(20)} | {'Author'.ljust(15)} | {'Total'.ljust(6)} | {'Avail'.ljust(6)}")
    print("-" * 65)
    for b_id, details in all_books.items():
        title = details['title'][:19]
        author = details['author'][:14]
        total = str(details['total_copies'])
        avail = str(details['available_copies'])
        print(f"{b_id.ljust(10)} | {title.ljust(20)} | {author.ljust(15)} | {total.ljust(6)} | {avail.ljust(6)}")
    print("-" * 65)

def issue_book_menu():
    display_header("ISSUE BOOK")
    student_name = input("Enter Student Name: ").strip()
    student_id = input("Enter Student ID: ").strip()
    book_id = input("Enter Book ID: ").strip()
    issue_date = input("Enter Issue Date (DD-MM-YYYY): ").strip()
    days_issued = input("Enter Number of Days Issued For: ").strip()
    
    success, message = transactions.issue_book(student_name, student_id, book_id, issue_date, days_issued)
    print("-" * 50)
    if success:
        print(f"Success: {message}")
    else:
        print(f"Error: {message}")
    print("-" * 50)

def return_book_menu():
    display_header("RETURN BOOK")
    book_id = input("Enter Book ID: ").strip()
    student_id = input("Enter Student ID: ").strip()
    
    success, message, days_late, fine_amount = transactions.return_book(book_id, student_id)
    print("-" * 50)
    if success:
        print(message)
        if days_late > 0:
            print(f"Return was late by {days_late} days.")
            print(f"Total Fine: {fine_amount} Rs")
        else:
            print("Book returned on time. No fine.")
    else:
        print(f"Error: {message}")
    print("-" * 50)

def view_issued_books_menu():
    display_header("ISSUED BOOKS")
    issued = transactions.get_all_issued_books()
    if not issued:
        print("No books are currently issued.")
        return
        
    print(f"{'Student ID'.ljust(12)} | {'Book ID'.ljust(10)} | {'Issue Date'.ljust(12)} | {'Allotted Days'}")
    print("-" * 60)
    for record in issued.values():
        sid = record['student_id'][:11]
        bid = record['book_id'][:9]
        idate = record['issue_date'].strftime("%d-%m-%Y")
        days = str(record['allotted_days'])
        print(f"{sid.ljust(12)} | {bid.ljust(10)} | {idate.ljust(12)} | {days}")
    print("-" * 60)

def run():
    while True:
        display_header("LIBRARY MANAGEMENT SYSTEM")
        print("1) Add Book")
        print("2) View All Books")
        print("3) Issue Book")
        print("4) Return Book")
        print("5) View Issued Books")
        print("6) Exit")
        print("-" * 50)
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            add_book_menu()
        elif choice == '2':
            view_all_books_menu()
        elif choice == '3':
            issue_book_menu()
        elif choice == '4':
            return_book_menu()
        elif choice == '5':
            view_issued_books_menu()
        elif choice == '6':
            print("\nExiting Library Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")
