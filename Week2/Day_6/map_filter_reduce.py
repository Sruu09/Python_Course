# --- map(), filter(), reduce() in Python ---

# 1️⃣ map(): Applies a function to every item in an iterable

numbers = [1, 2, 3, 4]

# Using a regular function
def square(n):
    return n * n

squared = list(map(square, numbers))
print("Squared:", squared)  # Output: [1, 4, 9, 16]

# Using lambda
squared_lambda = list(map(lambda n: n * n, numbers))
print("Squared (lambda):", squared_lambda)


# 2️⃣ filter(): Filters items using a function that returns True/False

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers)) 
print("Even numbers:", evens)  # Output: [2, 4]


# 3️⃣ reduce(): Repeatedly applies a function to reduce the list to a single value

from functools import reduce

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)  # Output: 10

# Multiply all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)  # Output: 24
