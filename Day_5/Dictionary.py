'''
Dictionary is a collection of key-value pairs
Syntax:
        a = {"key":"value", ....}

Properties:
1. It is unordered 
2. It is mutable
3. It is indexed
4. Cannot contain duplicate keys
'''
marks = { 
         "Ram": 100,
         "Shyam": 56,
         "Mukesh": 23,
}
print(marks,type(marks))


# Most Used Dictionary Methods in Python

# Sample dictionary
person = {
    "name": "Srushti",
    "age": 21,
    "country": "India"
}

# 1. keys() - Returns a view object of all keys
print(person.keys())  # dict_keys(['name', 'age', 'country'])

# 2. values() - Returns a view object of all values
print(person.values())  # dict_values(['Srushti', 21, 'India'])

# 3. items() - Returns a view of (key, value) pairs
print(person.items())  # dict_items([('name', 'Srushti'), ('age', 21), ('country', 'India')])

# 4. get(key) - Returns the value for the given key; returns None if key not found
print(person.get("age"))     # 21
print(person.get("email"))   # None

# 5. update(other_dict) - Updates the dictionary with key-value pairs from another dictionary
person.update({"email": "srushti@example.com"})
print(person)
# {'name': 'Srushti', 'age': 21, 'country': 'India', 'email': 'srushti@example.com'}

# 6. pop(key) - Removes and returns the value of the given key
age = person.pop("age")
print(age)        # 21
print(person)     # 'age' is removed

# 7. popitem() - Removes and returns the last inserted (key, value) pair
last_item = person.popitem()
print(last_item)  # e.g., ('email', 'srushti@example.com')

# 8. clear() - Removes all items from the dictionary
person.clear()
print(person)  # {}

# Re-initialize for more examples
person = {
    "name": "Srushti",
    "age": 21,
    "country": "India"
}

# 9. copy() - Returns a shallow copy of the dictionary
person_copy = person.copy()
print(person_copy)

# 10. fromkeys(iterable, value) - Creates a new dictionary from a list of keys and a common value
keys = ["name", "email", "age"]
default_dict = dict.fromkeys(keys, "N/A")
print(default_dict)
# {'name': 'N/A', 'email': 'N/A', 'age': 'N/A'}

# Membership with Dictionary
# ✅ Only checks for keys by default
print("name" in person)           # True
print("Srushti" in person)        # False
print("Srushti" in person.values())  # True

# Looping through a dictionary
for key, value in person.items():
    print(f"{key} → {value}")
