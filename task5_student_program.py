# Task 5: Student Information & Academic Summary Program

print("========================================")
print("     STUDENT ACADEMIC REPORT SYSTEM     ")
print("========================================\n")

# 1. Input: Student Details
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
class_grade = input("Enter Class/Grade: ")

# 2. Input: Marks in 3 Subjects
print("\nEnter Subject Marks (out of 100):")
math_marks = float(input("  Mathematics: "))
science_marks = float(input("  Science: "))
english_marks = float(input("  English: "))

# 3. Operations & Type Casting
total_marks = math_marks + science_marks + english_marks
max_marks = 300.0
percentage = (total_marks / max_marks) * 100
passed = percentage >= 40.0

# 4. Formatted Output Report
print("\n========================================")
print("           OFFICIAL REPORT CARD          ")
print("========================================")
print(f"Name        : {student_name}")
print(f"Roll Number : {roll_number}")
print(f"Class       : {class_grade}")
print("----------------------------------------")
print(f"Mathematics : {math_marks} / 100")
print(f"Science     : {science_marks} / 100")
print(f"English     : {english_marks} / 100")
print("----------------------------------------")
print(f"Total Score : {total_marks} / {max_marks}")
print(f"Percentage  : {percentage:.2f}%")
print(f"Pass Status : {'Passed' if passed else 'Failed'}")
print("========================================")