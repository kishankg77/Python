# Task 3: Functions
# Calculator using Functions


# Define separate arithmetic functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Modulo by zero is not allowed."
    return a % b


# Main Program Execution
def main():
    print("--- Simple Function Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")

    choice = input("\nSelect operation (1-5): ").strip()

    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice! Please select an option between 1 and 5.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")
        elif choice == "5":
            result = modulus(num1, num2)
            print(f"\nResult: {num1} % {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")


if __name__ == "__main__":
    main()