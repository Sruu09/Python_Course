'''
Set is a collection of non-repetitive elements
 Properties:
 1. Unordered
 2. Unindexed
 3. Immutable
 4. Cannot contain duplicate values
'''

e = set()    #Dont use s = {} for empty set it is used for empty dictionary

# Most Used Set Methods in Python

# Sample sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# 1. add(item) - Adds an element to the set
set_a.add(10)
print(set_a)  # {1, 2, 3, 4, 10}

# 2. remove(item) - Removes the specified element (raises error if not found)
set_a.remove(2)
print(set_a)  # {1, 3, 4, 10}

# 3. discard(item) - Removes item if it exists (no error if it doesn’t)
set_a.discard(100)  # No error
print(set_a)

# 4. pop() - Removes and returns an arbitrary element (sets are unordered)
element = set_a.pop()
print(element)  # Could be any element
print(set_a)

# 5. clear() - Removes all elements from the set
temp = {1, 2, 3}
temp.clear()
print(temp)  # Output: set()

# 6. union(other_set) - Returns a new set with elements from both sets
print(set_a.union(set_b))  # {1, 3, 4, 5, 6, 10}

# 7. update(other_set) - Adds elements from another set (modifies the original)
set_a.update(set_b)
print(set_a)  # Now includes elements from set_b too

# 8. intersection(other_set) - Returns elements common to both sets
print(set_a.intersection(set_b))  # {3, 4, 5, 6}

# 9. intersection_update(other_set) - Updates original set to keep only common elements
set_x = {1, 2, 3}
set_x.intersection_update({2, 3, 4})
print(set_x)  # {2, 3}

# 10. difference(other_set) - Returns elements only in the first set
print(set_b.difference(set_a))  # set_b - set_a → elements only in set_b

# 11. difference_update(other_set) - Removes common elements from original set
set_y = {1, 2, 3, 4}
set_y.difference_update({3, 4})
print(set_y)  # {1, 2}

# 12. symmetric_difference(other_set) - Elements in either set but not both
print(set_a.symmetric_difference(set_b))

# 13. isdisjoint(other_set) - Returns True if sets have no elements in common
print(set_a.isdisjoint({100, 200}))  # True

# 14. issubset(other_set) - Checks if current set is a subset of another
print({1, 2}.issubset(set_a))  # True or False depending on set_a

# 15. issuperset(other_set) - Checks if current set is a superset
print(set_a.issuperset({3, 4}))  # True

# ✅ Sets are unordered, mutable, and cannot contain duplicate values
