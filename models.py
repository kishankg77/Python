from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract base class demonstrating abstraction."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display(self):
        """Every child class must implement display()."""
        pass


class Student(Person):
    """Base Student class."""

    def __init__(self, student_id, name, age, course, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        self.marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if not isinstance(value, dict):
            raise TypeError("Marks must be stored in a dictionary.")
        for subject, mark in value.items():
            if not isinstance(mark, (int, float)) or not 0 <= mark <= 100:
                raise ValueError(f"Invalid marks for {subject}.")
        self.__marks = value

    def total_marks(self):
        return sum(self.__marks.values())

    def average_marks(self):
        if not self.__marks:
            return 0
        return self.total_marks() / len(self.__marks)

    def grade(self):
        average = self.average_marks()
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        return (
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Course: {self.course}\n"
            f"Marks: {self.marks}\n"
            f"Total: {self.total_marks():.2f}\n"
            f"Average: {self.average_marks():.2f}\n"
            f"Grade: {self.grade()}\n"
            + "-" * 50
        )


class GraduateStudent(Student):
    """Child class demonstrating inheritance and polymorphism."""

    def display(self):
        return (
            f"[Graduate Student]\n"
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Course: {self.course}\n"
            f"Marks: {self.marks}\n"
            f"Total: {self.total_marks():.2f}\n"
            f"Average: {self.average_marks():.2f}\n"
            f"Grade: {self.grade()}\n"
            f"Status: {'Pass' if self.grade() != 'F' else 'Needs Improvement'}\n"
            + "-" * 50
        )

    def study_level(self):
        return "Undergraduate / Graduate-level Student"
