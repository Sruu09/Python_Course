'''
Python: Guido van Rossum (1991)
Extension: .py

Module: A file containing code written by somebody else(usually) which can be imported and used in your program

PIP : It is the package manager for python which you can use to install a module on your system
pip install module_name

A Python REPL lets you run code line by line and see results instantly (terminal)
'''

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

import os

# Specify the directory path you want to list
directory_path = '.'  # '.' means current directory

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print(f"Contents of directory '{directory_path}':")
for item in contents:
    print(item)
