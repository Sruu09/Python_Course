# Dictionary and Sets

# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {"kya": "What?", "thike":"Okay", "jaa":"Go"}
word = input("Enter the word you want meaning of: ")
print(words[word])

# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).

num = set()
n1= int(input("Enter number:"))
num.add(n1)
n2= int(input("Enter number:"))
num.add(n2)
n3= int(input("Enter number:"))
num.add(n3)
n4= int(input("Enter number:"))
num.add(n4)
n5= int(input("Enter number:"))
num.add(n5)
n6= int(input("Enter number:"))
num.add(n6)
n7= int(input("Enter number:"))
num.add(n7)
n8= int(input("Enter number:"))
num.add(n8)
print(num)


# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add("18")
print(s)


# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add("20")   
# length of s after these operations?



# 5. s = {}
# What is the type of 's'?
s = {}
print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d = {}
name = input("Enter name:")
lang = input("Enter language:")
d.update({name:lang})
name = input("Enter name:")
lang = input("Enter language:")
d.update({name:lang})
name = input("Enter name:")
lang = input("Enter language:")
d.update({name:lang})
name = input("Enter name:")
lang = input("Enter language:")
d.update({name:lang})

print(d)


# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

#Ans. Will update the value


# 8. If languages of two friends are same; what will happen to the program in problem 6?

#Ans. No changes


# 9. Can you change the values inside a list which is contained in Set S?
s = {8, 7, 12, "Harry", [1,2]}

#Ans. No






