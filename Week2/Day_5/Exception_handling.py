# 🚨 Exception Handling in Python (VS Code Friendly)

# What is Exception Handling?
# → Used to handle runtime errors without crashing the program.
# → Examples: division by zero, invalid input, file errors, etc.

# --- Basic Syntax ---
try:
    # Code that may cause an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)

except ZeroDivisionError:
    # Handles division by zero
    print("Error: Cannot divide by zero.")

except ValueError:
    # Handles invalid integer input
    print("Error: Please enter a valid number.")

except Exception as e:
    # Handles any other exceptions
    print("Unexpected error:", e)

else:
    # Runs if no exception occurs
    print("No errors occurred.")

finally:
    # Runs always (used for cleanup)
    print("Program ended.")


# --- Using 'raise' ---
# → 'raise' is used to manually trigger an exception

def check_age(age):
    if age < 0:
        # manually raise an exception
        raise ValueError("Age cannot be negative.")
    print("Age is valid.")

try:
    check_age(-3)
except ValueError as err:
    print("Raised Exception:", err)

# Output:
# Raised Exception: Age cannot be negative.
