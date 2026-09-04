# Task 1: Classes & Objects
# Entity: Student Profile Management System

class Student:
    """Represents an academic student entity."""

    def __init__(self, student_id, name, course, gpa):
        # Initializing instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.gpa = gpa

    def display_details(self):
        """Method to display complete profile information of the student."""
        print(f"{'ID':<12}: {self.student_id}")
        print(f"{'Name':<12}: {self.name}")
        print(f"{'Course':<12}: {self.course}")
        print(f"{'GPA':<12}: {self.gpa:.2f}")
        print(f"{'Standing':<12}: {self.get_academic_standing()}")
        print("-" * 40)

    def get_academic_standing(self):
        """Method to evaluate standing based on GPA attribute."""
        if self.gpa >= 8.5:
            return "First Class with Distinction"
        elif self.gpa >= 6.5:
            return "First Class"
        else:
            return "Pass Class"


def main():
    print("=== Task 1: Classes & Objects Demonstration ===\n")

    # Creating two distinct Student objects (instances)
    student1 = Student(
        student_id="INT2026-01",
        name="Kishan Kumar Gupta",
        course="Python Internova",
        gpa=9.25
    )

    student2 = Student(
        student_id="INT2026-02",
        name="Aarav Sharma",
        course="Cloud Architecture",
        gpa=7.80
    )

    # Invoking the instance method on each object to display information
    print("Displaying Student 1 Details:")
    student1.display_details()

    print("\nDisplaying Student 2 Details:")
    student2.display_details()


if __name__ == "__main__":
    main()