# report_generator.py
# Generates a simple academic report.
# Data comes from three TXT files:
# - students.txt (student_id|student_name)
# - courses.txt (course_code|course_name)
# - grades.txt (student_id|course_code|grade_letter)

from __future__ import annotations

import os
from typing import List, Dict


DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.txt")
COURSES_FILE = os.path.join(DATA_DIR, "courses.txt")
GRADES_FILE = os.path.join(DATA_DIR, "grades.txt")


def _read_lines(file_path: str) -> List[str]:
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def _read_students() -> Dict[str, str]:
    students: Dict[str, str] = {}
    for line in _read_lines(STUDENTS_FILE):
        parts = line.split("|", 1)
        if len(parts) == 2:
            students[parts[0]] = parts[1]
    return students


def _read_courses() -> Dict[str, str]:
    courses: Dict[str, str] = {}
    for line in _read_lines(COURSES_FILE):
        parts = line.split("|", 1)
        if len(parts) == 2:
            courses[parts[0]] = parts[1]
    return courses


def _read_grades() -> List[Dict[str, str]]:
    grades: List[Dict[str, str]] = []
    for line in _read_lines(GRADES_FILE):
        parts = line.split("|")
        if len(parts) == 3:
            grades.append({"student_id": parts[0], "course_code": parts[1], "grade": parts[2]})
    return grades


def generate_report() -> None:
    """Generate and print a report to the console."""

    students = _read_students()
    courses = _read_courses()
    grades = _read_grades()

    if not grades:
        print("No grades available. Add students, courses, and grades first.")
        return

    # Build a student -> course list mapping
    report_rows: Dict[str, List[Dict[str, str]]] = {}
    for g in grades:
        sid = g["student_id"]
        report_rows.setdefault(sid, []).append(g)

    print("\n===== Academic Report =====")

    for sid, student_grades in report_rows.items():
        student_name = students.get(sid, "Unknown Student")
        print(f"\nStudent: {student_name} ({sid})")

        # Print each course grade
        for g in student_grades:
            course_code = g["course_code"]
            course_name = courses.get(course_code, "Unknown Course")
            grade = g["grade"]
            print(f"  - {course_code}: {course_name} => Grade {grade}")


# ---- Learning note ----
# report_generator.py demonstrates:
# - reading multiple TXT files
# - combining data from separate modules/files
# - generating a readable report on the terminal

