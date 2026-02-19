# task_manager_app/file_handler.py
import json
from pathlib import Path
from typing import List, Dict
from .task import Task


DATA_FILENAME = "tasks.json"


def _get_data_file_path() -> Path:
    """
    Returns the Path to the data/tasks.json file.
    This file is located at the project root /data/tasks.json (one folder up from package).
    """
    package_dir = Path(__file__).resolve().parent
    project_root = package_dir.parent
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / DATA_FILENAME


def load_tasks() -> List[Task]:
    """Load tasks from the JSON file. Return an empty list if file is missing or corrupted."""
    path = _get_data_file_path()
    try:
        if not path.exists():
            # create empty file
            path.write_text("[]", encoding="utf-8")
            return []
        content = path.read_text(encoding="utf-8").strip()
        if not content:
            return []
        data = json.loads(content)
        if not isinstance(data, list):
            # if file content not list, reset to empty list
            return []
        tasks = [Task.from_dict(item) for item in data]
        return tasks
    except (json.JSONDecodeError, OSError) as e:
        # On any error, return empty list (do not crash).
        print(f"[Warning] Failed to read tasks file: {e}")
        return []


def save_tasks(tasks: List[Task]) -> bool:
    """Save list of Task objects to file. Returns True on success."""
    path = _get_data_file_path()
    try:
        data = [t.to_dict() for t in tasks]
        path.write_text(json.dumps(data, indent=4, ensure_ascii=False), encoding="utf-8")
        return True
    except OSError as e:
        print(f"[Error] Failed to write tasks file: {e}")
        return False
