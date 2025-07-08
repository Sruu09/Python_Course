#A class method is a method that works with the class itself (not just an object). It can access and modify class variables.
class Employee:
    company = "Google"

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

# Usage
print(Employee.company)      # Google
Employee.change_company("Microsoft")
print(Employee.company)      # Microsoft
