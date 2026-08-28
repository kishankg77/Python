# Task 2: Exception Handling
# Demonstrating handling of invalid input,
# division by zero, and file not found errors

# 1. Handling Invalid User Input
try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)

except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")


# 2. Handling Division by Zero
try:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")


# 3. Handling File Not Found
try:
    file = open("unknown_file.txt", "r")
    data = file.read()
    print("\nFile Content:")
    print(data)
    file.close()

except FileNotFoundError:
    print("Error: The requested file was not found.")