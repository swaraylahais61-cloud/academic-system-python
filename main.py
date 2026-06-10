# main.py
# This is the entry point for the console application.
# It demonstrates using Python modules/packages via imports from:
# - students/student_manager.py
# - courses/course_manager.py
# - grades/grade_manager.py
# - reports/report_generator.py

from students.student_manager import (
    add_student,
    view_students,
)
from courses.course_manager import (
    add_course,
    view_courses,
)
from grades.grade_manager import (
    assign_grade,
    view_grades,
)
from reports.report_generator import generate_report



def show_menu() -> None:
    print("\n==== University Academic System ====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. View Courses")
    print("5. Assign Grade")
    print("6. View Grades")
    print("7. Generate Academic Report")
    print("8. Exit")


def main() -> None:
    # Loop until the user chooses to exit.
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            # Student management
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            # Course management
            add_course()
        elif choice == "4":
            view_courses()
        elif choice == "5":
            # Grade management
            assign_grade()
        elif choice == "6":
            view_grades()
        elif choice == "7":
            # Report generation
            generate_report()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()

# ---- Learning note (for presentation) ----
# main.py does not contain business logic.
# It only handles user interaction and calls functions from other modules.
# This is a clean example of package/module separation.
