'''
Calls itself again
it is used to directly use a mathematical formula as function.
'''

# Recursive function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage
num = 5
print(f"Factorial of {num} is:", factorial(num))  # Output: 120







