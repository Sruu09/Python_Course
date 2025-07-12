# --- What is the 'global' keyword? ---

# It lets you modify a variable defined outside a function (in the global scope) from inside that function.

count = 0  # global variable

def increment():
    global count  # tell Python we mean the global 'count'
    count += 1    # modify the global variable

increment()
print(count)  # Output: 1

# Without 'global', modifying 'count' inside the function would create a new local variable instead.
