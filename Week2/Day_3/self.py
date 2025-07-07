#Self refers to the instance of the class. It is automatically passed with a function call from an object

class Employee:
    language = "Python"
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

harry = Employee()
harry.getInfo()