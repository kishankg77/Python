# Task 4: Arithmetic Operators Calculator

print("=== Simple Python Arithmetic Calculator ===")

# Taking numeric inputs from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing calculations
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "Error (Division by zero)"
mod_result = num1 % num2 if num2 != 0 else "Error (Modulus by zero)"
exp_result = num1 ** num2

# Displaying results
print("\n--- Calculation Results ---")
print(f"Addition       ({num1} + {num2})  = {add_result}")
print(f"Subtraction    ({num1} - {num2})  = {sub_result}")
print(f"Multiplication ({num1} * {num2})  = {mul_result}")
print(f"Division       ({num1} / {num2})  = {div_result}")
print(f"Modulus        ({num1} % {num2})  = {mod_result}")
print(f"Exponentation  ({num1} ** {num2}) = {exp_result}")