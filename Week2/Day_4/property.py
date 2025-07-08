'''
The @property decorator is used to make a method behave like an attribute.

It allows you to:

Access method results like a variable.

Create getter behavior without using .get_something().
'''
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            print("Marks cannot be negative!")
        else:
            self._marks = value

s = Student(90)
print(s.marks)      # 90
s.marks = 95        # Setter called
print(s.marks)      # 95
s.marks = -10       # Invalid
