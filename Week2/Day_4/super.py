#super() allows you to call methods from the parent class.
#Mostly used in constructors (__init__) or method overriding.
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()  # calls Parent's show
        print("Child method")

c = Child()
c.show()
