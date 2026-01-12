# Task Manager Application

Simple console-based Task Manager that lets you add, view, update and delete tasks. Tasks are saved persistently in a JSON file.

## Folder structure
/task_manager_app
┣ /data
┃ ┗ tasks.json
┣ /task_manager_app
┃ ┣ init.py
┃ ┣ task.py
┃ ┣ file_handler.py
┃ ┣ input_validator.py
┣ main.py
┗ README.md


## How to run

1. Make sure you have Python 3.8+ installed.
2. From project root (where `main.py` is located) run:
python main.py

3. Follow on-screen menu instructions.

## Features

- Add task (name, description, priority)
- View tasks (neatly formatted)
- Update task (leave input empty to keep current value)
- Delete task (with confirmation)
- Data is saved in `data/tasks.json`

## Validation

- Name: required, non-empty
- Description: optional, limited length
- Priority: must be one of `High`, `Medium`, `Low` (case-insensitive input accepted)

## Notes

- `data/tasks.json` will be created automatically if it doesn't exist.
- The code is modular: business objects (`Task`), file handling (`file_handler`) and validation (`input_validator`) are separated for maintainability.
