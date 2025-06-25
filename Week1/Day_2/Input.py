'''
input() function:
This function allows user to take input from the keyboard as string
It is improtant to note that the output is always a string (even if a number is entered)
'''

a = input("Enter Number 1: ") #2
b = input("Enter Number 2: ") #5

print(a+b) #result = 25 (concat because compiler compiled it as str)

x = int(input("Enter Number 1: ")) #2
y = int(input("Enter Number 2: ")) #5

print(x+y)  #result = 7 (compiler copiled it as int)