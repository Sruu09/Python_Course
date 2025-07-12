# --- What is enumerate()? ---

# It adds a counter to an iterable (like a list) and returns it as an enumerate object.
# Useful when you need both the item and its index in a loop.

fruits = ['apple', 'banana', 'cherry']

# Without enumerate:
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

# With enumerate:
for index, fruit in enumerate(fruits):
    print(index, fruit)

# You can also start counting from a different number:
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
