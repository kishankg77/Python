# FINAL PYTHON PROJECT REPORT

## Student Management System

**Submitted By:** KISHAN KUMAR GUPTA  
**Course:** B.Tech – Computer Science & Engineering  
**Project Type:** Python Final Project  
**Task:** Task 3 — Final Python Project (50 Marks)

---

## 1. Introduction

The Student Management System is a menu-driven Python application designed to manage student academic records.

The application allows the user to add, view, search, update and delete student records. It also calculates total marks, average marks and grades. Student information is permanently stored in a JSON file.

The project applies the Python concepts learned during the internship from Week 1 to Week 6.

---

## 2. Objectives

The main objectives are:

1. To develop a practical Python application.
2. To understand and implement Object-Oriented Programming.
3. To use data structures for storing records.
4. To implement file handling for permanent data storage.
5. To handle invalid inputs using exception handling.
6. To demonstrate inheritance, polymorphism, encapsulation and abstraction.
7. To understand basic Git and GitHub workflow.

---

## 3. Technologies Used

- Python 3
- JSON
- Object-Oriented Programming
- VS Code
- Git
- GitHub

No external Python package is required.

---

## 4. Features

### 4.1 Add Student
The user enters Student ID, name, age, course and marks.

### 4.2 View Students
Displays all stored student records.

### 4.3 Search Student
Searches for a student using Student ID.

### 4.4 Update Student
Allows modification of name, course, age and marks.

### 4.5 Delete Student
Removes a student record from the system.

### 4.6 Grade Calculation
The system calculates grades according to the average marks.

| Average | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

### 4.7 Class Statistics
The application calculates the number of students, class average, highest average and lowest average.

### 4.8 File Storage
Student records are stored in `students.json` using Python's JSON library.

---

## 5. Python Concepts Implemented

### Variables and Data Types
The project uses strings, integers, floating-point values, lists and dictionaries.

### Input and Output
`input()` is used for user input and `print()` displays results.

### Operators
Arithmetic, comparison and logical operations are used for calculations and validation.

### Type Casting
User input is converted into `int` and `float`.

### Conditional Statements
`if`, `elif` and `else` are used for menu selection, validation and grade calculation.

### Loops
`while` is used for the main menu and `for` loops are used for subjects and student records.

### Functions
The application is divided into reusable functions such as `add_student()`, `search_student()` and `delete_student()`.

### Data Structures
Lists store multiple student objects and dictionaries store marks and JSON data.

### File Handling
`open()` is used with read/write modes to store student information.

### Exception Handling
`try-except` blocks handle invalid numeric input and file/JSON errors.

### Python Libraries
The project uses standard libraries:
- `json`
- `os`
- `datetime`
- `abc`

---

## 6. Object-Oriented Programming

### Classes and Objects
The project contains `Person`, `Student`, `GraduateStudent` and `StudentManager` classes.

### Constructor
The `__init__()` method initializes object attributes.

### Inheritance
`Student` inherits from `Person`, while `GraduateStudent` inherits from `Student`.

### Polymorphism
`GraduateStudent` overrides the `display()` method inherited from `Student`.

### Encapsulation
The marks attribute uses the private variable `__marks`. The student collection in `StudentManager` uses `__students`.

A property and setter provide controlled access to marks.

### Abstraction
`Person` is an abstract class using Python's `ABC` and `@abstractmethod`. Child classes implement the `display()` method.

---

## 7. File Handling

The program stores data in:

`students.json`

Example structure:

```json
[
    {
        "student_id": "ST001",
        "name": "Rahul",
        "age": 20,
        "course": "B.Tech CSE",
        "marks": {
            "Python": 85,
            "Data Structures": 78,
            "Database": 82,
            "Computer Networks": 80,
            "AI": 90
        }
    }
]
```

This allows records to remain available after the program is closed.

---

## 8. Exception Handling

The project handles:

- Non-numeric age
- Invalid marks
- Invalid menu choice
- Empty Student ID
- Duplicate Student ID
- Missing JSON file
- Invalid JSON data
- File access errors

This makes the application more reliable.

---

## 9. Algorithm

1. Start the program.
2. Create a `StudentManager` object.
3. Load existing records from JSON.
4. Display the main menu.
5. Ask the user for a choice.
6. Perform the selected operation.
7. Save changes to JSON.
8. Return to the main menu.
9. Exit when the user selects option 7.

---

## 10. Sample Output

```text
============================================================
              STUDENT MANAGEMENT SYSTEM
============================================================
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Class Statistics
7. Exit

Enter your choice (1-7): 1

--- Add Student ---
Enter Student ID: ST001
Enter Student Name: Rahul
Enter Course: B.Tech CSE
Enter Age: 20
Enter marks for Python (0-100): 85
Enter marks for Data Structures (0-100): 78
Enter marks for Database (0-100): 82
Enter marks for Computer Networks (0-100): 80
Enter marks for AI (0-100): 90

Student added successfully.
```

---

## 11. Testing

| Test Case | Input | Expected Result |
|---|---|---|
| Add valid student | Correct details | Student added |
| Duplicate ID | Existing ID | Error message |
| Invalid age | `abc` | Input rejected |
| Invalid marks | `110` | Input rejected |
| Search existing ID | ST001 | Student displayed |
| Search wrong ID | ST999 | Not found |
| Delete existing ID | ST001 | Student deleted |
| Empty records | No data | Proper message |

---

## 12. Git and GitHub

The project can be uploaded to GitHub using:

```bash
git init
git add .
git commit -m "Initial Student Management System project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Git provides version control and GitHub provides online repository hosting.

---

## 13. Advantages

- Simple and user-friendly
- Modular code
- Permanent JSON storage
- No external dependencies
- Demonstrates major Python concepts
- Easy to modify and extend

---

## 14. Future Enhancements

Possible future improvements include:

- GUI using Tkinter
- SQLite/MySQL database
- Login and authentication
- Attendance management
- Export reports to CSV/PDF
- Web version using Flask or Django
- Student performance charts

---

## 15. Conclusion

The Student Management System successfully demonstrates practical implementation of Python concepts learned during the internship.

The project combines procedural programming, data structures, file handling, exception handling and Object-Oriented Programming into one complete application.

It also demonstrates advanced OOP principles including inheritance, polymorphism, encapsulation and abstraction, along with basic Git and GitHub usage.

Therefore, the project fulfills the requirements of the Final Python Project — Task 3.
