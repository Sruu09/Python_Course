'''
'Break' statement is used come out of an loop when encountered. It instructs the program to exit the loop
'''

for i in range (0,8):
    if i == 3:
        break         #ends loop at 3
    print(i)
    


'''
'Continue' is used to stop the current iteration of the loop and continue woth next one. It instructs the program to skip the iteration
'''
for i in range (0,10):
    if i == 6:
        continue   #skips 6 and continues
    print(i)
    


'''
Pass statement is a null statement in python.
It instructs to do nothing
'''

l = [1,7,8]
for i in l:
    pass          #meaning you can skip this loop for now and work on some other loop
