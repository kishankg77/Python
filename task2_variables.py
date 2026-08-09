# Task 2: Demonstrating Python Variables and Data Types

# Declaring variables of different data types
user_name = "Kishan"          # String (str)
user_age = 20              # Integer (int)
user_height = 5.9           # Floating-point number (float)
is_enrolled = True          # Boolean (bool)
courses = ["Python", "SQL"]  # List (list)
profile = {"role": "Student", "grade": "A"}  # Dictionary (dict)

# Printing variable values and their data types
print("--- Variables and Data Types ---")
print(f"user_name   | Value: {user_name:<10} | Type: {type(user_name)}")
print(f"user_age    | Value: {user_age:<10} | Type: {type(user_age)}")
print(f"user_height | Value: {user_height:<10} | Type: {type(user_height)}")
print(f"is_enrolled | Value: {str(is_enrolled):<10} | Type: {type(is_enrolled)}")
print(f"courses     | Value: {str(courses):<10} | Type: {type(courses)}")
print(f"profile     | Value: {str(profile):<10} | Type: {type(profile)}")