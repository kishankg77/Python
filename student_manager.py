import json
import os
from models import GraduateStudent


class StudentManager:
    """Handles CRUD operations and file storage."""

    FILE_NAME = "students.json"

    def __init__(self):
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)
        self.save_data()

    def get_all_students(self):
        return self.__students.copy()

    def search_student(self, student_id):
        for student in self.__students:
            if student.student_id.lower() == student_id.lower():
                return student
        return None

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student is None:
            return False

        self.__students.remove(student)
        self.save_data()
        return True

    def save_data(self):
        data = []
        for student in self.__students:
            data.append({
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "marks": student.marks
            })

        try:
            with open(self.FILE_NAME, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except (OSError, TypeError) as error:
            print(f"Could not save data: {error}")

    def load_data(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.__students.clear()

            for item in data:
                student = GraduateStudent(
                    item["student_id"],
                    item["name"],
                    item["age"],
                    item["course"],
                    item["marks"]
                )
                self.__students.append(student)

        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Could not load data: {error}")

    def get_statistics(self):
        if not self.__students:
            return {
                "count": 0,
                "average": 0,
                "highest": 0,
                "lowest": 0
            }

        averages = [student.average_marks() for student in self.__students]

        return {
            "count": len(self.__students),
            "average": sum(averages) / len(averages),
            "highest": max(averages),
            "lowest": min(averages)
        }
