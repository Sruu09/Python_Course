'''
List are containers to store a set of values of any data type
It can be indexed just like a string
It is mutable

'''
fun = ["Apples","Orange",2,False,345.23]
fun[2] = "Grapes"
print(fun)

# Most Used List Methods in Python

# Sample list for reference
fruits = ["apple", "banana", "cherry"]

# 1. append(item) - Adds an item to the end of the list
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# 2. insert(index, item) - Inserts an item at a specific position
fruits.insert(1, "mango")
print(fruits)  # ['apple', 'mango', 'banana', 'cherry', 'orange']

# 3. extend(iterable) - Adds all elements of an iterable (like another list)
more_fruits = ["kiwi", "grape"]
fruits.extend(more_fruits)
print(fruits)  # ['apple', 'mango', 'banana', 'cherry', 'orange', 'kiwi', 'grape']

# 4. remove(item) - Removes the first occurrence of the item
fruits.remove("banana")
print(fruits)  # ['apple', 'mango', 'cherry', 'orange', 'kiwi', 'grape']

# 5. pop([index]) - Removes and returns the item at the given index (last if not specified)
last_fruit = fruits.pop()
print(last_fruit)  # 'grape'
print(fruits)      # ['apple', 'mango', 'cherry', 'orange', 'kiwi']

# 6. index(item) - Returns the index of the first occurrence
print(fruits.index("cherry"))  # 2

# 7. count(item) - Returns how many times an item appears in the list
print(fruits.count("apple"))  # 1

# 8. sort() - Sorts the list in ascending order (modifies the list)
fruits.sort()
print(fruits)  # ['apple', 'cherry', 'kiwi', 'mango', 'orange']

# 9. reverse() - Reverses the list order in-place
fruits.reverse()
print(fruits)  # ['orange', 'mango', 'kiwi', 'cherry', 'apple']

# 10. copy() - Returns a shallow copy of the list
copy_fruits = fruits.copy()
print(copy_fruits)  # ['orange', 'mango', 'kiwi', 'cherry', 'apple']

# 11. clear() - Removes all elements from the list
fruits.clear()
print(fruits)  # []
