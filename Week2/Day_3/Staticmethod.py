class Employee:
    language = "Python"
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod    #Sometimes we need a func that does not use the self parameter. 
    def greet():
        print("Good Morning")

harry = Employee()
harry.getInfo()