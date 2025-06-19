'''
String is a data type in python
String is a sequence of characters enclosed in qoutes
We can primarily write a string in three ways
'hey' "hey"  
Also in triple single quotes to write multi lines
String is immutable
'''

#String slicing : It can be sliced to get a part of string

name = "Roller" # negative indexing starts from -1 right to left!

name1= len(name)
print(name1)  #6

name2 = name[0:3] # index 0 1 2 excluded:3
print(name2)  #Rol

print(name[4])
print(name[ :4])  #starts from 0
print(name[2:])   #till end 
print(name[2:6])  

#Slicing with skip value 

word = "amazing"
print(word[1:6:3])  #start:stop:step
