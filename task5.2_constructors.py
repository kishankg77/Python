# Task 2: Constructors
# Demonstrating the use of __init__() constructor

class Student:
    # Constructor
    def __init__(self, name, age, course, city):
        self.name = name
        self.age = age
        self.course = course
        self.city = city

    # Method to display student information
    def display_info(self):
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Course :", self.course)
        print("City   :", self.city)


# Creating objects with different values
student1 = Student("Kishan Gupta", 20, "B.Tech CSE", "Varanasi")
student2 = Student("Rahul Sharma", 21, "B.Tech CSE", "Lucknow")

# Accessing initialized attributes
print("Student 1 Name:", student1.name)
print("Student 2 Course:", student2.course)

# Displaying complete information using method
print("\n----- Student 1 Information -----")
student1.display_info()

print("\n----- Student 2 Information -----")
student2.display_info()