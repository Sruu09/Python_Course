# Function with arguments in Python
# Arguments are values passed into a function when it's called
# They help make functions dynamic and reusable

# Example 1: Function with one argument
def greet(name):  # 'name' is the argument
    print(f"Hello, {name}!")

greet("Srushti")  # Output: Hello, Srushti!


# Example 2: Function with two arguments
def add(a, b):  # 'a' and 'b' are parameters (placeholders)
    return a + b

result = add(3, 5)  # Passing arguments 3 and 5
print("Sum:", result)  # Output: Sum: 8


# Example 3: Function with default argument
def welcome(user="Guest"):  # Default value is 'Guest'
    print(f"Welcome, {user}!")

welcome()           # Output: Welcome, Guest!
welcome("Riya")     # Output: Welcome, Riya!


# Example 4: Function with keyword arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=20, name="Amit")  # Order doesn't matter with keyword arguments


# Example 5: Function with variable number of arguments (*args)
def total_marks(*marks):  # Accepts any number of arguments as a tuple
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(85, 90, 78, 92)  # Output: Total: 345


# Example 6: Function with variable keyword arguments (**kwargs)
def profile(**info):  # Accepts keyword arguments as a dictionary
    print("Profile Info:")
    for key, value in info.items():
        print(f"{key}: {value}")

profile(name="Srushti", age=21, hobby="Badminton")
