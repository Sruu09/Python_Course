# Multiple Inheritance :One child class inherits from more than one parent class.
class Father:
    def gardening(self):
        print("Father enjoys gardening")

class Mother:
    def cooking(self):
        print("Mother loves cooking")

class Child(Father, Mother):
    def playing(self):
        print("Child plays football")

c = Child()
c.gardening()
c.cooking()
c.playing()
