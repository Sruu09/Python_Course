# Multilevel Inheritance: A class inherits from a child class, which itself inherits from another class.
class Grandfather:
    def old_story(self):
        print("Grandfather tells stories")

class Father(Grandfather):
    def teach(self):
        print("Father teaches")

class Son(Father):
    def play(self):
        print("Son plays cricket")

s = Son()
s.old_story()
s.teach()
s.play()
