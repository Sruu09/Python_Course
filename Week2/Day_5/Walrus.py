# --- What is the Walrus Operator (:=)? ---

# The walrus operator assigns a value to a variable as part of an expression.
# It lets you combine assignment and evaluation in one line.

# Example without walrus:
line = input("Enter text: ")
if line:
    print("You entered:", line)

# Same example with walrus:
if (line := input("Enter text: ")):
    print("You entered:", line)

# This saves one line and can make code more concise.
