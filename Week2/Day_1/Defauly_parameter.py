# Default Parameters in Python
# A default parameter is used when no value is passed for that parameter during the function call
# It helps make function arguments optional and avoids errors

# Example 1: Function with one default parameter
def greet(name="Guest"):  # 'Guest' is the default value
    print(f"Hello, {name}!")

greet()           # No argument passed → uses default → Output: Hello, Guest!
greet("Srushti")  # Argument passed → overrides default → Output: Hello, Srushti!


# Example 2: Multiple parameters with one default
def introduce(name, city="Mumbai"):
    print(f"{name} is from {city}.")

introduce("Riya")                # Output: Riya is from Mumbai
introduce("Amit", "Pune")        # Output: Amit is from Pune


# Example 3: Multiple default parameters
def connect(server="localhost", port=3306):
    print(f"Connecting to {server} on port {port}...")

connect()                        # Output: Connecting to localhost on port 3306...
connect("192.168.1.1")           # Output: Connecting to 192.168.1.1 on port 3306...
connect("db.server.com", 8080)   # Output: Connecting to db.server.com on port 8080...


# Important Rule:
# Parameters with default values must come **after** non-default ones
# This will cause an error:
# def wrong_func(a=10, b): ❌
#     print(a, b)

# Correct version:
def right_func(a, b=10):  # ✅
    print(a, b)

right_func(5)       # Output: 5 10
right_func(5, 20)   # Output: 5 20
