# course_manager.py
# Handles operations related to courses.
# Data is stored in courses.txt in the data folder.

from __future__ import annotations

import os
from typing import List, Dict


DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
COURSES_FILE = os.path.join(DATA_DIR, "courses.txt")


def _ensure_data_file() -> None:
    # Creates the TXT file if it does not exist yet.
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(COURSES_FILE):
        with open(COURSES_FILE, "w", encoding="utf-8") as f:
            # Format: course_code|course_name
            pass


def _read_courses() -> List[Dict[str, str]]:
    _ensure_data_file()
    courses: List[Dict[str, str]] = []

    with open(COURSES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|", 1)
            if len(parts) != 2:
                continue
            courses.append({"code": parts[0], "name": parts[1]})

    return courses


def _write_courses(courses: List[Dict[str, str]]) -> None:
    _ensure_data_file()
    with open(COURSES_FILE, "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c['code']}|{c['name']}\n")


def add_course() -> None:
    """Prompt the user and add a course to courses.txt."""

    try:
        course_code = input("Enter Course Code (example: CS101): ").strip().upper()
        if not course_code:
            print("Course code cannot be empty.")
            return

        course_name = input("Enter Course Name: ").strip()
        if len(course_name) < 2:
            print("Course name must be at least 2 characters.")
            return

        courses = _read_courses()

        # Prevent duplicate course codes
        for c in courses:
            if c["code"] == course_code:
                print("This Course Code already exists. No changes made.")
                return

        courses.append({"code": course_code, "name": course_name})
        _write_courses(courses)
        print("Course added successfully.")

    except Exception as e:
        print(f"Error adding course: {e}")


def view_courses() -> None:
    """Display all courses from courses.txt."""

    courses = _read_courses()

    if not courses:
        print("No courses found.")
        return

    print("\n--- Courses ---")
    for c in courses:
        print(f"Code: {c['code']}\tName: {c['name']}")


# ---- Learning note ----
# course_manager.py demonstrates:
# - using a separate module to manage courses
# - importing nothing except standard library
# - storing data in a TXT file using '|' separators

