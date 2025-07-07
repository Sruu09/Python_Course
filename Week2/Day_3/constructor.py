'''
__init__() is a special method which is first run as soon as the object is created.
It is also called Constructor
It takes self-arguement and can also take further arguments
'''
class Employee:
    language = "Python"
    salary = 120000

    def __init__(self):    #dunder method which is automatically called
        print("I am an Object!")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

harry = Employee()
print(harry.language,harry.salary)