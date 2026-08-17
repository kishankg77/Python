# Task 4: Dictionaries
# Demonstrating creation, accessing, adding, updating,
# removing data, displaying keys and values, and dictionary methods

# 1. Creating a Student Information Dictionary
student = {
    "Name": "Kishan",
    "Age": 20,
    "Course": "B.Tech CSE",
    "City": "Varanasi"
}

print("Original Student Information:")
print(student)

# 2. Accessing values
print("\nAccessing Values:")
print("Name:", student["Name"])
print("Course:", student["Course"])

# 3. Adding a new key-value pair
student["College"] = "ABC Engineering College"
print("\nAfter Adding College:")
print(student)

# 4. Updating a value
student["Age"] = 21
print("\nAfter Updating Age:")
print(student)

# 5. Removing data
student.pop("City")
print("\nAfter Removing City:")
print(student)

# 6. Displaying keys
print("\nDictionary Keys:")
print(student.keys())

# 7. Displaying values
print("\nDictionary Values:")
print(student.values())

# 8. Displaying key-value pairs
print("\nDictionary Items:")
print(student.items())

# 9. Using get() method
print("\nUsing get() method:")
print("Name:", student.get("Name"))

# 10. Checking if a key exists
print("\nChecking Key:")
print("Course" in student)