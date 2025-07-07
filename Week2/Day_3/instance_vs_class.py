class Employee:
    language = "Python" #This is class attribute
    salary = 1200000

harry = Employee()
harry.language = "JavaScript"  #This is an instance attribute
print(harry.language,harry.salary)

#Instance attribute take preference over class attributes