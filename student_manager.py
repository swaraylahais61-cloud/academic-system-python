# student_manager.py
# Handles operations related to students.
# Demonstrates reading/writing TXT files and using validation from validation.py.

from __future__ import annotations

from .validation import (
    validate_student_id,
    validate_student_name,
)


import os
from typing import List, Dict

# Location of the data files (TXT)
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.txt")


def _ensure_data_file() -> None:
    # Creates the TXT file if it does not exist yet.
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
            # Format: student_id|student_name
            pass


def _read_students() -> List[Dict[str, str]]:
    _ensure_data_file()
    students: List[Dict[str, str]] = []
    with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|", 1)
            if len(parts) != 2:
                continue
            students.append({"id": parts[0], "name": parts[1]})
    return students


def _write_students(students: List[Dict[str, str]]) -> None:
    _ensure_data_file()
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s['id']}|{s['name']}\n")


def add_student() -> None:
    """Prompt the user and add a student to students.txt."""

    try:
        raw_id = input("Enter Student ID (example: S123456): ")
        student_id = validate_student_id(raw_id)

        raw_name = input("Enter Student Name: ")
        student_name = validate_student_name(raw_name)

        students = _read_students()

        # Prevent duplicate IDs
        for s in students:
            if s["id"] == student_id:
                print("This Student ID already exists. No changes made.")
                return

        students.append({"id": student_id, "name": student_name})
        _write_students(students)
        print("Student added successfully.")

    except ValueError as e:
        print(f"Invalid input: {e}")


def view_students() -> None:
    """Display all students from students.txt."""

    students = _read_students()
    if not students:
        print("No students found.")
        return

    print("\n--- Students ---")
    for s in students:
        print(f"ID: {s['id']}\tName: {s['name']}")


# ---- Learning note ----
# student_manager.py demonstrates:
# 1) importing validation functions from validation.py
# 2) file I/O for persistence using a simple '|' separated format

