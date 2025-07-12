# --- What is a lambda function? ---

# A lambda function is a small, anonymous (unnamed) function.
# Syntax: lambda arguments: expression

# Regular function:
def add(x, y):
    return x + y

# Same using lambda:
add_lambda = lambda x, y: x + y

print(add(2, 3))         # Output: 5
print(add_lambda(2, 3))  # Output: 5

# Lambda is useful for short, one-line functions (especially in functions like map, filter, sort, etc.)

# Example with sort:
points = [(2, 3), (1, 2), (4, 1)]
# Sort by the second value of each tuple
points.sort(key=lambda point: point[1])
print(points)  # Output: [(4, 1), (1, 2), (2, 3)]
