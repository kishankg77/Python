# Task 1: Conditional Statements
# Student Grade Calculator

try:
    marks = float(input("Enter student's marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")
    elif marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: Fail")
except ValueError:
    print("Invalid input! Please enter a numeric value.")