# grade_manager.py
# Handles operations related to assigning and viewing grades.
# Data is stored in grades.txt in the data folder.
# Format used: student_id|course_code|grade_letter

from __future__ import annotations

import os

from typing import List, Dict


DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
GRADES_FILE = os.path.join(DATA_DIR, "grades.txt")


def _ensure_data_file() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(GRADES_FILE):
        with open(GRADES_FILE, "w", encoding="utf-8") as f:
            pass


def _read_grades() -> List[Dict[str, str]]:
    _ensure_data_file()
    grades: List[Dict[str, str]] = []

    with open(GRADES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) != 3:
                continue
            grades.append({"student_id": parts[0], "course_code": parts[1], "grade": parts[2]})

    return grades


def _write_grades(grades: List[Dict[str, str]]) -> None:
    _ensure_data_file()
    with open(GRADES_FILE, "w", encoding="utf-8") as f:
        for g in grades:
            f.write(f"{g['student_id']}|{g['course_code']}|{g['grade']}\n")


def _normalize_grade(grade: str) -> str:
    g = grade.strip().upper()
    allowed = {"A", "B", "C", "D", "E", "F"}
    if g not in allowed:
        raise ValueError("Grade must be one of: A, B, C, D, E, F")
    return g


def assign_grade() -> None:
    """Prompt user to assign/update a grade in grades.txt."""

    try:
        student_id = input("Enter Student ID (example: S123456): ").strip().upper()
        course_code = input("Enter Course Code (example: CS101): ").strip().upper()
        grade_raw = input("Enter Grade (A-F): ")
        grade = _normalize_grade(grade_raw)

        grades = _read_grades()

        # Update if same student+course already exists
        for g in grades:
            if g["student_id"] == student_id and g["course_code"] == course_code:
                g["grade"] = grade
                _write_grades(grades)
                print("Grade updated successfully.")
                return

        # Otherwise add new record
        grades.append({"student_id": student_id, "course_code": course_code, "grade": grade})
        _write_grades(grades)
        print("Grade assigned successfully.")

    except ValueError as e:
        print(f"Invalid input: {e}")


def view_grades() -> None:
    """Display grades from grades.txt."""

    grades = _read_grades()
    if not grades:
        print("No grades found.")
        return

    print("\n--- Grades ---")
    for g in grades:
        print(f"Student: {g['student_id']}\tCourse: {g['course_code']}\tGrade: {g['grade']}")


# ---- Learning note ----
# grade_manager.py demonstrates:
# - handling records in a TXT file
# - a simple update-or-insert (upsert-like) behavior for beginner-friendly code
# - grade normalization and input validation

