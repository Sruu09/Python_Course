#String Practice Set

#write a program to display a user entered  followed by Good Afternoon using input() function.

name = input("Enter Your Name: ")
print(f"Good Afternoon {name}")

#Write a program to fill in a letter template given beloow with  and date 
letter =''' Dear <|Name|>
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>","Srushti").replace("<|Date|>", "18 June 2025"))

#Write a program to detect double spacing in a string
name2 = "Hello! Have a lovely  day!"
print(name2.find("  "))

#Replace the double spcae from above problem with single space

print(name2.replace("  "," "))

#write a program to format the following letter using escape sequence characters
lletter = "Dear Harry,\n\t this python course is nice.\nThanks!"

print(lletter)

