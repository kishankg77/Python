# Task 3: Inheritance
# Demonstrating Parent and Child Classes

# Parent/Base Class
class Employee:
    def __init__(self, name, age, employee_id):
        self.name = name
        self.age = age
        self.employee_id = employee_id

    # Common method
    def display_info(self):
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Employee ID :", self.employee_id)


# Child/Derived Class
class Developer(Employee):
    def __init__(self, name, age, employee_id, programming_language):
        # Calling parent class constructor
        super().__init__(name, age, employee_id)
        self.programming_language = programming_language

    # Specific method of Developer class
    def display_skill(self):
        print("Programming Language :", self.programming_language)


# Creating objects of the child class
developer1 = Developer("Kishan Gupta", 20, "EMP101", "Python")
developer2 = Developer("Rahul Sharma", 21, "EMP102", "C++")


# Demonstrating inherited functionality
print("----- Developer 1 -----")
developer1.display_info()
developer1.display_skill()

print("\n----- Developer 2 -----")
developer2.display_info()
developer2.display_skill()