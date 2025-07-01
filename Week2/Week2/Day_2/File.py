'''

'''
#read
f = open("Hello.txt")
data = f.read()
print(data)
f.close

#write
st = "Hey, i'm doing great!"
f=open("Hello.txt","w")
f.write(st)
f.close()