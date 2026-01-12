
# task_manager_app/task.py
from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class Task:
    name: str
    description: str
    priority: str

    def to_dict(self) -> Dict:
        """Convert Task to a JSON-serializable dict."""
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict) -> "Task":
        """Construct a Task from a dict (validation is expected earlier)."""
        return Task(
            name=data.get("name", "").strip(),
            description=data.get("description", "").strip(),
            priority=data.get("priority", "").strip().title(),
        )
