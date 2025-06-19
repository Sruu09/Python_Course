'''
if else and elif
They are a multiway decision taken by our program due to certain conditions in our code

Syntax:

       if(condition1):     #if condition1 is True
           print("yes")
       elif(condition2):   #if condition2 is True 
           print("no")
       else:               #otherwise 
           print("maybe")   
'''
# If elif else ladder
a = int(input("Enter your age: "))

if(a>=18):
    print("You are an adult")

elif(a<=0):
    print("Not a valid age!")

else:
    print("You are not an adult")