'''
Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class (called the child class or derived class) to inherit attributes and methods from another class (called the parent class or base class).

This promotes code reusability, modularity, and cleaner designs.

Syntax:
# Base (Parent) class
class Parent:
    def parent_method(self):
        print("This is a method from the Parent class.")

# Derived (Child) class inheriting from Parent
class Child(Parent):
    def child_method(self):
        print("This is a method from the Child class.")
'''

class Animal:  # Parent class
    def speak(self):
        print("Animals can make sounds.")

class Dog(Animal):  # Child class inheriting Animal
    def bark(self):
        print("Dog barks.")

# Creating object of Dog class
d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Own method
