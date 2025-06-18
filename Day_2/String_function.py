#String functions

#len(): returns length of the string.
name = "Edward"
print(len(name))

#Stringname.endswith(): tells whether the variable string ends with the mentioned string in () or not.
print(name.endswith("rd"))    #true/false
print(name.startswith("ED"))  #true/false
print(name.capitalize())      #capitalize first word

#string.find(word): finds the word and returns the index of first occurence of that word inn the string.
print(name.find("war"))

#string.replace(old word, new word)
s = "hello world"
print(s.replace("world","mate"))

#use chatgpt to find more string function.

'''
Escape sequence characters: Sequence of characters after backlash "\".

Escape sequence characters comprise of more than one character but represent one character when used within the strings

\n : new line   \t: tab   \;: single qoute  \\: backslash  etc. 
'''