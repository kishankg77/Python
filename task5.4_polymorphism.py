# Task 4: Polymorphism
# Demonstrating the same method with different behaviors

# First class
class Dog:
    def make_sound(self):
        print("Dog says: Woof Woof!")


# Second class
class Cat:
    def make_sound(self):
        print("Cat says: Meow Meow!")


# Creating objects
dog = Dog()
cat = Cat()

# Same method call, different outputs
print("Dog:")
dog.make_sound()

print("\nCat:")
cat.make_sound()
