# Task 5: Built-in Python Modules
# Demonstrating math, random, and datetime

from datetime import datetime
import math
import random


def main():
    print("=== Built-in Modules Demonstration ===\n")

    # 1. math module operations
    number = 64
    angle_degrees = 45
    angle_radians = math.radians(angle_degrees)

    sqrt_val = math.isqrt(number) if number >= 0 else None
    sine_val = math.sin(angle_radians)

    print("--- 1. math Module ---")
    print(f"Square root of {number}: {math.sqrt(number)}")
    print(f"Sine of {angle_degrees}° ({angle_radians:.4f} rad): {sine_val:.4f}")
    print(f"Value of Pi: {math.pi:.6f}")

    # 2. random module operations
    random_int = random.randint(1, 100)
    items = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
    random_choice = random.choice(items)

    print("\n--- 2. random Module ---")
    print(f"Random integer between 1 and 100: {random_int}")
    print(f"Random choice from {items}: {random_choice}")

    # 3. datetime module operations
    now = datetime.now()
    formatted_date = now.strftime("%A, %B %d, %Y")
    formatted_time = now.strftime("%I:%M:%S %p")

    print("\n--- 3. datetime Module ---")
    print(f"Current Date: {formatted_date}")
    print(f"Current Time: {formatted_time}")
    print(f"ISO Format Timestamp: {now.isoformat()}")


if __name__ == "__main__":
    main()