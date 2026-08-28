# Demonstrating Random, Math, and Datetime libraries

import random
import math
import datetime

# 1. Random Library
# The random library is used to generate random values.
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)


# 2. Math Library
# The math library provides mathematical functions.
number = 64
square_root = math.sqrt(number)
print("Square root of", number, "=", square_root)

# Performing another mathematical operation: power
power_result = math.pow(2, 5)
print("2 raised to the power 5 =", power_result)


# 3. Datetime Library
# The datetime library is used to work with dates and time.
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)