# Assignment Compliance Report

## Project Overview

This report checks the read-only `academic_system` Python console project against the given university assignment requirements.

### Detected Project Structure (from file scan)
- Total folders: **5**
  - `academic_system/`
  - `students/`
  - `courses/`
  - `grades/`
  - `reports/`
  - `data/` (data folder)
- Total Python files: **8**
  - `main.py`
  - `students/__init__.py`
  - `students/student_manager.py`
  - `students/validation.py`
  - `courses/__init__.py`
  - `courses/course_manager.py`
  - `grades/__init__.py`
  - `grades/grade_manager.py`
  - `reports/__init__.py`
  - `reports/report_generator.py`
- Total packages: **4**
  - `students`, `courses`, `grades`, `reports` (each has an `__init__.py`)
- Total modules: **5**
  - `main`
  - `students.validation`
  - `students.student_manager`
  - `courses.course_manager`
  - `grades.grade_manager`
  - `reports.report_generator`

## Requirement Validation

### 1) Creating and Importing Modules
**PASS**

**Evidence (imports found):**
- `main.py` imports manager functions:
  - `from students.student_manager import add_student, view_students`
  - `from courses.course_manager import add_course, view_courses`
  - `from grades.grade_manager import assign_grade, view_grades`
  - `from reports.report_generator import generate_report`

**Files involved:**
- `main.py`
- `students/student_manager.py`
- `courses/course_manager.py`
- `grades/grade_manager.py`
- `reports/report_generator.py`

---

### 2) Creating Custom Packages
**PASS**

**Evidence:**
Package folders detected containing `__init__.py`:
- `students/__init__.py`
- `courses/__init__.py`
- `grades/__init__.py`
- `reports/__init__.py`

---

### 3) Organizing Code into Multiple Files
**PASS**

**Evidence (modules separated):**
- `main.py`: menu + calls functions
- `students/validation.py`: student ID/name validation
- `students/student_manager.py`: student TXT persistence
- `courses/course_manager.py`: course TXT persistence
- `grades/grade_manager.py`: grade TXT persistence
- `reports/report_generator.py`: combines TXT data to generate report

---

### 4) Reading and Writing Data
**PASS**

**Evidence (TXT file operations via `open()`):**
- `students/student_manager.py`
  - `_read_students()` opens `students.txt` (read)
  - `_write_students()` opens `students.txt` (write)
- `courses/course_manager.py`
  - `_read_courses()` opens `courses.txt` (read)
  - `_write_courses()` opens `courses.txt` (write)
- `grades/grade_manager.py`
  - `_read_grades()` opens `grades.txt` (read)
  - `_write_grades()` opens `grades.txt` (write)
- `reports/report_generator.py`
  - `_read_lines()` opens TXT files (read)

**TXT files involved (expected by assignment):**
- `data/students.txt`
- `data/courses.txt`
- `data/grades.txt`

---

### 5) Function Reuse Across Modules
**PASS**

**Evidence (cross-module function usage):**
- `main.py` calls functions imported from other modules:
  - `add_student()`, `view_students()`
  - `add_course()`, `view_courses()`
  - `assign_grade()`, `view_grades()`
  - `generate_report()`

**Evidence of module-level reuse:**
- `students/student_manager.py` imports validation functions from `students/validation.py`:
  - `validate_student_id()`
  - `validate_student_name()`

---

### 6) Console-Based Application
**PASS**

**Evidence:**
- Menu-driven loop in `main.py`:
  - `show_menu()` prints menu items
  - `input()` reads choice
  - `print()` displays results

---

## Architecture Assessment
**Intermediate**

Justification:
- Clean separation into packages/modules
- File-based persistence layer per entity (students/courses/grades)
- Report combines data across modules
- Still beginner-friendly (no overengineering, no advanced abstractions)

## Lecturer Evaluation (Simulated)

### Strengths
- Clear modular design with packages (`students`, `courses`, `grades`, `reports`).
- Uses TXT files for storage (meets the assignment constraint).
- `main.py` focuses on the console menu and delegates actions to modules.
- Validation is centralized in `students/validation.py`.

### Weaknesses
- Report prints grouped rows but does not include grade summary statistics (e.g., average per course).
- Data consistency relies on the user entering consistent course codes/student IDs (no referential integrity checks).

### Areas for Improvement
- Validate that assigned grades reference existing student IDs and course codes.
- Improve report formatting (e.g., show grade distribution or sort courses).
- Consider a small “press Enter to continue” UX enhancement.

## Estimated Grade
- **Percentage:** **96%**
- **Letter Grade:** **A**
- **Justification:** All required features are present and aligned with the constraints (standard Python only, console-only, TXT storage, module imports, validation usage, and menu-driven interaction).

## Final Compliance Score
- **Score: 96/100**
- **Assignment-ready for submission:** **YES (PASS)**

