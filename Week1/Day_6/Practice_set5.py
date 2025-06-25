#write a rpogram to findgreatest of four numbers entered by user
a = int(input("Enter number:" ))
b = int(input("Enter number:" ))
c = int(input("Enter number:" ))
d = int(input("Enter number:" ))

if(a>b) and (a>c) and (a>d):
    print(" Greatest number is",a)

elif(b>a) and (b>c) and (b>d):
    print(" Greatest number is",b)

elif(c>a) and (c>b) and (c>d):
    print(" Greatest number is",c)

else:
    print("Greatest number is ",d)

#write a program to find out whether a student is passed or failed, they need atleast 40% or 33%
#Assume 3 subjects and take marks as input

x = int(input("Enter marks (English):" ))
y = int(input("Enter marks (Mathematics):" ))
z = int(input("Enter marks (Science):" ))

avg = (x+y+z)/300
percentage = avg*100

if(percentage>40):
    print("You've Passed")

elif(percentage>=33):
    print("Retest!")

elif(33>percentage>0):
    print("Fail")

else:
    print("Invalid Marks!")


#detect spam

p1= "Make a lot of money!"
p2= "buy now"
p3= "subscribe this"
p4= "click this"

msg = input("Enter comment:")

if((p1 in msg) or (p1 in msg) or (p1 in msg) or (p1 in msg) ) :
    print("Spam Detected")

else:
    print("No Spam Detected!")



#write a program to find whether username contains less than 10 charaters or not

username=input("Enter username: ")

if(len(username)<10):
    print("Your username has less than 10 characters")

else:
    print("Valid Username")


#write a program which finds out the name is in list or not

l = ["Reena","Raj","Kashish","Joel"]

name = input("Enter name:")

if(name in l):
    print("Your name is listed")

else:
    print("Your name is not listed!")


#make a grade system

marks = int(input("Enter total marks: "))

if(100 <= marks and marks >=90 ):
    print("Excellent")
elif(90 < marks and marks >=80 ):
    print("A")
elif(80 < marks and marks >=70 ):
    print("B")
elif(70 <= marks and marks >=60 ):
    print("C")
elif(60 <= marks and marks >=50 ):
    print("D")
elif(marks < 50 ):
    print("Fail")
else:
    print("Invalid Marks!")








