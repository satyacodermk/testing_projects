import os
from modules.expense import Expense

DATA_FILE = os.path.join('data', 'expenses.txt')


def save_expense(expense: Expense):
    """Append a single expense to the file."""
    try:
        with open(DATA_FILE, 'a') as file:
            file.write(expense.to_file_string())
    except IOError:
        print("Error: Unable to save expense.")


def load_expenses():
    """Load all expenses from file."""
    expenses = []
    try:
        with open(DATA_FILE, 'r') as file:
            for line in file:
                try:
                    expenses.append(Expense.from_file_string(line))
                except ValueError:
                    print("Warning: Skipping corrupted record.")
    except FileNotFoundError:
        return []

    return expenses