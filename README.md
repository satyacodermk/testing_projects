# Personal Expense Tracker

A beginner-friendly terminal app (Python standard library only) to record,
view and summarize daily expenses. Data is saved in `expenses.txt`.

## Requirements
Python 3.6+ (no external packages).

## Run
```
cd personal_expense_tracker
python main.py
```

## Project structure
```
personal_expense_tracker/
 ┣ screens/              Screenshots of each terminal screen
 ┣ main.py               Entry point: menu loop and routing
 ┣ expense_manager.py    Input, validation, display, calculations (+ Expense class)
 ┣ storage.py            Save and load expense records
 ┣ expenses.txt          Local data file (created automatically if missing)
 ┗ README.md
```

## Usage
1. **Add New Expense** - amount (positive number), category, description
   (not empty), date (`YYYY-MM-DD`, press Enter for today).
2. **View All Expenses** - aligned table + record count.
3. **View Expense Summary** - grand total, count, totals per category.
4. **Exit Application** - data is already saved after every add.

## Data format (`expenses.txt`)
One record per line, pipe-delimited:
```
2025-01-15|Food|Lunch at cafe|250.50
```

## Edge cases handled
- Missing data file -> starts empty, no crash.
- Invalid menu choice / amount / date / empty description -> message and retry.
- `|` inside category or description -> rejected (it is the file delimiter).
- Corrupted line in `expenses.txt` -> skipped with a warning.
- Ctrl+C / Ctrl+D -> exits cleanly.

## Sample output
```
No.  Date        Category    Description              Amount
------------------------------------------------------------
1    2025-01-15  Food        Lunch at cafe            250.50
2    2025-01-16  Travel      Metro card recharge      300.00
3    2025-01-17  Bills       Electricity bill        1200.00
------------------------------------------------------------
Total expenses recorded: 3
```
