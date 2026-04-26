# library/transactions.py
from datetime import datetime
from . import books
from . import fine

issued_records = {}

def generate_transaction_id(book_id, student_id):
    return f"{book_id}_{student_id}"

def issue_book(student_name, student_id, book_id, issue_date_str, days_issued):
    book = books.get_book(book_id)
    if not book:
        return False, "Book ID not found."
    
    if book['available_copies'] <= 0:
        return False, "No copies available currently."
        
    try:
        issue_date = datetime.strptime(issue_date_str, "%d-%m-%Y")
    except ValueError:
        return False, "Invalid date format. Use DD-MM-YYYY."
        
    try:
        days_issued = int(days_issued)
    except ValueError:
        return False, "Number of days must be an integer."
        
    trans_id = generate_transaction_id(book_id, student_id)
    if trans_id in issued_records:
        return False, "This student has already issued this book."
        
    books.update_available_copies(book_id, -1)
    
    issued_records[trans_id] = {
        'student_name': student_name,
        'student_id': student_id,
        'book_id': book_id,
        'issue_date': issue_date,
        'allotted_days': days_issued
    }
    
    return True, "Book issued successfully."

def return_book(book_id, student_id):
    trans_id = generate_transaction_id(book_id, student_id)
    if trans_id not in issued_records:
        return False, "No issue record found for this student and book.", 0, 0
        
    record = issued_records[trans_id]
    issue_date = record['issue_date']
    allotted_days = record['allotted_days']
    
    # Calculate days using current date
    return_date = datetime.now()
    days_kept = (return_date - issue_date).days
    
    # Allow same day return to count as 0 days kept
    if days_kept < 0:
        days_kept = 0
        
    days_late = days_kept - allotted_days
    fine_amount = 0
    if days_late > 0:
        fine_amount = fine.calculate_fine(days_late)
    else:
        days_late = 0
        
    books.update_available_copies(book_id, 1)
    del issued_records[trans_id]
    
    return True, "Book returned successfully.", days_late, fine_amount

def get_all_issued_books():
    return issued_records
