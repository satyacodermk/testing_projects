"""main.py - Entry point: menu loop and routing.

Run with:  python main.py
"""

import expense_manager


def show_menu():
    print("\n==============================")
    print("  PERSONAL EXPENSE TRACKER")
    print("==============================")
    print("Welcome! Track your spending easily.\n")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Expense Summary")
    print("4. Exit Application\n")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            expense_manager.add_expense()
        elif choice == "2":
            expense_manager.view_expenses()
        elif choice == "3":
            expense_manager.view_summary()
        elif choice == "4":
            print("\nGoodbye! Your data has been saved.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGoodbye! Your data has been saved.")
