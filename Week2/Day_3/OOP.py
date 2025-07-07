'''
Solving problem by creating object is one of the most popular approach in programming.

Class :
A class is a blueprint for creating object

Object:
An object is an instantiation of a class. When a class is defined, a template (info) is defined. Memory allocated only after object instantiation
Objects of given class can invoke the methods available to it without revealing the implementation detailed to the user - Abstraction & Encapsulation
'''

class Employee:
    language = "Python" #This is class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry"  #This is an instance attribute
print(harry.name,harry.language,harry.salary)

rohan = Employee()
print(rohan.language,rohan.salary)

#Here name is an instance attribute and salary and language attributes as they directly belong to the class