# validation.py
# Contains helper functions for validating student input.

import re


def validate_student_id(student_id: str) -> str:
    """Validate and normalize a student id.

    For a university assignment, we keep validation beginner-friendly.
    Rule used here:
    - Must start with 'S' (uppercase)
    - Followed by exactly 6 digits
    Example: S123456

    Returns:
        The normalized student id (trimmed).

    Raises:
        ValueError if invalid.
    """

    normalized = student_id.strip().upper()
    pattern = r"^S\d{6}$"

    if not re.match(pattern, normalized):
        raise ValueError("Student ID must look like S123456 (S + 6 digits).")

    return normalized


def validate_student_name(name: str) -> str:
    """Validate student name.

    Rule:
    - At least 2 characters
    """

    normalized = name.strip()
    if len(normalized) < 2:
        raise ValueError("Student name must be at least 2 characters.")
    return normalized

