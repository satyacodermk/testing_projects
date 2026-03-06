
import re
from modules.expense import Expense
from modules.file_operations import save_expense, load_expenses
from modules.category_summarizer import summarize_by_category

DATE_PATTERN = r"^\d{4}-\d{2}-\d{2}$"


def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summarize by Category")
    print("4. Exit")


def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    category = input("Enter category: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    if not re.match(DATE_PATTERN, date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    expense = Expense(amount, category, date)
    save_expense(expense)
    print("Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nAmount     Category        Date")
    print("--------------------------------")
    for exp in expenses:
        print(exp)


def show_summary():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to summarize.")
        return

    summary = summarize_by_category(expenses)

    print("\n--- Expense Summary by Category ---")
    print("Category        Total Amount")
    print("---------------------------------")
    for category, total in summary.items():
        print(f"{category:<15} {total:.2f}")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()