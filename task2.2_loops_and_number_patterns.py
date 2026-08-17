# Task 2: Loops & Number Patterns

try:
    N = int(input("Enter a positive integer (N): "))

    if N <= 0:
        print("Please enter a number greater than 0.")
    else:
        # 1. Print numbers from 1 to N using a for loop
        print("\n--- Numbers from 1 to N (for loop) ---")
        for i in range(1, N + 1):
            print(i, end=" ")
        print()

        # 2. Print numbers from N to 1 using a while loop
        print("\n--- Numbers from N to 1 (while loop) ---")
        current = N
        while current >= 1:
            print(current, end=" ")
            current -= 1
        print()

        # 3. Print the multiplication table of N
        print(f"\n--- Multiplication Table for {N} ---")
        for i in range(1, 11):
            print(f"{N} x {i} = {N * i}")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
    