#Write a program to print multiplication table using loop
num = 2
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1


#Write a program to greet all the person names stored in a list l which starts with s
l = ["Jinal","Sachin","Soham","Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")


#Write a program to find whether given number is prime or not
 
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


#Write a code to print sum of n numbers
n = int(input("Enter number:"))
i = 0
sum = 0
while(i<=n):
    sum += i
    i += 1
print(sum)

#Write a program to calculate the factorial of a given number using loop
n = int(input("Enter number:"))
i = 0
sum = 1
while(i<= n):
    sum *= i
    i += 1
print(sum)

'''
write a program to print following star pattern:
  *
 ***
*****
'''

n = int(input("Enter number:"))
for i in range (1,n+1):
    print(" " * (n-i) + "*" * (2*i-1))

'''
print following star pattern:

*
**
***

'''
n = int(input("Enter number:"))
for i in range (1,n+1):
    print(" " * (n-i) + "*" * (i))


'''
print following star pattern:
***
* *
***
'''
n = int(input("Enter number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")

    