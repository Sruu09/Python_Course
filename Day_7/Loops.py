'''
Primarily there are 2 types of loops:
1) while loop     2) for loop

-while loop:
while(condition):
       body of loop

In while loop comdition is checked first.
If it evaluates as true then the body is executed otherwise not!
If the loop is entered the process is executed until the condition becomes false!
'''

i = 1

while(i<6):
    print(i)
    i += 1


l = [1,"Hari",False,"This","Rohan","Shubham","Shubhi"]

j = 0

while (i<len(l)):
    print(l[i])
    i += 1


'''
range() is used to generate sequence of numbers

Syntax:
range(start,stop,step)

'''

for i in range(0,7):
    print(i)            #prints 0 to 6





'''
A for loop is used to iterate through a sequence like list,tuple or string

syntax:

l = [1,3,5,8]
for item in l:
    print(item)
'''
l = [1,3,5,8]
for item in l:
    print(item)



m = [1,5,4,6,8]
for item in m:
    print(item)

else:
    print("done")