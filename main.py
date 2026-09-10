from student_manager import StudentManager
from models import GraduateStudent
from datetime import datetime


def print_header():
    print("\n" + "=" * 60)
    print("              STUDENT MANAGEMENT SYSTEM")
    print("=" * 60)


def get_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_float(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_marks():
    subjects = ["Python", "Data Structures", "Database", "Computer Networks", "AI"]
    marks = {}
    for subject in subjects:
        marks[subject] = get_float(
            f"Enter marks for {subject} (0-100): ", 0, 100
        )
    return marks


def add_student(manager):
    print("\n--- Add Student ---")
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return

    if manager.search_student(student_id):
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()
    age = get_int("Enter Age: ", 1, 100)
    marks = get_marks()

    student = GraduateStudent(student_id, name, age, course, marks)
    manager.add_student(student)
    print("Student added successfully.")


def view_students(manager):
    print("\n--- All Students ---")
    students = manager.get_all_students()
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student.display())


def search_student(manager):
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID: ").strip()
    student = manager.search_student(student_id)

    if student:
        print(student.display())
    else:
        print("Student not found.")


def update_student(manager):
    print("\n--- Update Student ---")
    student_id = input("Enter Student ID: ").strip()
    student = manager.search_student(student_id)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")
    name = input(f"Name [{student.name}]: ").strip()
    course = input(f"Course [{student.course}]: ").strip()
    age_text = input(f"Age [{student.age}]: ").strip()

    if name:
        student.name = name
    if course:
        student.course = course

    if age_text:
        try:
            age = int(age_text)
            if 1 <= age <= 100:
                student.age = age
            else:
                print("Invalid age. Existing age retained.")
        except ValueError:
            print("Invalid age. Existing age retained.")

    choice = input("Update marks too? (y/n): ").strip().lower()
    if choice == "y":
        student.marks = get_marks()

    manager.save_data()
    print("Student updated successfully.")


def delete_student(manager):
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID: ").strip()

    if manager.delete_student(student_id):
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def show_statistics(manager):
    print("\n--- Class Statistics ---")
    stats = manager.get_statistics()

    if stats["count"] == 0:
        print("No records available.")
        return

    print(f"Total Students : {stats['count']}")
    print(f"Class Average  : {stats['average']:.2f}")
    print(f"Highest Average : {stats['highest']:.2f}")
    print(f"Lowest Average  : {stats['lowest']:.2f}")


def main():
    manager = StudentManager()
    manager.load_data()

    while True:
        print_header()
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Class Statistics")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            add_student(manager)
        elif choice == "2":
            view_students(manager)
        elif choice == "3":
            search_student(manager)
        elif choice == "4":
            update_student(manager)
        elif choice == "5":
            delete_student(manager)
        elif choice == "6":
            show_statistics(manager)
        elif choice == "7":
            print("\nThank you for using Student Management System.")
            print(f"Session ended: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
            break
        else:
            print("Invalid choice. Please select 1-7.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
