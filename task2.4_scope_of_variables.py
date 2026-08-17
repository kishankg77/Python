# Task 4: Scope of Variables
# Demonstrating Local and Global Variables

# Global variable
message = "I am a Global Variable"


def demonstrate_scope():
    # Local variable
    message = "I am a Local Variable"

    print("Inside the function:")
    print(message)


# Accessing the global variable
print("Outside the function:")
print(message)

# Calling the function
demonstrate_scope()

# Global variable remains unchanged
print("\nOutside the function after calling it:")
print(message)