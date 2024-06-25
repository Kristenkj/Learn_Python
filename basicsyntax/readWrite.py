file = open('test.txt')  #pass the path

#file.read() #Read all the contencts of the file
"""
have to provide print to see the contents that were read
Passing n means that only the first n characters in the file will be read - print(file.read(n))
Not passing anything means that everything will be read
"""
#print(file.read())

#Prints/reads line by line
#print(file.readline())
#print(file.readline())


"""
Print line by line using readLine method
"""

"""
line = file.readline()

while line != "":
    print(line)
    line = file.readline()
"""


#Each and every line is stored in a list. Easier to iterate and extract the values
for line in file.readlines():
    print(line)

file.close()
