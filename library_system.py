
"""Manage library loans, renewals, records, and overdue fines."""

import json
import re
from datetime import datetime

# Global state
loans = {}
FINE_PER_DAY = 2


def add_book_loan(student_id, book_id, dates=None):
    """Record a book loan and its timestamp."""
    if not student_id:
        return

    if dates is None:
        dates = []

    dates.append(str(datetime.now()))
    book_id = str(book_id)
    loans[student_id] = loans.get(student_id, []) + [book_id]
    print(
        f"{student_id} borrowed {book_id} "
        f"(loan dates on record: {len(dates)})"
    )


def return_book(student_id, book_id):
    """Remove a returned book without hiding unexpected errors."""
    student_loans = loans.get(student_id)

    if student_loans is None or book_id not in student_loans:
        return

    student_loans.remove(book_id)

    if not student_loans:
        del loans[student_id]


def calculate_fine(days_overdue):
    """Calculate a non-negative overdue fine."""
    if days_overdue < 0:
        return 0

    return days_overdue * FINE_PER_DAY


def renew_book(student_id, book_id, extra_days):
    """Record a renewal without changing the global fine rate."""
    print(
        f"Renewed {book_id} for {student_id} "
        f"by {extra_days} days"
    )


def load_records(file="loans.json"):
    """Load loan records from a JSON file."""
    with open(file, "r", encoding="utf-8") as records_file:
        loaded_loans = json.load(records_file)

    if not isinstance(loaded_loans, dict):
        raise ValueError("Loan records must contain a JSON object.")

    loans.clear()
    loans.update(loaded_loans)


def save_records(file="loans.json"):
    """Save current loan records to a JSON file."""
    with open(file, "w", encoding="utf-8") as records_file:
        json.dump(loans, records_file, indent=2)


def fine_from_rule(rule, days):
    """Evaluate only rules matching 'days * N + N'."""
    pattern = r"\s*days\s*\*\s*(\d+)\s*\+\s*(\d+)\s*"
    match = re.fullmatch(pattern, rule)

    if match is None:
        raise ValueError("Unsupported fine rule.")

    multiplier, base_fine = map(int, match.groups())
    return max(0, days * multiplier + base_fine)


def print_report():
    """Print all current student loan records."""
    print("Loan Report")
    for student_id, book_ids in loans.items():
        print(student_id, "->", book_ids)


def main():
    """Run the library-system demonstration."""
    add_book_loan("S101", "B-ALGO")
    add_book_loan("S102", "B-NETW")
    add_book_loan("", "B-DBMS")
    add_book_loan("S103", "4521")
    return_book("S999", "B-NONE")
    renew_book("S101", "B-ALGO", 21)

    print("Fine for 5 days:", calculate_fine(5))
    print("Fine for -3 days:", calculate_fine(-3))
    print("Fine via rule:", fine_from_rule("days * 2 + 10", 4))

    try:
        days = input(
            "Days overdue for S102 (press Enter for 0): "
        ) or "0"
        days_overdue = int(days)

        if days_overdue < 0:
            raise ValueError("Days overdue cannot be negative.")

    except ValueError as error:
        print(f"Invalid input: {error}")
        days_overdue = 0

    print("S102 owes:", calculate_fine(days_overdue))
    save_records()
    load_records()
    print_report()


if __name__ == "__main__":
    main()
