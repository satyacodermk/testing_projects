# task_manager_app/input_validator.py
import re
from typing import Tuple

# Allowed priorities
PRIORITIES = ("High", "Medium", "Low")

# Regex for name: at least 1 non-space character; we also disallow newline characters.
NAME_RE = re.compile(r"^\s*(?=\S).{1,200}$", re.UNICODE)
# Description: up to 1000 chars, allow anything but exclude control chars except common punctuation/newlines
DESCRIPTION_RE = re.compile(r"^[\s\S]{0,1000}$", re.UNICODE)
# Priority match (case-insensitive)
PRIORITY_RE = re.compile(r"^(high|medium|low)$", re.IGNORECASE)


def validate_name(name: str) -> Tuple[bool, str]:
    """Validate task name. Returns (is_valid, normalized_value_or_error)."""
    if name is None:
        return False, "Name is required."
    name = name.strip()
    if not NAME_RE.match(name):
        return False, "Name must be non-empty and under 200 characters."
    return True, name


def validate_description(description: str) -> Tuple[bool, str]:
    """Validate description (optional but limit length)."""
    if description is None:
        return True, ""
    description = description.strip()
    if not DESCRIPTION_RE.match(description):
        return False, "Description too long (max 1000 characters)."
    return True, description


def validate_priority(priority: str) -> Tuple[bool, str]:
    """Validate priority. Accepts High/Medium/Low (case-insensitive)."""
    if priority is None:
        return False, f"Priority is required. Choose one of: {', '.join(PRIORITIES)}."
    match = PRIORITY_RE.match(priority.strip())
    if not match:
        return False, f"Invalid priority. Choose one of: {', '.join(PRIORITIES)}."
    return True, match.group(1).title()
