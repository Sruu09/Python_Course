#Write a program using functions to find grreatest of three number
a = 1
b = 2
c = 3
def greatest(a,b,c):
    if(a>b and a>c):
        print(f"{a} is the greatest number") 
    elif(b>a and b>c):
        print(f"{b} is the greatest number")
    else:
        print(f"{c} is the greatest number")

    print(greatest(a,b,c))



#Write program to convert Celcius to Farenheit

def conv(c):
    f =  (c * 9/5)+32 
    return f


c = int(input("Enter temperature in Celcius:"))
print("Celsius:",c)

print("Fahrenheit:",conv(c))


#Write a recursive function to calculate the sum of first n natural numbers

def cal_sum(n):
    if (n == 1):
        return 1
    return cal_sum(n-1)+n

n = int(input("Enter number:"))
print(cal_sum(n))
    
#print pattern 
'''
***
**
*
'''

def pattern(s):
    for i in range(s,0,-1):
        print('*'* i)

s = int(input("Enter number:"))
pattern(s)

#write a function to convert inches to cms

def conv(inches):
    cm = inches * 2.54
    return cm

inches = float(input("Enter length in inches: "))
print("Inches:", inches)

print("Centimeters:", conv(inches))



#write a function to remove a given word from list add stip it at the same time
def clean_list(word_to_remove, words):
    result = []
    for w in words:
        w = w.strip()
        if w != word_to_remove:
            result.append(w)
    return result

words = [' apple ', 'banana', ' banana ', 'orange ']
print(clean_list('banana', words))

#write a function to print multiplication table
def multiplication_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
multiplication_table(num)


