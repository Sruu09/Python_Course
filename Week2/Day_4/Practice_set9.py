''' #Create a class (2D vector) and use it to create another class representing a 3D vector
class TwoD:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"2-D vector is {self.i}i + {self.j}j")
    
class ThreeD(TwoD):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"3-D vector is {self.i}i + {self.j}j + {self.k}k")
    

a = TwoD(1,2)
a.show()

b = ThreeD(1,2,3)
b.show()

#Create a class Pets from a class Animals and further create a class Dog from Pets. Add a method bark to class Dog

class Animals:
    print("This is class Animals")

class Pets(Animals):
    print("This is class Pets")

class Dogs(Pets):
    print("This is class Dogs")

    def bark(self):
        print("Dogs Bark!")

a = Dogs()
a.bark()

'''
#Create a class Employee and add salary and increment properties
class Employee:
    salary = 23400
    increment = 20
    @property
    def salaryafterincrement(self):
        return(self.salary + self.salary * (self.increment/100))
    
    @increment.setter
    def increment(self,salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
print(e.salaryafterincrement)

#Complex number addition using operator overloading

class complex:
    def __init__(self,i,r):
        self.r = r
        self.i = i

    def __add__(self,c2):
        return complex(self.r + c2.r,self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1= complex(1,3)
c2 = complex(5,7)
print(c1+c2) 
        
