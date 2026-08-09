# Task 3: User Input, Formatting, and Type Casting

# Taking user input
raw_name = input("Enter your name: Kishan ")
raw_age = input("Enter your age: 20 ")
raw_city = input("Enter your city: Agra ")

# Type casting age string into an integer
age = int(raw_age)

# Formatted output
print("\n--- Profile Summary ---")
print(f"Hello! My name is {raw_name}.")
print(f"I am {age} years old.")
print(f"I live in {raw_city}.")

# Verification of type casting
print(f"\n[Note: Data type of 'age' after casting is {type(age)}]")