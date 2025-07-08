# Hierarchical Inheritance : Multiple child classes inherit from a single parent class.
class Parent:
    def guide(self):
        print("Parent guides")

class Son(Parent):
    def study(self):
        print("Son studies")

class Daughter(Parent):
    def dance(self):
        print("Daughter dances")

s = Son()
d = Daughter()

s.guide()
s.study()

d.guide()
d.dance()
