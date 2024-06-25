#String is a bunch of characters

name = 'Kristen'
name2 = 'Lanier'
print(name)
print(name2)
print(type(name))
print(type(name2))

directory = 'C:.abc/abc.txt'
print(directory)

dir = "C:\abc\abc.txt"
print(dir)

dire = "C :\abc\\abc\\.txt"


#raw String
#This will be helpful in the dir paths
dir = r'C:\namedir\aome dir'
print(dir)

#format String f
first_name = "Kristen"
last_name = "Jones"
age = 28
isMarried = True
print(f"Your name is {first_name} {last_name}, and you're married: {isMarried} your age is {age}.")