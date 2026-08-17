# Task 1: Lists
# Demonstrating creation, accessing, adding, updating,
# removing, and sorting elements

# 1. Creating a list
numbers = [50, 20, 40, 10, 30]
print("Original list:", numbers)

# 2. Accessing elements
print("First element:", numbers[0])
print("Third element:", numbers[2])

# 3. Adding an element
numbers.append(60)
print("After adding 60:", numbers)

# 4. Updating an element
numbers[1] = 25
print("After updating second element:", numbers)

# 5. Removing an element
numbers.remove(40)
print("After removing 40:", numbers)

# 6. Sorting the list
numbers.sort()
print("After sorting:", numbers)