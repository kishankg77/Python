# Task 3: Sets
# Demonstrating creation, duplicate removal,
# adding/removing elements, union, intersection, and difference

# 1. Creating a set and removing duplicate values
set1 = {10, 20, 30, 20, 40, 10}
print("Set after removing duplicates:", set1)

# 2. Adding an element
set1.add(50)
print("After adding 50:", set1)

# 3. Removing an element
set1.remove(30)
print("After removing 30:", set1)

# Creating another set for set operations
set2 = {20, 40, 50, 60, 70}

# 4. Union
print("Union:", set1.union(set2))

# 5. Intersection
print("Intersection:", set1.intersection(set2))

# 6. Difference
print("Difference (set1 - set2):", set1.difference(set2))