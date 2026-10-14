"""expense_manager.py - Input, validation, display and calculations."""

import math
from datetime import datetime

import storage

DATE_FORMAT = storage.DATE_FORMAT
DELIMITER = storage.DELIMITER

# Column widths for the expense table
W_NO, W_DATE, W_CAT, W_DESC, W_AMT = 5, 12, 12, 21, 10
TABLE_WIDTH = W_NO + W_DATE + W_CAT + W_DESC + W_AMT


class Expense:
    """Optional stretch goal: a simple expense object."""

    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def display(self, number):
        """Return one formatted table row."""
        desc = self.description
        if len(desc) > W_DESC - 2:
            desc = desc[:W_DESC - 5] + "..."
        return (f"{number:<{W_NO}}{self.date:<{W_DATE}}"
                f"{self.category:<{W_CAT}}{desc:<{W_DESC}}"
                f"{self.amount:>{W_AMT}.2f}")


# ---------- Input helpers (each loops until the value is valid) ----------

def get_amount():
    while True:
        text = input("Enter amount: ").strip()
        try:
            amount = float(text)
        except ValueError:
            print("Invalid amount. Please enter a number (e.g. 250.50).")
            continue
        if not math.isfinite(amount) or amount <= 0:
            print("Amount must be a positive number.")
            continue
        return round(amount, 2)


def get_text(prompt, field_name):
    """Ask for non-empty text that does not contain the file delimiter."""
    while True:
        text = input(prompt).strip()
        if not text:
            print(f"{field_name} cannot be empty.")
        elif DELIMITER in text:
            print(f"{field_name} cannot contain the '{DELIMITER}' character.")
        else:
            return text


def get_category():
    return get_text("Enter category (e.g. Food, Travel, Shopping, Bills): ",
                    "Category").title()


def get_description():
    return get_text("Enter description: ", "Description")


def get_date():
    today = datetime.now().strftime(DATE_FORMAT)
    while True:
        text = input(f"Enter date (YYYY-MM-DD) [Enter = {today}]: ").strip()
        if not text:
            return today
        try:
            datetime.strptime(text, DATE_FORMAT)
            return text
        except ValueError:
            print("Invalid date. Use the YYYY-MM-DD format with a real date "
                  "(e.g. 2025-01-15).")


# ---------- Features ----------

def add_expense():
    print("\n--- Add New Expense ---")
    expense = {
        "amount": get_amount(),
        "category": get_category(),
        "description": get_description(),
        "date": get_date(),
    }
    try:
        storage.save_expense(expense)
    except OSError as error:
        print(f"Error: could not save the expense: {error}")
        return
    print("Expense added successfully!")


def view_expenses():
    expenses = storage.load_expenses()
    print()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'No.':<{W_NO}}{'Date':<{W_DATE}}{'Category':<{W_CAT}}"
          f"{'Description':<{W_DESC}}{'Amount':>{W_AMT}}")
    print("-" * TABLE_WIDTH)
    for number, item in enumerate(expenses, start=1):
        row = Expense(item["date"], item["category"],
                      item["description"], item["amount"])
        print(row.display(number))
    print("-" * TABLE_WIDTH)
    print(f"Total expenses recorded: {len(expenses)}")


def calculate_summary(expenses):
    """Return (grand_total, {category: total}) using an accumulator."""
    grand_total = 0.0
    by_category = {}
    for item in expenses:
        grand_total += item["amount"]
        category = item["category"]
        by_category[category] = by_category.get(category, 0.0) + item["amount"]
    return grand_total, by_category


def view_summary():
    expenses = storage.load_expenses()
    print()
    if not expenses:
        print("No expense data available.")
        return

    grand_total, by_category = calculate_summary(expenses)
    print("===== EXPENSE SUMMARY =====")
    print(f"Total Spent: {grand_total:.2f}")
    print(f"Number of Expenses: {len(expenses)}")
    print("\nSpending by Category:")
    for category, total in by_category.items():
        print(f"{category:<10} : {total:.2f}")
