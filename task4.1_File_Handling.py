# Task 1: File Handling
# Demonstrating creating, writing, reading, appending, and closing a file

# 1. Create a text file and write data into it
file = open("student.txt", "w")

file.write("Name: Kishan Gupta\n")
file.write("Course: B.Tech CSE\n")
file.write("Subject: Python Programming\n")

# Closing the file
file.close()

# 2. Read and display the data
file = open("student.txt", "r")

print("Original File Content:")
print(file.read())

file.close()

# 3. Append new data to the existing file
file = open("student.txt", "a")

file.write("Assignment: File Handling\n")
file.write("Status: Completed\n")

file.close()

# 4. Read and display the updated file content
file = open("student.txt", "r")

print("Updated File Content:")
print(file.read())

file.close()