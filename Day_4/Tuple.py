'''
A tuple is an immutable data type in python 
'''
a = ()                        #Empty tuple
b = (1, )                     #Tuple with only one element
c = (1,2,3,4,5)               #Tuple with more than one element

# Most Used Tuple Methods and Operations in Python

# Sample tuple
fruits = ("apple", "banana", "cherry", "banana")

# 1. count(item) - Returns the number of times the item appears in the tuple
print(fruits.count("banana"))  # Output: 2

# 2. index(item) - Returns the index of the first occurrence of the item
print(fruits.index("cherry"))  # Output: 2

# Tuples are immutable, meaning you CANNOT do the following:
# ❌ fruits.append("orange")
# ❌ fruits.remove("banana")
# ❌ fruits[1] = "mango"  → This will raise an error

# But you can:
# 3. Access elements by index
print(fruits[0])  # Output: "apple"

# 4. Slicing works like lists
print(fruits[1:3])  # Output: ("banana", "cherry")

# 5. Loop through a tuple
for fruit in fruits:
    print(fruit)

# 6. Check if item exists
if "apple" in fruits:
    print("Apple is in the tuple")  # Output: Apple is in the tuple

# 7. Tuple concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4)

# 8. Tuple repetition
print(t1 * 2)  # Output: (1, 2, 1, 2)

# 9. Convert tuple to list if you need to modify it
fruits_list = list(fruits)
fruits_list.append("orange")
print(tuple(fruits_list))  # Output: ('apple', 'banana', 'cherry', 'banana', 'orange')

# 10. Tuple unpacking
person = ("Srushti", 21, "India")
name, age, country = person
print(name)     # Output: Srushti
print(age)      # Output: 21
print(country)  # Output: India

#11. `in` and `not in`
numbers = (1, 2, 3, 4)
print(3 in numbers)          # True → 3 exists in the tuple
print(5 not in numbers)      # True → 5 is not in the tuple