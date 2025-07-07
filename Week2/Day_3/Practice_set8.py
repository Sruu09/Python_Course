'''
#Create a class "Programmer" for storing information of new programmers working at Microsoft
class Programmer:
    def __init__(self, name, employee_id, language, experience):
        self.name = name
        self.employee_id = employee_id
        self.language = language
        self.experience = experience  # in years

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Programming Language: {self.language}")
        print(f"Experience: {self.experience} years")
        print("Company: Microsoft")

p1 = Programmer("Alice Johnson", 101, "Python", 2)
p2 = Programmer("Bob Smith", 102, "C++", 5)

p1.display_info()
print()
p2.display_info()
'''

#Write a class "calculator" capable of finding square , cube and sqaure root of a number.

class calculator:

    def __init__(self,num):
        self.num = num

    def calc(self):
        print(f"Square: {self.num ** 2}")
        print(f"Cube: {self.num ** 3}")
        print(f"Square Root: {self.num ** 0.5}")

a = calculator(9)
a.calc()

#Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o. Does this change the class attribute?

class Name:
    a = 10

obj = Name()
print(f"Before change : {obj.a}")

obj.a = 0
print(f"After change : {obj.a}")

#Add static method in problem 2, to greet the user with hello

class calculator:

    def __init__(self,num):
        self.num = num
    
    @staticmethod   
    def greet():
        print("Hello")

    def calc(self):
        print(f"Square: {self.num ** 2}")
        print(f"Cube: {self.num ** 3}")
        print(f"Square Root: {self.num ** 0.5}")
    
    

a = calculator(9)
a.calc()

#Write a class Train which has a method to book a ticket , get status (no of seats) and get fare information of train running under Indian Railways

class Train:

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"Train: {self.name}")
        print(f"Available Seats: {self.seats}")

    def get_fare_info(self):
        print(f"Fare for {self.name} is ₹{self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            print(f"Ticket booked successfully for {self.name}!")
            self.seats -= 1
            print(f"Remaining Seats: {self.seats}")
        else:
            print("Sorry, no seats available.")


rajdhani = Train("Rajdhani Express", 1500, 5)

rajdhani.get_status()
rajdhani.get_fare_info()
rajdhani.book_ticket()
rajdhani.book_ticket()
rajdhani.get_status()


