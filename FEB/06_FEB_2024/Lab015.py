name = "Wonder Woman"
print(len(name)) #length starts at 1

#indexes start from zero but lenght starts from 1
print(name[0])
print(name[4])

#print(name[15])#Index out of range
print(len(name)-1)
print(name[len(name)-1])

#String - Immutability
#That can't be changed or modifies

string = 'Hello'
string[0] = 'P' #TypeError: 'str