# Task 2: Tuples
# Demonstrating creation, accessing, slicing,
# length, and basic tuple operations

# 1. Creating a tuple
numbers = (10, 20, 30, 40, 50)

print("Original tuple:", numbers)

# 2. Accessing elements using indexing
print("First element:", numbers[0])
print("Third element:", numbers[2])

# 3. Tuple slicing
print("Tuple from index 1 to 3:", numbers[1:4])

# 4. Finding the length
print("Length of tuple:", len(numbers))

# 5. Basic tuple operations

# Concatenation
new_tuple = numbers + (60, 70)
print("After concatenation:", new_tuple)

# Repetition
repeated_tuple = (1, 2) * 3
print("After repetition:", repeated_tuple)

# Membership operation
print("Is 30 present in tuple?", 30 in numbers)