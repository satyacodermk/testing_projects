# main.py
import sys
from typing import List, Optional

from task_manager_app.task import Task
from task_manager_app import file_handler, input_validator


def clear_console():
    print("\033[2J\033[H", end="")


def pause():
    input("\nPress Enter to continue...")


def print_header():
    print("=" * 40)
    print("       Task Manager Application")
    print("=" * 40)


def list_tasks(tasks: List[Task]) -> None:
    print_header()
    print("Your Current Tasks:\n")
    if not tasks:
        print("No tasks found.")
        return
    for idx, t in enumerate(tasks, start=1):
        print(f"{idx}. {t.name} [{t.priority}]")
        print(f"   {t.description}")
    print()


def prompt_for_task(existing: Optional[Task] = None) -> Optional[Task]:
    """
    Prompt user for task details.
    If existing provided, user can press Enter to keep current values.
    Returns Task or None if validation fails/cancelled.
    """
    try:
        # Name
        while True:
            prompt_name = "Task Name"
            if existing:
                prompt_name += f" (Enter to keep: '{existing.name}')"
            prompt_name += ": "
            name_input = input(prompt_name)
            if existing and name_input.strip() == "":
                name = existing.name
                break
            valid, result = input_validator.validate_name(name_input)
            if valid:
                name = result
                break
            print(f"[Invalid] {result}")

        # Description
        while True:
            prompt_desc = "Description"
            if existing:
                prompt_desc += f" (Enter to keep current)"
            prompt_desc += ": "
            desc_input = input(prompt_desc)
            if existing and desc_input.strip() == "":
                description = existing.description
                break
            valid, result = input_validator.validate_description(desc_input)
            if valid:
                description = result
                break
            print(f"[Invalid] {result}")

        # Priority
        while True:
            prompt_pr = "Priority (High / Medium / Low)"
            if existing:
                prompt_pr += f" (Enter to keep: '{existing.priority}')"
            prompt_pr += ": "
            pr_input = input(prompt_pr)
            if existing and pr_input.strip() == "":
                priority = existing.priority
                break
            valid, result = input_validator.validate_priority(pr_input)
            if valid:
                priority = result
                break
            print(f"[Invalid] {result}")

        return Task(name=name, description=description, priority=priority)
    except (KeyboardInterrupt, EOFError):
        print("\n[Cancelled]")
        return None


def add_task():
    clear_console()
    print_header()
    print("Add New Task\n")
    new_task = prompt_for_task()
    if new_task is None:
        pause()
        return
    tasks = file_handler.load_tasks()
    tasks.append(new_task)
    if file_handler.save_tasks(tasks):
        print("\nTask added successfully!")
    else:
        print("\n[Error] Could not save task.")
    pause()


def view_tasks():
    clear_console()
    print_header()
    tasks = file_handler.load_tasks()
    list_tasks(tasks)
    pause()


def update_task():
    clear_console()
    print_header()
    tasks = file_handler.load_tasks()
    if not tasks:
        print("No tasks to update.")
        pause()
        return
    list_tasks(tasks)
    try:
        idx_input = input("Enter the task number to update (or 'c' to cancel): ").strip()
        if idx_input.lower() == "c":
            print("Update cancelled.")
            pause()
            return
        idx = int(idx_input) - 1
        if idx < 0 or idx >= len(tasks):
            print("[Error] Invalid task number.")
            pause()
            return
        selected = tasks[idx]
        print(f"\nUpdating Task #{idx+1}: {selected.name}\nLeave field empty to keep current value.")
        updated = prompt_for_task(existing=selected)
        if updated is None:
            print("Update cancelled.")
            pause()
            return
        tasks[idx] = updated
        if file_handler.save_tasks(tasks):
            print("Task updated successfully!")
        else:
            print("[Error] Could not save updated task.")
    except ValueError:
        print("[Error] Please enter a valid number.")
    except (KeyboardInterrupt, EOFError):
        print("\n[Cancelled]")
    pause()


def delete_task():
    clear_console()
    print_header()
    tasks = file_handler.load_tasks()
    if not tasks:
        print("No tasks to delete.")
        pause()
        return
    list_tasks(tasks)
    try:
        idx_input = input("Enter the task number to delete (or 'c' to cancel): ").strip()
        if idx_input.lower() == "c":
            print("Deletion cancelled.")
            pause()
            return
        idx = int(idx_input) - 1
        if idx < 0 or idx >= len(tasks):
            print("[Error] Invalid task number.")
            pause()
            return
        selected = tasks[idx]
        confirm = input(f"Are you sure you want to delete '{selected.name}'? (y/n): ").strip().lower()
        if confirm != "y":
            print("Deletion cancelled.")
            pause()
            return
        tasks.pop(idx)
        if file_handler.save_tasks(tasks):
            print("Task deleted successfully!")
        else:
            print("[Error] Could not save tasks after deletion.")
    except ValueError:
        print("[Error] Please enter a valid number.")
    except (KeyboardInterrupt, EOFError):
        print("\n[Cancelled]")
    pause()


def main_menu():
    while True:
        clear_console()
        print_header()
        print("Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nExiting Task Manager. Goodbye!")
            sys.exit(0)
        else:
            print("\n[Error] Invalid choice. Please select 1-5.")
            pause()


if __name__ == "__main__":
    try:
        main_menu()
    except (KeyboardInterrupt, EOFError):
        print("\n\nExiting Task Manager. Goodbye!")
