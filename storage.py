"""storage.py - Save and load expense records (pipe-delimited text file)."""

import os
import math
from datetime import datetime

# Constants (easy to change later). Path is relative to this file, so the
# program works no matter which folder it is launched from.
DATA_FILE = "expenses.txt"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, DATA_FILE)
DELIMITER = "|"
DATE_FORMAT = "%Y-%m-%d"


def parse_line(line):
    """Convert one 'date|category|description|amount' line into a dict.

    Raises ValueError if the line is malformed.
    """
    parts = line.strip().split(DELIMITER)
    if len(parts) != 4:
        raise ValueError("expected 4 fields separated by '|'")

    date_text, category, description, amount_text = (p.strip() for p in parts)

    datetime.strptime(date_text, DATE_FORMAT)  # raises ValueError if invalid
    if not category or not description:
        raise ValueError("category and description cannot be empty")

    amount = float(amount_text)  # raises ValueError if not a number
    if not math.isfinite(amount) or amount <= 0:
        raise ValueError("amount must be a positive number")

    return {
        "date": date_text,
        "category": category,
        "description": description,
        "amount": amount,
    }


def format_record(expense):
    """Convert an expense dict into one line of text (without newline)."""
    return DELIMITER.join([
        expense["date"],
        expense["category"],
        expense["description"],
        f"{expense['amount']:.2f}",
    ])


def load_expenses():
    """Read all valid expenses from the file.

    - Missing file  -> empty list (first run, no crash).
    - Corrupted line -> skipped with a warning.
    """
    expenses = []
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue  # ignore blank lines silently
                try:
                    expenses.append(parse_line(line))
                except ValueError as error:
                    print(f"Warning: skipped bad line {line_number} "
                          f"in {DATA_FILE} ({error}).")
    except FileNotFoundError:
        return []
    except OSError as error:
        print(f"Error: could not read {DATA_FILE}: {error}")
        return []
    return expenses


def save_expense(expense):
    """Append one expense as a new line. Raises OSError on file problems."""
    with open(DATA_PATH, "a", encoding="utf-8") as file:
        file.write(format_record(expense) + "\n")
